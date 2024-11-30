from random import random, gauss
import matplotlib.pyplot as plt



if __name__ == '__main__':
    # x = [gauss(mu=0,sigma=1) for _ in range(10**5)]
    # y = [gauss(mu=0.5,sigma=1) for _ in range(10**5)]
    s = 111
    # pad = []
    # for _ in range(5 * 10 ** 6):
    #     a = 107
    #     c = 253
    #     m = 1007
    #     s = (a * s + c) % m
    #     pad.append(s / m)

    # pad = [get_random() for _ in range(5 * 10 ** 6)]
    # x = pad[:5 * 10 ** 4]
    # y = pad[10 ** 3 : 10 ** 3 + 5 * 10 ** 4]

    x = [random() for _ in range(5 * 10**3)]
    y = [random() for _ in range(5 * 10**3)]


    plt.scatter(x, y, s=1)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Random Scatter Plot')
    plt.grid(True)
    plt.show()
