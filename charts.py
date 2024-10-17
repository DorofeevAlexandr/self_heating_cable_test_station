import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import datetime as dt
import csv

import multi_cursor


class FrameShowCharts(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent, width=3000, height=100)
        self.pack(fill=tk.BOTH)
        self.figure_1 = plt.Figure(figsize=(1, 1), facecolor='white')
        self.ax = []
        self.ax.append(self.figure_1.add_subplot(4, 1, 1))
        self.ax.append(self.figure_1.add_subplot(4, 1, 2, sharex=self.ax[0]))
        self.ax.append(self.figure_1.add_subplot(4, 1, 3, sharex=self.ax[0]))
        self.ax.append(self.figure_1.add_subplot(4, 1, 4, sharex=self.ax[0]))

        self.figure_1.autofmt_xdate()

        self.canvas = FigureCanvasTkAgg(self.figure_1, self)
        self.canvas.get_tk_widget().place(x=-125, y=0, width=1800, height=1050)

        self.dates = []
        self.values_1 = []
        self.values_2 = []
        self.values_3 = []
        self.values_4 = []
        self.values_5 = []
        self.values_power = []

    def clear_chart(self):
        self.dates.clear()
        self.values_1.clear()
        self.values_2.clear()
        self.values_3.clear()
        self.values_4.clear()
        self.values_5.clear()
        self.values_power.clear()

        self.ax[0].clear()
        self.ax[1].clear()
        self.ax[2].clear()
        self.ax[3].clear()

    def open_chart(self, file_name, title):
        self.figure_1.suptitle(title)
        self.clear_chart()
        with open(file_name, newline='') as f:
            for row in csv.reader(f, delimiter=';', quotechar='"'):
                # print(row)
                try:
                    self.dates.append(dt.datetime.strptime("{}".format('2000 ' + row[0]), '%Y %H:%M:%S:%f'))
                    self.values_1.append(float(row[1]))
                    self.values_2.append(float(row[2]))
                    self.values_3.append(float(row[3]))
                    self.values_4.append(float(row[4]))
                    self.values_5.append(float(row[5]))
                    self.values_power.append(float(row[1]) * float(row[5]))
                except ValueError:
                    print('Прочитано некоректное значение', )

        self.figure_1.autofmt_xdate()

        self.ax[0].plot(self.dates, self.values_1, label='Ток образца  кабеля', linestyle='solid', marker='o', markersize=3, color='green')
        self.ax[0].set_ylabel('Ток образца кабеля, А')
        self.ax[0].set_title('Ток образца кабеля, А')
        self.ax[0].grid()

        self.ax[1].plot(self.dates, self.values_2, label='Т образца кабеля', linestyle='solid', marker='o', markersize=3, color='red')
        self.ax[1].plot(self.dates, self.values_3, label='T трубы на входе', linestyle='solid', marker='o', markersize=3, color='black')
        self.ax[1].plot(self.dates, self.values_4, label='Т трубы на выходе', linestyle='solid', marker='o', markersize=3, color='orange')
        self.ax[1].legend(loc='upper left')
        self.ax[1].set_ylabel('Температура, °С')
        self.ax[1].grid()

        self.ax[2].plot(self.dates, self.values_5, label='U', linestyle='solid', marker='o',
                        markersize=3, color='black')
        self.ax[2].set_ylabel('Напряжение, В')
        self.ax[2].grid()

        self.ax[3].plot(self.dates, self.values_power, label='P', linestyle='solid', marker='o',
                        markersize=3, color='blue')
        self.ax[3].set_ylabel('Мощность, Вт')
        self.ax[3].grid()

        self.canvas.draw()

        self.cursor = multi_cursor.MultiCursor(self.figure_1.canvas,
                                               (self.ax[0], self.ax[1], self.ax[2],  self.ax[3]),
                                               x_data=self.dates, x_label='T',
                                               y_data=[self.values_1,
                                                       [self.values_2, self.values_3, self.values_4],
                                                       self.values_5,
                                                       self.values_power],
                                               y_labels=['I', ['t', 't_in', 't_out'], 'U', 'P'],
                                               color='r', lw=1, horizOn=True, useblit=False
                                               )
