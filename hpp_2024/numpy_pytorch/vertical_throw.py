

def sim_distance(acc: float, duration: float) -> float:

    s = 0
    v = 0
    dt = 0.01
    t = 0

    while t < duration:
        s += v * dt
        v += acc * dt
        t += dt
    return s


def get_particle_positions(init_height: float, acc: float) -> list[float]:
    """
    cząstka startuje na wysokości init_height; spada w dół z przyspieszeniem acc;
    jeśli zejdzie poniżej s=0, to zamieniamy v -> -v

    :param init_height:
    :param acc:
    :return:
    """
    pass


def vertical_throw(init_height: float, init_velo: float, duration: float = 1):
    g = -9.81
    duration = 10
    t = 0
    h = init_height
    v = init_velo
    dt = 0.01
    tt = 0
    while t < duration:
        h += v * dt
        v += g * dt
        t += dt
        tt += dt
        if h < 0:
            v *= 0.99
            v = -v

        if tt > 0.1:
            print(f'h={h:.2f} v={v:.2f}')
            tt = 0


if __name__ == '__main__':
    vertical_throw(init_height=10, init_velo=0, duration=10)
