from abc import abstractmethod, ABC
from asyncio import sleep
from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class AsyncComponent(ABC):

    @abstractmethod
    async def initialize(self, event_logger: 'EventLogger', action_bus: 'ActionBus'):
        pass

    @abstractmethod
    async def run(self):
        pass

    async def terminate(self):
        pass


class Action(Enum):
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
    event_type: EventType
    timestamp: float


class EventLogger:
    def __init__(self):
        self.events: list[Event] = []

    def log(self, event: EventType):
        self.events.append(Event(event_type=event, timestamp=datetime.now().timestamp()))

    def get_events_of_type(self, event_types: list[EventType]) -> list[Event]:
        """list all events with types as in event_types, or all if this list is empty
          events are listed in order in which they were submitted to EventLogger
        """
        if event_types == []:
            return self.events
        else:
            return [e for e in self.events if e.event_type in event_types]


class ActionBus:
    def __init__(self):
        self.action_id = 0
        self.actions: list[tuple[int, Action]] = []

    def submit_action(self, action_type: Action):
        self.action_id += 1
        self.actions.append((self.action_id, action_type))

    def get_actions_since(self, action_id) -> list[Action]:
        pass


class HQ(AsyncComponent):
    def __init__(self):
        pass


class Ship(AsyncComponent):
    def __init__(self):
        pass


class FTS(AsyncComponent):
    def __init__(self):
        pass


class Engine(AsyncComponent):
    def __init__(self):
        pass


async def add(a, b):
    await sleep(0.01)
    return a + b
