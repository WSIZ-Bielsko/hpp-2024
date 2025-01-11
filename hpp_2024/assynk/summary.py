import random
from asyncio import run, sleep, create_task, gather

from loguru import logger
from pydantic import BaseModel


class SharedData(BaseModel):
    run_sensor: bool
    measurement: float


async def job(i: int) -> int:
    logger.info(f'from job {i}')
    await sleep(0.5)
    logger.info(f'from job {i} - done')
    return i


async def sensor_loop(shared_data: SharedData):
    while shared_data.run_sensor:
        logger.info(f'sensor measure')
        await sleep(0.1)
        shared_data.measurement = random.random()


async def main():
    logger.info('from main')
    dd = SharedData(run_sensor=True, measurement=0)
    create_task(sensor_loop(dd))

    z = await job(12)  # czekamy na zakończenie tego job-a; tworzymy zadanie i czekamy na jego wynik
    logger.info(f'job 12 returned: {z}')

    t1 = create_task(job(11))  # "fire and forget": tworzymy zadanie ...
    t2 = create_task(job(10))

    logger.info(f'from main - job done; temperature = {dd.measurement}')

    # now awaiting created tasks
    # z1 = await t1  # czekamy na wynik zadania
    # z2 = await t2
    print(t1.done())
    z1, z2 = await gather(t1, t2)
    logger.info(f'job 11 returned: {z1}')
    dd.run_sensor = False
    logger.warning(f'all tasks done -- exiting main; temperature = {dd.measurement}')


if __name__ == '__main__':
    run(main())
