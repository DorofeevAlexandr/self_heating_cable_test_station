from tkinter import *
from reading_csv_file_ftp import CsvFileReader


def open_folder(path='/sd0/'):
    for i in range(1, box.size()):
        box.delete(1)
    with CsvFileReader() as csv_reader:
        folders = csv_reader.get_dir_list(path)
        for folder in folders:
            box.insert(END, folder)
        label['text'] = csv_reader.get_path()


def open_sub_folder(event):
    select = list(box.curselection())[0]
    if select == 0 and label['text'].rfind('/') != -1:
        path = label['text'][0:label['text'].rfind('/')] + '/'
        if path == '/':
            path = '/sd0/'
        file_name = ''
    else:
        path = label['text'] + '/'
        file_name = box.get(select)

    with CsvFileReader() as csv_reader:
        if file_name.find('.') == -1:
            for i in range(1, box.size()):
                box.delete(1)
            folders = csv_reader.get_dir_list(path + file_name)
            for folder in folders:
                box.insert(END, folder)
            label['text'] = csv_reader.get_path()
        else:
            csv_reader.copy_file(path, file_name)
            csv_reader.open_file(file_name)


window = Tk()
window.title("Выбор архива")


label = Label(text='/sd0/')
label.pack(side=TOP, fill=Y, anchor=NW)

f_open_dialog = Frame()
f_open_dialog.pack(side=LEFT, anchor=NW, fill=BOTH)

box = Listbox(f_open_dialog, selectmode=SINGLE, width=100, height=30)
box.pack(side=LEFT, fill=BOTH)
box.insert(END, '[**]')
box.bind('<Double-Button-1>', open_sub_folder)
scroll = Scrollbar(f_open_dialog, command=box.yview)
scroll.pack(side=LEFT, fill=Y)
box.config(yscrollcommand=scroll.set)

open_folder()

window.mainloop()
