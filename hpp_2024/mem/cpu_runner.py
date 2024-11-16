from matplotlib import pyplot as plt

from hpp_2024.mem.cpu1 import experiment

if __name__ == '__main__':
    n_workers = [1, 2, 4, 6, 8, 10, 12, 16]
    times = []
    cpu_usage = []

    for n_work in n_workers:
        res, exec_time = experiment(n_epochs=5000, n_workers=n_work)
        times.append(exec_time)
        cpu_usage.append(exec_time * n_work)

    plt.figure(figsize=(8, 6))
    plt.plot(n_workers, times, 'bo-', linewidth=2, markersize=8, label='exec time')
    plt.plot(n_workers, cpu_usage, 'r^-', linewidth=2, markersize=8, label='CPU Usage')

    plt.xlabel('Number of Workers')
    plt.ylabel('Execution Time (s)')
    plt.title('Execution Time vs Number of Workers')
    plt.grid(True)
    plt.show()
