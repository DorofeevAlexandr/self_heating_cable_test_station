import numpy as np
import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.widgets import MultiCursor as _MultiCursor

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
        self.x_format_func = kwargs.pop('x_format_func', None)
        self.y_data = kwargs.pop('y_data')
        self.y_labels = kwargs.pop('y_labels')
        self.y_format_funcs = kwargs.pop('y_format_funcs', None)
        if self.y_format_funcs is None:
            self.y_format_funcs = [None] * len(self.y_data)
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

        x = event.xdata
        ax = event.inaxes
        if ax not in self.axes:
            return
        fmin = self.x_data.min()
        fmax = self.x_data.max()
        if x < fmin:
            i_x = 0
        elif x > fmax:
            i_x = self.x_data.size - 1
        else:
            i_x = np.abs(self.x_data - x).argmin()
        data_x = self.x_data[i_x]
        if data_x == self.current_data_x:
            msg = self.toolbar_message
            if msg is not None:
                self.canvas.toolbar.set_message(msg)
            return

        if self.x_format_func is not None:
            x_str = self.x_format_func(data_x)
        else:
            x_str = str(data_x)
        labels = [(self.x_label, x_str)]
        self.needclear = True
        if not self.visible:
            return
        if self.vertOn:
            for line in self.vlines:
                line.set_xdata((data_x, data_x))
                line.set_visible(self.visible)
        if self.horizOn:
            for lbl, y_arr, line, fmt_func in zip(self.y_labels, self.y_data, self.hlines, self.y_format_funcs):
                data_y = y_arr[i_x]
                if fmt_func is not None:
                    y_str = fmt_func(data_y)
                else:
                    y_str = str(data_y)
                labels.append((lbl, y_str))
                line.set_ydata((data_y, data_y))
                line.set_visible(self.visible)
        self.current_data_x = data_x
        self._update()
        msg = ', '.join(['='.join(lbl) for lbl in labels])
        self.toolbar_message = msg
        self.canvas.toolbar.set_message(msg)

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
        color='r', lw=1, horizOn=True,
    )

    plt.show()