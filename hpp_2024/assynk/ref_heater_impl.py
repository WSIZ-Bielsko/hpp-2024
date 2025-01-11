import random
from asyncio import run, sleep, create_task, gather

from loguru import logger
from pydantic import BaseModel


class SharedData(BaseModel):
    run_sensor: bool
    temperature: float
    heating: float

    def __str__(self) -> str:
        return f"temperature={self.temperature:.2f}, heating={self.heating:.2f}"


async def sensor_loop(shared_data: SharedData):
    while shared_data.run_sensor:
        await sleep(0.1)
        shared_data.temperature += shared_data.heating + random.random()
        logger.info(shared_data)


async def heater_loop(shared_data: SharedData):
    while shared_data.run_sensor:
        await sleep(0.02)
        if shared_data.temperature > 30:
            shared_data.heating = -2
        elif shared_data.temperature > 28:
            shared_data.heating = -1
        elif shared_data.temperature < 22:
            shared_data.heating = 1
        else:
            shared_data.heating = 0


async def main():
    logger.info("Starting up")
    dd = SharedData(run_sensor=True, temperature=25.0, heating=0.0)
    create_task(sensor_loop(dd))
    create_task(heater_loop(dd))
    await sleep(2)
    dd.temperature = 50
    await sleep(2)
    logger.info("Shutting down")

if __name__ == '__main__':
    run(main())
