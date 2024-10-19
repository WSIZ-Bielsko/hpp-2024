from concurrent.futures import wait
from datetime import datetime
from time import sleep


def ts() -> float:
    return datetime.now().timestamp()




if __name__ == '__main__':
    st = ts()
    sleep(0.5)
    en = ts()
    print(f'elapsed: {en-st:.3f}s')