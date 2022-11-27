import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QMessageBox
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from mtz import ShowData, RhoSeem

matplotlib.use('Qt5Agg')


class VisualMTZ(QWidget):
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
        self.btn2 = QPushButton("Визуализировать кривые rho кажущегося", self)
        self.btn3 = QPushButton("Визуализировать карту rho кажущегося", self)
        self.btn4 = QPushButton("Визуализировать кривые phi кажущегося", self)
        self.btn5 = QPushButton("Визуализировать карту phi кажущегося", self)

        self.create_menu_layout()  # method to configure menu_layout dependencies

        # Defining graph_layout and matplotlib variables
        self.figure, self.axs = plt.subplots(1, figsize=(5, 5), constrained_layout=True)
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

        self.menu_layout.addWidget(self.btn1, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn2, 0, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn3, 0, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn4, 0, 3, 1, 2, QtCore.Qt.AlignHCenter)
        self.menu_layout.addWidget(self.btn5, 0, 4, 1, 2, QtCore.Qt.AlignHCenter)

    # Method to configure graph_layout vars and their alignments
    def create_graph_layout(self):
        self.graph_layout.addWidget(self.toolbar)
        self.graph_layout.addWidget(self.canvas)

    # Method to configure layouts interposition and their relations
    def layouts_configure(self):
        self.layout.addLayout(self.graph_layout, 0, 0)
        self.layout.addLayout(self.menu_layout, 1, 0)
        self.setLayout(self.layout)

    # Placeholder for button 3 future function
    def evt_btn_clicked3(self):
        get_age, b_ok = QMessageBox.question(self, 'Справка', '12134')
        try:
            if b_ok:
                self.close()
            else:
                self.close()
        except Exception as err:
            print(err)

    def canvas_update(self):
        self.axs.clear()  # clear drawing axes

    # Method to visualisation mtz file
    def visual_mtz_file(self):
        if self.cb:
            self.figure.delaxes(self.figure.axes[1])

        file_data = ShowData(self.file_path)  # Object with calculated vars for mtz file

        # Configuration graph view
        self.axs.set_xticks(file_data.position_y)
        self.axs.set_yticks(file_data.position_z)
        self.axs.set_xticklabels(file_data.list_x)
        self.axs.set_yticklabels(file_data.list_y)
        self.axs.set_xlim([0, file_data.position_y[-1]])
        self.axs.set_ylim([file_data.position_z[-1], 0])

        # Creating graph
        p2 = self.axs.imshow(file_data.rho, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
        self.cb = self.figure.colorbar(p2, ax=self.axs)
        self.figure.canvas.draw()

    # Rho seem visual
    def visual_rho(self, is_graph):
        self.canvas_update()
        if is_graph:
            self.axs.plot([i+1 for i in range(len(self.data_analysed.row_solutions))], self.data_analysed.row_solutions)
            self.axs.set_xticks([i+1 for i in range(len(self.data_analysed.row_solutions))])
            self.axs.set_xticklabels([i+1 for i in range(len(self.data_analysed.row_solutions))])
            self.axs.set_xlim([1, len(self.data_analysed.row_solutions)])
            legend_marks = [self.data_analysed.t1 * 2**(i+1) for i in range(len(self.data_analysed.row_solutions[0]))]
            self.axs.legend(legend_marks, title="Периоды")
            self.figure.canvas.draw()
        else:
            self.axs.plot([i+1 for i in range(len(self.data_analysed.row_solutions))], self.data_analysed.row_solutions)
            self.axs.set_xticks([i+1 for i in range(len(self.data_analysed.row_solutions))])
            self.axs.set_xticklabels([i+1 for i in range(len(self.data_analysed.row_solutions))])
            self.axs.set_xlim([1, len(self.data_analysed.row_solutions)])
            temp_mas = np.array(self.data_analysed.row_solutions).transpose()
            p2 = self.axs.imshow(temp_mas, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
            self.cb = self.figure.colorbar(p2, ax=self.axs)
            self.figure.canvas.draw()

    # Phi visual
    def visual_phi(self, is_graph=True):
        self.canvas_update()
        if is_graph:
            self.axs.plot([i+1 for i in range(len(self.data_analysed.phi_solutions))], self.data_analysed.phi_solutions)
            self.axs.set_xticks([i+1 for i in range(len(self.data_analysed.phi_solutions))])
            self.axs.set_xticklabels([i+1 for i in range(len(self.data_analysed.phi_solutions))])
            self.axs.set_xlim([1, len(self.data_analysed.phi_solutions)])
            legend_marks = [self.data_analysed.t1 * 2**(i+1) for i in range(len(self.data_analysed.phi_solutions[0]))]
            self.axs.legend(legend_marks, title="Периоды")
            self.figure.canvas.draw()
        else:
            self.axs.plot([i+1 for i in range(len(self.data_analysed.phi_solutions))], self.data_analysed.phi_solutions)
            self.axs.set_xticks([i+1 for i in range(len(self.data_analysed.phi_solutions))])
            self.axs.set_xticklabels([i+1 for i in range(len(self.data_analysed.phi_solutions))])
            self.axs.set_xlim([1, len(self.data_analysed.phi_solutions)])
            temp_mas = np.array(self.data_analysed.phi_solutions).transpose()
            p2 = self.axs.imshow(temp_mas, cmap='jet', aspect='auto', interpolation='bilinear', origin="upper")
            self.cb = self.figure.colorbar(p2, ax=self.axs)
            self.figure.canvas.draw()

    def error_window(self):
        pass