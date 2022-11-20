import matplotlib.pyplot as plt
import numpy as np


class data_show:
    def __init__(self, file_path):
        file = open(file_path, 'r')
        MasN = list(map(int, file.readline().split()))
        Hy = list(map(int, file.readline().split()))
        Hz = list(map(int, file.readline().split()))
        print(Hy)
        print(len(Hz))
        rho = np.empty((len(Hy), len(Hz)), dtype=int)

        for i in range(len(Hz)):
            rho[i] = list(map(int, file.readline().split()))

        fig, ax = plt.subplots(1, figsize=(5, 5), constrained_layout=True)

        p2 = ax.imshow(rho, cmap='jet', aspect='auto', interpolation='gaussian', origin="upper",
                       extent=(0, 1000, 0, 1000))
        fig.colorbar(p2, ax=ax)
        ax.invert_yaxis()
        plt.show()
