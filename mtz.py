import matplotlib.pyplot as plt
import numpy as np


class ShowData:
    def __init__(self, file_path):
        file = open(file_path, 'r')

        masN = list(map(int, file.readline().split()))
        hy = list(map(int, file.readline().split()))
        hz = list(map(int, file.readline().split()))
        rho = np.empty((len(hy), len(hz)), dtype=int)

        for i in range(len(hz)):
            rho[i] = list(map(int, file.readline().split()))

        fig, ax = plt.subplots(1, figsize=(5, 5), constrained_layout=True)

        p2 = ax.imshow(rho, cmap='jet', aspect='auto', interpolation='gaussian', origin="upper",
                       extent=(0, 1000, 0, 1000))
        fig.colorbar(p2, ax=ax)
        ax.invert_yaxis()
        plt.show()


if __name__ == "__main__":
    ShowData("test_data/x.txt")
