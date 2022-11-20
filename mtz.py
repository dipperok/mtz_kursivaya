import matplotlib.pyplot as plt
import numpy as np


class ShowData:
    def __init__(self, file_path):
        file = open(file_path, 'r')

        # mas_n = list(map(int, file.readline().split()))
        h_y = list(map(int, file.readline().split()))
        h_z = list(map(int, file.readline().split()))

        # print(h_y)
        # print(len(h_z))

        rho = np.empty((len(h_y), len(h_z)), dtype=int)

        for i in range(len(h_z)):
            rho[i] = list(map(int, file.readline().split()))

        fig, ax = plt.subplots(1, figsize=(5, 5), constrained_layout=True)

        p2 = ax.imshow(rho, cmap='jet', aspect='auto', interpolation='gaussian', origin="upper",
                       extent=(0, 1000, 0, 1000))
        fig.colorbar(p2, ax=ax)
        ax.invert_yaxis()
        plt.show()
