from asyncio import run
from loguru import logger
from model import *


async def test_engine():
    action_bus = ActionBus()
    event_logger = EventLogger()

    # utworzenie obiektu "engine"; narazie nie będzie odpowiadał na żadne actions
    engine = Engine(action_bus=action_bus, event_logger=event_logger, frequency=1)

    await engine.initialize()
    # od teraz engine nasłuchje na "actions"

    action_bus.submit_action(ActionType.ENGINE_START)
    logger.debug(engine.is_running)
    await sleep(0.1)
    logger.debug(engine.is_running)

    action_bus.submit_action(ActionType.ENGINE_STOP)
    await sleep(0.1)
    logger.debug(engine.is_running)

    # attempted restart
    action_bus.submit_action(ActionType.ENGINE_START)
    await sleep(0.1)
    logger.debug(engine.is_running)


async def test_fts():
    action_bus = ActionBus()
    event_logger = EventLogger()

    # utworzenie obiektu "fts"; narazie nie będzie odpowiadał na żadne actions
    fts = FTS(action_bus=action_bus, event_logger=event_logger, frequency=1)

    await fts.initialize()
    # od teraz fts nasłuchje na "actions"
    await sleep(0.1)

    logger.debug(fts.state)
    action_bus.submit_action(ActionType.FTS_ARM)
    await sleep(0.01)
    logger.debug(fts.state)
    action_bus.submit_action(ActionType.FTS_DISARM)
    await sleep(0.01)
    logger.debug(fts.state)
    action_bus.submit_action(ActionType.FTS_ARM)
    await sleep(0.01)
    logger.debug(fts.state)
    action_bus.submit_action(ActionType.FTS_EXPLODE)
    await sleep(0.01)
    logger.debug(fts.state)


async def main():
    await test_fts()


if __name__ == '__main__':
    run(main())
