import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mtz import RhoSeem

matplotlib.use('Qt5Agg')


class VisualMTZ(QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self, file_path):

        super(VisualMTZ, self).__init__()

        self.file_path = file_path
        self.data_analysed = RhoSeem(self.file_path)
        print(self.file_path)

        self.configure_window()  # Method to configure window parameters

        # Defining layouts for PyQt5 window
        self.layout = QGridLayout()
        self.menu_layout = QGridLayout()
        self.graph_layout = QVBoxLayout()

        # Defining menu_layout variables
        self.btn1 = QPushButton("Визуализировать данные", self)
        self.btn2 = QPushButton("Кривые ρ кажущегося", self)
        self.btn3 = QPushButton("Двумерный разрез ρ кажущегося", self)
        self.btn4 = QPushButton("Кривые φ", self)
        self.btn5 = QPushButton("Двумерный разрез φ", self)
        self.btn6 = QPushButton("Вернуться назад", self)

        self.create_menu_layout()  # method to configure menu_layout dependencies

        # Defining graph_layout and matplotlib variables
        # self.figure, self.axs = plt.subplots(1, figsize=(5, 5), constrained_layout=True)
        gs_kw = dict(width_ratios=[15, 1])
        self.figure, (self.axs, self.cax) = plt.subplots(1, 2, figsize=(5, 5),  constrained_layout=True, gridspec_kw=gs_kw)
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        self.cb = None

        self.create_graph_layout()  # method to configure graph_layout dependencies
        self.layouts_configure()  # Method to configure layouts

        self.show()

    # Method to config main window
    def configure_window(self):
        self.setWindowTitle('MTZ v1.0')
        self.resize(1280, 720)

    # Method to configure menu_layout vars and their alignments
    def create_menu_layout(self):
        self.btn1.clicked.connect(self.visual_mtz_file)
        self.btn1.setFixedHeight(35)

        self.btn2.clicked.connect(lambda: self.visual_rho(True))
        self.btn2.setFixedHeight(35)

        self.btn3.clicked.connect(lambda: self.visual_rho(False))
        self.btn3.setFixedHeight(35)

        self.btn4.clicked.connect(lambda: self.visual_phi(True))
        self.btn4.setFixedHeight(35)

        self.btn5.clicked.connect(lambda: self.visual_phi(False))
        self.btn5.setFixedHeight(35)

        self.btn6.clicked.connect(self.switch)
        self.btn6.setFixedHeight(35)

        self.menu_layout.addWidget(self.btn1, 0, 0*3, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn2, 0, 1*3, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn3, 0, 2*3, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn4, 0, 3*3, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn5, 0, 4*3, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn6, 0, 5*3, 1, 2, QtCore.Qt.AlignHCenter)

    def switch(self):
        self.close()
        self.switch_window.emit()

    # Method to configure graph_layout vars and their alignments
    def create_graph_layout(self):
        self.graph_layout.addWidget(self.toolbar)
        self.graph_layout.addWidget(self.canvas)

    # Method to configure layouts interposition and their relations
    def layouts_configure(self):
        self.layout.addLayout(self.graph_layout, 0, 0)
        self.layout.addLayout(self.menu_layout, 1, 0)
        self.setLayout(self.layout)


    def canvas_update(self):
        self.axs.clear()  # clear drawing axes

    # Method to visualisation mtz file
    def visual_mtz_file(self):
        if self.cb:
            self.figure.delaxes(self.figure.axes[1])

        # Configuration graph view
        self.axs.set_yscale("linear")
        self.axs.set_xticks(self.data_analysed.position_y)
        self.axs.set_yticks(self.data_analysed.position_z)
        self.axs.set_xticklabels(self.data_analysed.list_x)
        self.axs.set_yticklabels(self.data_analysed.list_y)
        self.axs.set_xlabel("Расстояние по горизонтали, км")
        self.axs.set_ylabel("Расстояние по вертикали, км")
        self.axs.set_xlim([0, self.data_analysed.position_y[-1]])
        self.axs.set_ylim([self.data_analysed.position_z[-1], 0])

        # Creating graph
        p = self.axs.imshow(self.data_analysed.rho, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
        self.figure.colorbar(p, cax=self.cax)
        self.cax.set_ylabel(r"Сопротивление, $\rho$ [$Ом \times м$]", rotation=90)
        self.figure.canvas.draw()

    # Rho seem visual
    def visual_rho(self, is_graph):
        self.canvas_update()

        if is_graph:
            self.cax.clear()
            temp_mas = np.log10(np.array(self.data_analysed.row_solutions))
            self.axs.plot([i+1 for i in range(len(temp_mas))], temp_mas)

            self.axs.set_yscale('log')
            self.axs.set_xticks([i+1 for i in range(len(self.data_analysed.row_solutions))])
            self.axs.set_xticklabels([i+1 for i in range(len(self.data_analysed.row_solutions))])
            self.axs.set_xlim([1, len(self.data_analysed.row_solutions)])
            self.axs.set_xlabel("Номер пикета")
            self.axs.set_ylabel(r"Кажущееся сопротивление, $lg(\rho_{T})$")

            legend_marks = [self.data_analysed.t1 * 2**(i+1) for i in range(len(self.data_analysed.row_solutions[0]))]
            self.axs.legend(legend_marks, title=r"Периоды, $T [с]$")
            self.figure.canvas.draw()
        else:
            self.axs.set_xticks(self.data_analysed.position_y)
            self.axs.set_xticklabels(self.data_analysed.list_x)
            self.axs.set_xlim([0, self.data_analysed.position_y[-1]])
            self.axs.set_xlabel("Расстояние по горизонтали, км")

            periods = [self.data_analysed.t1 * 2**(i+1) for i in range(len(self.data_analysed.row_solutions[0]))]

            self.axs.set_yticks([i for i in range(len(periods))])
            self.axs.set_yticklabels(periods)
            self.axs.set_ylabel(r"Периоды, $T [с]$")

            temp_mas = np.log10(np.array(self.data_analysed.row_solutions).transpose())
            p2 = self.axs.imshow(temp_mas, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
            self.figure.colorbar(p2, cax=self.cax)
            self.cax.set_ylabel(r"Кажущееся сопротивление, $lg(\rho_{T})$", rotation=90)
            self.figure.canvas.draw()

    # Phi visual
    def visual_phi(self, is_graph=True):
        self.canvas_update()

        if is_graph:
            self.cax.clear()
            self.axs.plot([i+1 for i in range(len(self.data_analysed.phi_solutions))], self.data_analysed.phi_solutions)

            self.axs.set_xticks([i+1 for i in range(len(self.data_analysed.phi_solutions))])
            self.axs.set_xticklabels([i+1 for i in range(len(self.data_analysed.phi_solutions))])
            self.axs.set_xlim([1, len(self.data_analysed.phi_solutions)])
            self.axs.set_xlabel("Номер пикета")
            self.axs.set_ylabel(r"Фаза импеданса, $\phi$")

            legend_marks = [self.data_analysed.t1 * 2**(i+1) for i in range(len(self.data_analysed.phi_solutions[0]))]
            self.axs.legend(legend_marks, title=r"Периоды, $T [с]$")
            self.figure.canvas.draw()
        else:
            self.axs.set_xticks(self.data_analysed.position_y)
            self.axs.set_xticklabels(self.data_analysed.list_x)
            self.axs.set_xlim([0, self.data_analysed.position_y[-1]])
            self.axs.set_xlabel("Расстояние по горизонтали, км")

            periods = [self.data_analysed.t1 * 2**(i+1) for i in range(len(self.data_analysed.phi_solutions[0]))]

            self.axs.set_yticks([i for i in range(len(periods))])
            self.axs.set_yticklabels(periods)
            self.axs.set_ylabel(r"Периоды, $T [с]$")

            temp_mas = np.array(self.data_analysed.phi_solutions).transpose()
            p2 = self.axs.imshow(temp_mas, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
            self.figure.colorbar(p2, cax=self.cax)
            self.cax.set_ylabel(r"Фаза импеданса, $\phi$", rotation=90)
            self.figure.canvas.draw()

    def error_window(self):
        pass