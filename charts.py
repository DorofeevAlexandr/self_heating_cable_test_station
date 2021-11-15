import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.dates as mdates
import datetime as dt
import csv


class FrameShowCharts(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent, width=3000, height=100)
        self.pack(fill=tk.BOTH)

        self.label = tk.Label(self, text='kjhjhjgghfhfgdfgdfgdfgdfdfgdfgdrfkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk'
                                         'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkghjghjh'
                                         'ghffffffffffffjhuygggggggggggggggggggggggggggggggggggggggggggggggggggggggggg'
                                         'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
        self.label.pack(side=tk.TOP, fill=tk.Y, anchor=tk.NW)

        self.figure_1 = plt.Figure(figsize=(1, 1), facecolor='white')
        # self.figure_1.tight_layout()
        self.ax = [self.figure_1.add_subplot(3, 1, x + 1) for x in range(3)]


        # ax = plt.axes()
        '''ax.yaxis.grid(True)
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        ax.xaxis.set_major_locator(mdates.AutoDateLocator())'''

        self.figure_1.autofmt_xdate()
        # plt.legend(loc='upper left', frameon=False)

        self.canvas = FigureCanvasTkAgg(self.figure_1, self)
        self.canvas.get_tk_widget().place(x=-125, y=0, width=1800, height=1050)

    def open_chart(self, file_name):
        self.figure_1.suptitle(file_name)
        dates = []
        values_1 = []
        values_2 = []
        values_3 = []
        values_4 = []
        values_5 = []

        with open(file_name, newline='') as f:
            for row in csv.reader(f, delimiter=';', quotechar='"'):
                print(row)
                try:
                    dates.append(dt.datetime.strptime("{}".format(row[0]), '%H:%M:%S:%f'))
                    values_1.append(float(row[1]))
                    values_2.append(float(row[2]))
                    values_3.append(float(row[3]))
                    values_4.append(float(row[4]))
                    values_5.append(float(row[5]))
                except ValueError:
                    print('Прочитано некоректное значение', )
        self.ax[0].clear()
        self.ax[1].clear()
        self.ax[2].clear()
        self.figure_1.autofmt_xdate()

        self.ax[0].plot(dates, values_1, label='Ток образца', linestyle='solid', marker='o', markersize=3, color='green')
        # self.ax[0].legend(loc='upper left')
        self.ax[0].set_ylabel('Ток образца, А')
        # self.ax[0].set_xlabel('Время')
        self.ax[0].grid()

        self.ax[1].plot(dates, values_2, label='Т образца', linestyle='solid', marker='o', markersize=3, color='red')
        self.ax[1].plot(dates, values_3, label='T установки 1', linestyle='solid', marker='o', markersize=3, color='black')
        self.ax[1].plot(dates, values_4, label='Т установки 2', linestyle='solid', marker='o', markersize=3, color='orange')
        self.ax[1].legend(loc='upper left')
        self.ax[1].set_ylabel('Температура, °С')
        # self.ax[1].set_xlabel('Время')
        self.ax[1].grid()

        self.ax[2].plot(dates, values_5, label='U', linestyle='solid', marker='o', markersize=3, color='black')
        # self.ax[2].set_title('Параметры цикла')
        # self.ax[2].legend(loc='upper left')
        self.ax[2].set_ylabel('Напряжение, В')
        # self.ax[2].set_xlabel('Время')
        self.ax[2].grid()

        self.canvas.draw()
        # plt.show()

