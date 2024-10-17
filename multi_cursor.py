import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import MultiCursor as _MultiCursor
import datetime as dt


class MultiCursor(_MultiCursor):
    """MultiCursor widget subclass that snaps to plot data
    Snaps to the nearest x-axis value on mouse-movement. The horizontal lines of
    the cursor then follow the y-axis values. Data for each axis is displayed
    on the bottom toolbar of the figure.
    Attributes:
        x_data (np.ndarray): The original x-axis data passed to the plot.
            Must be shared by all related subplots (using ``sharex`` parameter)
        x_label (str): Label used for x-axis display on the toolbar
        x_format_func (callable, optional): If provided, a callable to convert
            values in :attr:`x_data` to string
        y_data: List containing the y-axis data for each subplot
        y_labels: List of labels associated with :attr:`y_data`
        y_format_funcs: List of callables (or ``None``) to format values in
            :attr:`y_data` to string
    """
    def __init__(self, *args, **kwargs):
        self.x_data = kwargs.pop('x_data')
        self.x_label = kwargs.pop('x_label')
        self.y_data = kwargs.pop('y_data')
        self.y_labels = kwargs.pop('y_labels')
        self.current_data_x = None
        self.toolbar_message = None
        super().__init__(*args, **kwargs)

    def onmove(self, event):
        if self.ignore(event):
            return
        if event.inaxes is None:
            return
        if not self.canvas.widgetlock.available(self):
            return

        x0 = event.xdata
        x = dt.datetime(1970, 1, 1) + dt.timedelta(x0)
        ax = event.inaxes
        if ax not in self.axes:
            return
        fmin = self.x_data[0]
        fmax = self.x_data[len(self.x_data)-1]
        if x < fmin:
            i_x = 0
        elif x > fmax:
            i_x = len(self.x_data) - 1
        else:
            for index, t in enumerate(self.x_data):
                if np.abs(t - x) < dt.timedelta(milliseconds=250):
                    i_x = index
                    break
            # i_x = self.x_data.index(x)
            # i_x = np.abs(self.x_data - x).argmin()
        data_x = self.x_data[i_x]
        if data_x == self.current_data_x:
            msg = self.toolbar_message
            # if msg is not None:
            #     self.canvas.toolbar.set_message(msg)
            return

        x_str = str(data_x.time())
        labels = [(self.x_label, x_str)]
        self.needclear = True

        if not self.visible:
            return
        if self.vertOn:
            for line in self.vlines:
                line.set_xdata((data_x, data_x))
                line.set_visible(self.visible)
        if self.horizOn:
            for lbl, y_arr, line in zip(self.y_labels, self.y_data, self.hlines):
                if type(y_arr[0]) == list:
                    labels.append((lbl[0], str('%.1f' % y_arr[0][i_x])))
                    labels.append((lbl[1], str('%.1f' % y_arr[1][i_x])))
                    labels.append((lbl[2], str('%.1f' % y_arr[2][i_x])))
                    line.set_ydata((y_arr[0][i_x], y_arr[0][i_x]))
                else:
                    data_y = y_arr[i_x]
                    y_str = str('%.3f' % data_y)
                    labels.append((lbl, y_str))
                    line.set_ydata((data_y, data_y))
                line.set_visible(self.visible)

        self.current_data_x = data_x
        msg = ', '.join(['='.join(lbl) for lbl in labels])
        self.toolbar_message = msg
        s_time = ', ' + labels[0][0] + ' = ' + labels[0][1]
        s_current = labels[1][0] + ' = ' + labels[1][1]
        s_temper = labels[2][0] + ' = ' + labels[2][1] + ', ' +\
                   labels[3][0] + ' = ' + labels[3][1] + ', ' + \
                   labels[4][0] + ' = ' + labels[4][1]
        s_u = labels[5][0] + ' = ' + labels[5][1]
        s_power = labels[6][0] + ' = ' + labels[6][1]
        s_current_pusk = ',      I_pusk = ' + str('%.3f' % max(self.y_data[0]))

        self.axes[0].set_title(s_current + s_time + s_current_pusk)
        self.axes[1].set_title(s_temper + s_time)
        self.axes[2].set_title(s_u + s_time)
        self.axes[3].set_title(s_power + s_time)

        self.axes[0].set_ylim(0, max(self.y_data[0]) * 1.05)
        self.axes[1].set_ylim(min(min(self.y_data[1][0]), min(self.y_data[1][1]), min(self.y_data[1][2])),
                              max(max(self.y_data[1][0]), max(self.y_data[1][1]), max(self.y_data[1][2])) * 1.05)
        self.axes[2].set_ylim(0, 250)




        # self.axes[0].draw_artist(self.axes[0].)
        # self.canvas.draw()
        self._update()

if __name__ == '__main__':
    T = 2.0
    N = 256
    xdata = np.linspace(0, T, N)
    y0 = np.cos(2 * np.pi * xdata)
    y1 = np.sin(2 * np.pi * xdata)

    def format_x(value):
        return '{:.3f}'.format(value)

    def format_y(value):
        return '{:.3f}'.format(value)

    fig = plt.figure()

    ax0 = fig.add_subplot(2,1,1)
    plt.plot(xdata, y0)

    ax1 = fig.add_subplot(2,1,2, sharex=ax0)
    plt.plot(xdata, y1)

    cursor = MultiCursor(fig.canvas, (ax0, ax1),
        x_data=xdata, x_label='T', x_format_func=format_x,
        y_data=[y0, y1], y_labels=['cos', 'sin'], y_format_funcs=[format_y, format_y],
        color='r', lw=1, horizOn=True, useblit=True
    )

    plt.show()