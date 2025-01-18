from asyncio import sleep

import pytest
from pydantic import BaseModel

from hpp_2024.assynk.starship.model import Ship, add, Action, EventLogger, EventType


@pytest.fixture
async def ship():
    return Ship()


@pytest.mark.asyncio
async def test_can_add(ship):
    res = await add(1, 2)
    assert res == 3


def test_bla_bla():
    x = 1
    y = 15
    z = x + y
    assert z == 16


async def test_can_start_engine():
    actions = [(Action.ENGINE_START, 0), ]


async def test_can_start_ship():
    actions = [(Action.ENGINE_START, 0), (Action.SHIP_START, 0.1)]

    # assert ENGINE_RUNNING
    # assert SHIP_RUNNING
    # assert SHIP_RUNNING after ENGINE_RUNNING
    # assert SHIP_RUNNING at least 0.1s after ENGINE_RUNNING


@pytest.mark.asyncio
async def test_event_logger():
    logger = EventLogger()
    logger.log(EventType.SHIP_STARTED)
    logger.log(EventType.FTS_EXPLODED)

    log = logger.get_events_of_type(event_types=[])  # all
    types = [l.event_type for l in log]
    assert types == [EventType.SHIP_STARTED, EventType.FTS_EXPLODED]


@pytest.mark.asyncio
async def test_event_logger_with_time():
    logger = EventLogger()
    logger.log(EventType.SHIP_STARTED)
    await sleep(0.1)
    logger.log(EventType.FTS_EXPLODED)

    log = logger.get_events_of_type(event_types=[])  # all

    assert log[1].timestamp - log[0].timestamp >= 0.1
