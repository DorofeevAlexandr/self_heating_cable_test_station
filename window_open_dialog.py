from report import create_report_word
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from reading_csv_file_ftp import CsvFileReader
import charts
import os
from config import BASE_DIR

from additional_information_files import open_additional_information


class FrameOpenFile(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack(fill=tk.BOTH)

        self.label = tk.Label(self, text='Выбор источника загрузки')
        self.label.pack(side=tk.TOP, fill=tk.Y, anchor=tk.NW)

        self.box = tk.Listbox(self, selectmode=tk.SINGLE, width=50, height=30)
        self.box.pack(side=tk.LEFT, fill=tk.Y)
        self.box.insert(tk.END, '[**]')
        self.box.insert(tk.END, '[PLC]')
        self.box.insert(tk.END, '[data_base]')
        self.box.bind('<Double-Button-1>', self.open_sub_folder)
        self.scroll = tk.Scrollbar(self, command=self.box.yview)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.box.config(yscrollcommand=self.scroll.set)
        # self.open_folder()

        self.button_create_report = tk.Button(self, text="Сформировать отчет", command=lambda: self.create_report())
        # self.button_create_report.config(font=("Times", "12", "bold"))
        # self.button_create_report.place(x=10, y=20)
        self.button_create_report.pack(side=tk.TOP, fill=tk.X)

        self.frm_chart = charts.FrameShowCharts(self)
        self.frm_chart['text'] = 'График'
        self.frm_chart.pack(side=tk.LEFT, anchor=tk.SE, fill=tk.BOTH)
        # self.frm_chart.open_chart('Sample1_2021_11_16__16_16_51_kab_nomer.csv')

        self.download_source = ''
        self.select_folder = ''
        self.sample = {}

    def create_report(self):
        filename = asksaveasfilename(title="Save File",
                                     initialdir=BASE_DIR,
                                     initialfile='Отчет ' + self.sample.get("s_TimePuskTest", ""),
                                     defaultextension="",
                                     filetypes=[('word', '.docx')])

        print(filename)
        create_report_word(self.frm_chart.figure_1,
                           data=self.sample,
                           report_filename=filename)

    def open_folder(self, path='/sd0/'):
        for i in range(1, self.box.size()):
            self.box.delete(1)
        with CsvFileReader() as csv_reader:
            folders = csv_reader.get_dir_list(path)
            for folder in folders:
                self.box.insert(tk.END, folder)
            self.label['text'] = csv_reader.get_path()

    def open_sub_folder_plc(self):
        select = list(self.box.curselection())[0]
        if select == 0 and self.box.get(select) == '[**]' and self.label['text'] == '/sd0':
            self.init_select_download_source()
            return None
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
                self.sample = {}
                csv_reader.copy_file(path, file_name)
                csv_reader.open_file(file_name)
                self.frm_chart.open_chart(file_name)
        return file_name

    def open_sub_folder(self, event):
        select = list(self.box.curselection())[0]
        if self.download_source == '':
            if self.box.get(select) == '[data_base]':
                self.download_source = 'PC'
                self.update_list_dir_in_box(f_name='data_base')
            if self.box.get(select) == '[PLC]':
                self.download_source = 'PLC'
                self.label['text'] = ''
                self.clear_box(self.box)
                self.open_folder('/sd0/')
        elif self.download_source == 'PLC':
            self.open_sub_folder_plc()
        elif self.download_source == 'PC':
            self.open_sub_folder_pc()

    def update_list_dir_in_box(self, f_name=''):
        self.clear_box(self.box)
        path = os.path.join(BASE_DIR, self.select_folder, f_name)
        folders = os.listdir(path)
        for f in folders:
            self.box.insert(tk.END, f)
        self.select_folder = os.path.relpath(path, start=BASE_DIR)
        self.label['text'] = self.select_folder

    def init_select_download_source(self):
        self.clear_box(self.box)
        self.download_source = ''
        self.box.insert(tk.END, '[PLC]')
        self.box.insert(tk.END, '[data_base]')
        self.label['text'] = 'Выбор источника загрузки'

    def clear_box(self, box):
        for _ in range(1, self.box.size()):
            box.delete(1)

    def open_sub_folder_pc(self):
        select = list(self.box.curselection())[0]
        if select == 0 and self.box.get(select) == '[**]':
            self.select_folder = os.path.split(self.select_folder)[0]
            if self.select_folder == '':
                self.init_select_download_source()
            else:
                self.update_list_dir_in_box(f_name='')
        elif (select != 0 and self.box.get(select).find('.csv') == -1 and
                self.box.get(select).find('.json') == -1):
            self.update_list_dir_in_box(f_name=self.box.get(select))
        elif select != 0 and (self.box.get(select).find('.csv') != -1 or
                              self.box.get(select).find('.json') != -1):
            file_name = self.box.get(select)
            path = os.path.join(BASE_DIR, self.select_folder, file_name)
            self.open_arhives(path)

    def open_arhives(self, path):
        self.sample = {}
        if os.path.splitext(path)[1] == '.csv':
            self.frm_chart.open_chart(path)
        elif os.path.splitext(path)[1] == '.json':
            self.sample = open_additional_information(path)
            try:
                file_name = self.sample['s_csv_file_name']
                print(file_name)
                pc_path = os.path.split(path)[0]
                print(pc_path)
                fn = file_name.split('_')
                print(fn)
                ftp_path = f'/sd0/{fn[1]}/{fn[2]}/'
                print(ftp_path)
                with CsvFileReader() as csv_reader:
                    csv_reader.copy_file(ftp_path=ftp_path,
                                         file_name=file_name,
                                         pc_path=pc_path)
                    csv_reader.open_file(os.path.join(pc_path, file_name))
                    self.frm_chart.open_chart(os.path.join(pc_path, file_name))
            except Exception as e:
                print(e)


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Выбор архива")
    FrameOpenFile().mainloop()
