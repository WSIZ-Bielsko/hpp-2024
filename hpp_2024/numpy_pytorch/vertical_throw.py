from datetime import datetime
from random import random

import numpy as np


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


def ts() -> float:
    return datetime.now().timestamp()


def get_particle_positions(init_height: float, acc: float) -> list[float]:
    """
    cząstka startuje na wysokości init_height; spada w dół z przyspieszeniem acc;
    jeśli zejdzie poniżej s=0, to zamieniamy v -> -v

    :param init_height:
    :param acc:
    :return:
    """
    pass


def vertical_throw(init_height: float, init_velo: float, duration: float = 1) -> tuple[float, float]:
    g = -9.81
    t = 0
    h = init_height
    v = init_velo
    dt = 0.01
    while t < duration:
        h += v * dt
        v += g * dt
        t += dt
        if h < 0:
            v *= 0.99
            v = -v
    return h, v


def get_random_particles(n_particles: int) -> tuple[list[float], list[float]]:
    heights = [random() * 1000 for _ in range(n_particles)]
    velocities = [random() * 10 - 5 for _ in range(n_particles)]
    return heights, velocities


def simulate(heights: list[float], velocities: list[float], duration: float) -> tuple[list[float], list[float]]:
    n_heights = []
    n_velocities = []
    for h, v in zip(heights, velocities):
        nh, nv = vertical_throw(h, v, duration)
        n_heights.append(nh)
        n_velocities.append(nv)
    return n_heights, n_velocities


def plot_histo(data: list[float]):
    import matplotlib.pyplot as plt
    plt.hist(data, bins=100)
    plt.show()


def generate_conserved_velocities(velocities):
    # Assuming 'velocities' is your original numpy array of shape (n, m)
    # where n is the number of particles and m is the number of velocity components

    # Step 1: Calculate the total momentum and kinetic energy of the original velocities
    total_momentum = np.sum(velocities, axis=0)
    total_kinetic_energy = 0.5 * np.sum(velocities ** 2)

    # Step 2: Generate new random velocities
    new_velocities = np.random.randn(*velocities.shape)

    # Step 3: Rescale the new velocities to conserve the total momentum
    momentum_scale = np.sqrt(np.sum(new_velocities ** 2) / np.sum(velocities ** 2))
    new_velocities *= momentum_scale

    # Step 4: Adjust the total momentum to match the original
    momentum_difference = total_momentum - np.sum(new_velocities, axis=0)
    new_velocities += momentum_difference / velocities.shape[0]

    # Step 5: Adjust the new velocities to conserve kinetic energy
    new_kinetic_energy = 0.5 * np.sum(new_velocities ** 2)
    energy_scale = np.sqrt(total_kinetic_energy / new_kinetic_energy)
    new_velocities *= energy_scale

    # Now 'new_velocities' has the same total momentum and kinetic energy as 'velocities'
    return new_velocities


def get_average_velocity(heights: list[float], velocities: list[float], height_range: tuple[float, float]) -> float:
    """
    Find average absolute velocity for particles between height_range[0] and height_range[1]

    :param heights:
    :param velocities:
    :param height_range:
    :return:
    """
    pass


if __name__ == '__main__':
    # todo: use the code below, but for an ensamble of N=100 particles
    # heights, velocities = get_random_particles(n_particles=100)
    # for step in range(10000):
    #     n_heights, n_velocities = simulate(heights, velocities, duration=0.3)
    #     heights, velocities = n_heights, n_velocities
    #     # print(f'h={heights[0]:.2f} v={velocities[0]:.2f}')
    # plot_histo(velocities)

    # h = 10
    # v = 0
    # for _ in range(10):
    #     h, v = vertical_throw(h, v, duration=1)
    #     print(f'h={h:.2f} v={v:.2f}')

    d = [1, -1, 3.14, 1.41]
    d = np.array(d)
    x = generate_conserved_velocities(d)
    print(x)
    print(np.sum(d), np.sum(x))
    print(np.sum(d**2), np.sum((x**2)))

