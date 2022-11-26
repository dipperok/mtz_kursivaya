import matplotlib.pyplot as plt
import numpy as np


class ShowData:
    def __init__(self, file_path):
        self.file = open(file_path, 'r')

        self.mas_n = list(map(int, self.file.readline().split()))
        self.h_z = list(map(int, self.file.readline().split()))
        self.h_y = list(map(int, self.file.readline().split()))
        self.rho = np.empty((len(self.h_y), len(self.h_z)), dtype=float)

        for i in range(len(self.h_z)):
            self.rho[i] = list(map(int, self.file.readline().split()))
        
        self.list_x, self.list_y = [], []

        for i in range(len(self.h_y)):
            self.list_x.append(np.sum(self.h_y[:i])/1000)

        for i in range(len(self.h_z)):
            self.list_y.append(np.sum(self.h_z[:i])/1000)

        self.position_y = np.arange(len(self.list_x))
        self.position_z = np.arange(len(self.list_y))


if __name__ == "__main__":
    ShowData("test_data/x.txt")
