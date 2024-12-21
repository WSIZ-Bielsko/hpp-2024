import time
from asyncio import run, current_task, sleep, create_task
from datetime import datetime

from loguru import logger


def log(msg):
    logger.info(f'[{current_task().get_name()}] {msg}')


async def heat_up_pan(time: int = 10):
    log('heat_up_pan begin')
    await sleep(time * 0.1)
    log('heat_up_pan complete')


async def break_eggs(n_eggs: int = 2):
    log('break_eggs begin')
    await sleep(n_eggs * 0.1)
    log('break_eggs complete')


ts = lambda: datetime.now().timestamp()


async def cook(time: int = 3):
    st = ts()
    log('cook begin')
    await sleep(time)
    en = ts()
    log(f'cook complete in {en - st:.3f}s (expected: {time})')


async def pour_water(time: int = 3):
    log('pour_water begin')
    await sleep(time)
    log('pour_water complete')


async def enable_heater(time: float = 3):
    log('enable_heater begin')
    await sleep(time)
    log('enable_heater complete')


async def boil_water(time: int = 3):
    log('boil_water begin')
    await sleep(time)
    log('boil_water complete')


async def mail_delivery(duration: int = 3):
    log('postman arrived')
    time.sleep(duration)
    log('mail delivered')


async def prepare_scrambled_eggs():
    await heat_up_pan(10)
    await break_eggs(5)
    await cook(3)


async def prepare_water():
    await pour_water(1)
    await enable_heater(0.5)
    await boil_water(2)


async def prepare_breakfast():
    # await prepare_scrambled_eggs()
    # await prepare_water()

    se = create_task(prepare_scrambled_eggs())
    wa = create_task(prepare_water())
    log('--- tasks submitted ----')
    # ah...... ringing at the doors...
    await sleep(1)
    await mail_delivery(10)
    await sleep(100)


if __name__ == '__main__':
    run(prepare_breakfast())
