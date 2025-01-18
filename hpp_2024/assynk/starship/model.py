from abc import abstractmethod, ABC
from asyncio import sleep
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class AsyncComponent(ABC):

    def __init__(self, event_logger: 'EventLogger', action_bus: 'ActionBus'):
        self._event_logger = event_logger
        self._action_bus = action_bus
        self.__last_action_id = 0

    @abstractmethod
    async def initialize(self):
        pass

    @abstractmethod
    async def run(self):
        pass

    @abstractmethod
    async def terminate(self):
        pass

    @abstractmethod
    async def act_on(self, action: 'ActionType'):
        # should never let any exception out
        pass

    def log(self, event: 'EventType'):
        # reference impl
        self._event_logger.log(event)

    async def process_actions(self):
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

    # SHIP
    SHIP_STARTED = 100

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
        if event_types == []:
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
        pass


class Engine(AsyncComponent):
    def __init__(self, event_logger: 'EventLogger', action_bus: 'ActionBus'):
        super().__init__(event_logger, action_bus)
        self.started = False

    async def initialize(self):
        pass

    async def run(self):
        while True:
            await self.process_actions()
            await sleep(0.05)

    async def terminate(self):
        pass

    async def act_on(self, action: 'ActionType'):
        if action == ActionType.ENGINE_START:
            self.started = True

    def log(self, event: 'EventType'):
        super().log(event)

    async def process_actions(self):
        return await super().process_actions()


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
