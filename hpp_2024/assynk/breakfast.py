from asyncio import run, current_task, sleep

from loguru import logger


def log(msg):
    logger.info(f'[{current_task().get_name()}] {msg}')


async def break_eggs(n_eggs: int = 2):
    logger.info('break_eggs begin')
    await sleep(n_eggs * 0.1)
    logger.info('break_eggs complete')


async def main():
    t = break_eggs(1)
    print('here')
    await sleep(4)
    print('done')

if __name__ == '__main__':
    run(main())
