from random import random
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = [random() for _ in range(10**4)]
    y = [random() for _ in range(10**4)]

    plt.scatter(x, y, s=2)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Random Scatter Plot')
    plt.grid(True)
    plt.show()