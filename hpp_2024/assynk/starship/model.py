from abc import abstractmethod, ABC
from asyncio import sleep, create_task
from datetime import datetime
from enum import Enum

from pydantic import BaseModel
from loguru import logger

class Clock:
    delta_t = 0.001

    # one CLK event in all systems executes in delta_t real time

    @staticmethod
    def ts():
        return datetime.now().timestamp()


class ShipError(RuntimeError):
    def __init__(self, message):
        super().__init__(message)


class AsyncComponent(ABC):

    def __init__(self, event_logger: 'EventLogger', action_bus: 'ActionBus', frequency: int = 1):
        """

        :param event_logger: Common EventLogger for all AsyncComponents
        :param action_bus: Common ActionBus for all AsyncComponents
        :param frequency: this component with periodically execute actions every Clock.dt * frequency seconds
        """
        self._event_logger = event_logger
        self._action_bus = action_bus
        self.__last_action_id = 0
        self.frequency = frequency
        self.__should_be_running = False  # starts internal loop
        self._is_running = False  # true if this component is "usable" (after startup)

    def __del__(self):
        logger.warning(f'Shutting down {self.__class__.__name__}')
        self.__should_be_running = False


    async def initialize(self):
        """Only way to actually start component's internal loop (so it listens for Actions)"""
        logger.info('initializing component')
        await sleep(Clock.delta_t * self.frequency * 5)
        create_task(self.__run())

    @abstractmethod
    async def act_on(self, action: 'ActionType'):
        # should never let any exception out
        pass

    # aspects of "running" -- does it run (now, already?, still?)
    @property
    def is_running(self) -> bool:
        return self._is_running

    async def running_gate(self, desired_running=True, timeout_clks=10 ** 12):
        """Await-able startup/shutdown 'gate'; await this method to unblock as soon as the component is started"""
        start = Clock.ts()
        while self.is_running != desired_running:
            if Clock.ts() - start > Clock.delta_t * timeout_clks:
                raise ShipError(f'Timeout while waiting is_running={desired_running} of {self.__class__.__name__}')
            await sleep(Clock.delta_t * self.frequency)

    async def __run(self):
        """Component can be started only by an Action -> hence private method"""
        if self.__should_be_running:
            return
        self.__should_be_running = True
        while self.__should_be_running:
            await self.__process_actions()
            await sleep(Clock.delta_t * self.frequency)

    async def terminate(self):
        """Component can be stopped only by an Action -> hence private method"""
        self.__should_be_running = False
        await sleep(Clock.delta_t * self.frequency * 5)

    def _log(self, event: 'EventType'):
        # reference (and sufficient) implementation
        self._event_logger.log(event)

    async def __process_actions(self):
        # reference (and sufficient) implementation
        actions = self._action_bus.get_actions_since(self.__last_action_id)
        self.__last_action_id = actions[-1].id
        for action in actions:
            await self.act_on(action.type)


class ActionType(Enum):
    # ENGINES
    ENGINE_START = 0
    ENGINE_STOP = 1

    # SHIP
    SHIP_START = 100

    # HQ

    # FTS
    FTS_EXPLODE = 500

    # CONNECTIONS
    CONNECT_HQ_SHIP = 600
    CONNECT_SHIP_ENGINE = 601
    CONNECT_SHIP_FTS = 602

    DISCONNECT_HQ_SHIP = 603
    DISCONNECT_SHIP_ENGINE = 604
    DISCONNECT_SHIP_FTS = 605


class EventType(Enum):
    # ENGINES
    ENGINE_STARTED = 0
    ENGINE_STOPPED = 1
    ENGINE_ERROR = 99

    # SHIP
    SHIP_STARTED = 100
    SHIP_ERROR = 199

    # HQ
    HQ_CONNECTED_TO_SHIP = 200

    # FTS
    FTS_EXPLODED = 500

    # CONNECTIONS
    CONNECTION_HQ_SHIP_ESTABLISHED = 600
    CONNECTION_SHIP_ENGINE_ESTABLISHED = 601
    CONNECTION_SHIP_FTS_ESTABLISHED = 602


class Event(BaseModel):
    type: EventType
    timestamp: float


class Action(BaseModel):
    type: ActionType
    id: int


class EventLogger:
    def __init__(self):
        self.events: list[Event] = []

    def log(self, event: EventType):
        self.events.append(Event(type=event, timestamp=datetime.now().timestamp()))

    def get_events_of_type(self, event_types: list[EventType]) -> list[Event]:
        """list all events with types as in event_types, or all if this list is empty
          events are listed in order in which they were submitted to EventLogger
        """
        if not event_types:
            return self.events
        else:
            return [e for e in self.events if e.type in event_types]


class ActionBus:
    def __init__(self):
        self.action_id = 0
        self.actions: list[Action] = []

    def submit_action(self, action_type: ActionType):
        self.action_id += 1
        self.actions.append(Action(id=self.action_id, type=action_type))

    def get_actions_since(self, action_id) -> list[Action]:
        action_id = max(action_id, 0)
        return self.actions[action_id:]


class Engine(AsyncComponent):
    async def act_on(self, action: 'ActionType'):
        if action == ActionType.ENGINE_START:
            await sleep(Clock.delta_t * self.frequency * 2)
            self._is_running = True
            self._log(EventType.ENGINE_STARTED)
        if action == ActionType.ENGINE_STOP:
            await sleep(Clock.delta_t * self.frequency * 2)
            self._is_running = False
            self._log(EventType.ENGINE_STOPPED)


class FTS(AsyncComponent):
    def __init__(self, event_logger: 'EventLogger', action_bus: 'ActionBus'):
        super().__init__(event_logger, action_bus)


class Ship(AsyncComponent):

    def __init__(self, event_logger: 'EventLogger', action_bus: 'ActionBus', engine: Engine, fts: FTS):
        super().__init__(event_logger, action_bus)
        self.engine = engine
        self.fts = fts


class HQ(AsyncComponent):
    def __init__(self, event_logger: 'EventLogger', action_bus: 'ActionBus'):
        super().__init__(event_logger, action_bus)


async def add(a, b):
    await sleep(0.01)
    return a + b
