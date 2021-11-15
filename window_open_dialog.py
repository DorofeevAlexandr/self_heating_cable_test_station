import tkinter as tk
from reading_csv_file_ftp import CsvFileReader
import charts


class FrameOpenFile(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack(fill=tk.BOTH)

        self.label = tk.Label(self, text='/sd0/')
        self.label.pack(side=tk.TOP, fill=tk.Y, anchor=tk.NW)

        self.box = tk.Listbox(self, selectmode=tk.SINGLE, width=50, height=30)
        self.box.pack(side=tk.LEFT, fill=tk.Y)
        self.box.insert(tk.END, '[**]')
        self.box.bind('<Double-Button-1>', self.open_sub_folder)
        self.scroll = tk.Scrollbar(self, command=self.box.yview)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.box.config(yscrollcommand=self.scroll.set)
        # self.open_folder()

        self.frm_chart = charts.FrameShowCharts(self)
        self.frm_chart['text'] = 'График'
        self.frm_chart.pack(side=tk.LEFT, anchor=tk.SE, fill=tk.BOTH)
        # self.frm_chart.open_chart('Test_2021_11_3_15_49_37_0_qwer_asdf.csv')

    def open_folder(self, path='/sd0/'):
        for i in range(1, self.box.size()):
            self.box.delete(1)
        with CsvFileReader() as csv_reader:
            folders = csv_reader.get_dir_list(path)
            for folder in folders:
                self.box.insert(tk.END, folder)
            self.label['text'] = csv_reader.get_path()

    def open_sub_folder(self, event):
        select = list(self.box.curselection())[0]
        if select == 0 and self.label['text'].rfind('/') != -1:
            path = self.label['text'][0:self.label['text'].rfind('/')] + '/'
            if path == '/':
                path = '/sd0/'
            file_name = ''
        else:
            path = self.label['text'] + '/'
            file_name = self.box.get(select)

        with CsvFileReader() as csv_reader:
            if file_name.find('.') == -1:
                for i in range(1, self.box.size()):
                    self.box.delete(1)
                folders = csv_reader.get_dir_list(path + file_name)
                for folder in folders:
                    self.box.insert(tk.END, folder)
                self.label['text'] = csv_reader.get_path()
            else:
                csv_reader.copy_file(path, file_name)
                csv_reader.open_file(file_name)
                self.frm_chart.open_chart(file_name)
        return file_name


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Выбор архива")
    FrameOpenFile().mainloop()
