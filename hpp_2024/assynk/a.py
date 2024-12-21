from asyncio import run, current_task, sleep, create_task, Task

from loguru import logger


def log(msg):
    logger.info(f'[{current_task().get_name()}] {msg}')


async def job(i) -> str:
    if i == 3:
        await sleep(0)
    log(f'job {i} starts')
    await sleep(0.1)
    log(f'job {i} complete')
    return f'result {i}'


async def main():
    log('from main')
    r1 = await job(1)  # uruchomienie typu "czekamy"
    r2: Task = create_task(job(2))  # 'uruchomienie "równoległe"'
    print(type(r2))
    r3 = await job(3)

    log(f'all tasks finished; results: {[r1, r2, r3]}')
    log(f'r2.result = {r2.result()}')


if __name__ == '__main__':
    logger.info('start')
    run(main())
    logger.info('end')
