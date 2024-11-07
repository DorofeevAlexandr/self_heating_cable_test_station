import tkinter as tk
import control_plc as c_plc


def get_bit(num, pos):
    return (num >> pos) & 1


class WindowAlarmsList(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('400x500')

        self.label = tk.Label(self, text='Список аварий')
        self.label.pack(side=tk.TOP, fill=tk.Y, anchor=tk.N)

        self.box = tk.Listbox(self, selectmode=tk.SINGLE, width=350, height=30)
        self.box.pack(side=tk.LEFT, fill=tk.BOTH)
        self.box.insert(tk.END, '[**]')
        self.scroll = tk.Scrollbar(self, command=self.box.yview)
        self.scroll.pack(side=tk.LEFT, fill=tk.Y)
        self.box.config(yscrollcommand=self.scroll.set)
        self.clk_timer()

    def update_list_alarms_in_box(self):
        self.clear_box(self.box)
        w_alarm_1 = c_plc.parameters.p['w_RegAlarm_1'].value
        if get_bit(w_alarm_1, 0):
            self.box.insert(tk.END, '# 1: Нет питания ЛАТРа')
        if get_bit(w_alarm_1, 1):
            self.box.insert(tk.END, '# 2: Нет питания цепей управления контакторов')
        if get_bit(w_alarm_1, 2):
            self.box.insert(tk.END, ' # 3: Сработало тепловое реле КК1 контактора испытания образца 1')
        if get_bit(w_alarm_1, 3):
            self.box.insert(tk.END, '# 4: Сработало тепловое реле КК2 контактора испытания образца 2')
        if get_bit(w_alarm_1, 4):
            self.box.insert(tk.END, '# 5: Сработало тепловое реле КК3 контактора испытания образца 3')
        if get_bit(w_alarm_1, 5):
            self.box.insert(tk.END, '# 6: Авария контактора КМ1 испытания образца 1')
        if get_bit(w_alarm_1, 6):
            self.box.insert(tk.END, '# 7: Авария контактора КМ2 испытания образца 2')
        if get_bit(w_alarm_1, 7):
            self.box.insert(tk.END, '# 8: Авария контактора КМ3 испытания образца 3')
        if get_bit(w_alarm_1, 8):
            self.box.insert(tk.END, '# 9: Обрыв цепи измерения тока образца 1')
        if get_bit(w_alarm_1, 9):
            self.box.insert(tk.END, '# 10: Обрыв цепи измерения тока образца 2')
        if get_bit(w_alarm_1, 10):
            self.box.insert(tk.END, '# 11: Обрыв цепи измерения тока образца 3')
        if get_bit(w_alarm_1, 11):
            self.box.insert(tk.END, '# 12: Обрыв цепи измерения напряжения ЛАТРа')
        if get_bit(w_alarm_1, 12):
            self.box.insert(tk.END, '# 13: Обрыв связи с модулем МВ210')
        if get_bit(w_alarm_1, 13):
            self.box.insert(tk.END, '# 14: Низкое напряжение батареи МВ210')

        w_alarm_2 = c_plc.parameters.p['w_RegAlarm_2'].value
        if get_bit(w_alarm_2, 0):
            self.box.insert(tk.END, '# 15: Обрыв цепи измерения температуры образца 1')
        if get_bit(w_alarm_2, 1):
            self.box.insert(tk.END, ' # 16: Обрыв цепи измерения температуры образца 2')
        if get_bit(w_alarm_2, 2):
            self.box.insert(tk.END, '# 17: Обрыв цепи измерения температуры образца 3')
        if get_bit(w_alarm_2, 3):
            self.box.insert(tk.END, '# 18: Обрыв цепи измерения температуры стенда 1')
        if get_bit(w_alarm_2, 4):
            self.box.insert(tk.END, '# 19: Обрыв цепи измерения температуры стенда 2')
        if get_bit(w_alarm_2, 5):
            self.box.insert(tk.END, '# 20: Нет тока через образец 1')
        if get_bit(w_alarm_2, 6):
            self.box.insert(tk.END, '# 21: Нет тока через образец 2')
        if get_bit(w_alarm_2, 7):
            self.box.insert(tk.END, '# 22: Нет тока через образец 3')

    def clear_box(self, box):
        for _ in range(0, self.box.size()):
            box.delete(0)

    def clk_timer(self):
        self.update_list_alarms_in_box()
        self.after(2500, self.clk_timer)        


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Выбор архива")
    WindowAlarmsList(window).mainloop()
