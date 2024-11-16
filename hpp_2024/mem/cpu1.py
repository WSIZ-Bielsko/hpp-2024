import math
from concurrent.futures import ProcessPoolExecutor, wait
from datetime import datetime

from loguru import logger
from matplotlib import pyplot as plt


class L:
    def info(self, msg: str):
        now = datetime.now()
        tm = f"{now.strftime('%H:%M:%S')}.{now.microsecond // 1000:03d}"
        print(f'[{tm}] {msg}')


# logger = L()

def ts() -> float:
    return datetime.now().timestamp()


def run_it(n_epochs, worker_id: int):
    x = 0.0
    logger.info(f'job {worker_id} starting')
    for e in range(n_epochs):
        for i in range(10 ** 5):
            x += math.sin(i * 0.01)
    logger.info(f'job {worker_id} finished')
    return x


def experiment(n_epochs: int, n_workers: int):
    st = ts()

    # res = run_it(5000) # zwykłe uruchomienie kodu (bez wątków)

    # chcemy uruchomić na 10 workerach run_it(500)

    futures_ = []
    logger.info('starting execution')

    # PARALLEL CODE STARTS HERE
    with ProcessPoolExecutor(max_workers=n_workers) as ex:
        for w in range(n_workers):
            f = ex.submit(run_it, n_epochs // n_workers, worker_id=w)

            futures_.append(f)
            logger.info(f'job {w} submitted')

    wait(futures_)
    logger.info('all done')
    res = 0
    for f in futures_:
        res += f.result()
    # PARALLEL CODE ENDS HERE

    en = ts()
    print(f'{res=}')
    print(f'elapsed {en - st:.3f}s')
    return res, en - st


if __name__ == '__main__':
    n_workers = [1, 2, 4, 6, 8, 10, 12, 16]
    times = []
    cpu_usage = []

    for n_work in n_workers:
        res, exec_time = experiment(n_epochs=5000, n_workers=n_work)
        times.append(exec_time)
        cpu_usage.append(exec_time * n_work)

