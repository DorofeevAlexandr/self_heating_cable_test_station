import tkinter as tk
import tkinter.messagebox as mb
import window_open_dialog
import control_plc as c_plc
from tkinter import ttk
import datetime as dt
import os

from additional_information_files import save_additional_information

WIDTH_1 = 15
WIDTH_2 = 25


def set_kth_bit(num, pos):
    return (1 << pos) | num


def get_bit(num, pos):
    return (num >> pos) & 1


class MainMenu(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)

        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        file_menu = tk.Menu(menubar, tearoff=0)
        # self.file_menu.add_command(label="Открыть...")
        # self.file_menu.add_command(label="Новый")
        file_menu.add_command(label="Настроить время в ПЛК", command=self.open_window_tuning_time_in_plc)
        # file_menu.add_separator()
        # file_menu.add_command(label="Выход", command=self.exit_program)
        menubar.add_cascade(label="Файл", menu=file_menu)

    @staticmethod
    def open_window_tuning_time_in_plc():
        WindowTuningTimeInPLC(window)
        WindowTuningTimeInPLC.grab_set(window)

    @staticmethod
    def exit_program():
        exit()


class WindowTuningTimeInPLC(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('500x150')
        self.time_read_frompc = tk.StringVar()
        self.label_time_read_frompc = tk.Label(self, text='Время в ПЛК')
        self.entry_time_read_frompc = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.time_read_frompc)
        self.label_time_read_frompc.grid(row=1, column=1, sticky="e")
        self.entry_time_read_frompc.grid(row=2, column=2)

        self.date_read_frompc = tk.StringVar()
        self.entry_date_read_frompc = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.date_read_frompc)
        self.entry_date_read_frompc.grid(row=2, column=1)

        width_time = 5
        self.year = tk.StringVar()
        self.entry_year = tk.Entry(self, width=width_time, textvariable=self.year)
        self.entry_year.grid(row=3, column=1)

        self.month = tk.StringVar()
        self.entry_month = tk.Entry(self, width=width_time, textvariable=self.month)
        self.entry_month.grid(row=3, column=2)

        self.day = tk.StringVar()
        self.entry_day = tk.Entry(self, width=width_time, textvariable=self.day)
        self.entry_day.grid(row=3, column=3)

        self.hour = tk.StringVar()
        self.entry_hour = tk.Entry(self, width=width_time, textvariable=self.hour)
        self.entry_hour.grid(row=3, column=4)

        self.minute = tk.StringVar()
        self.entry_minute = tk.Entry(self, width=width_time, textvariable=self.minute)
        self.entry_minute.grid(row=3, column=5)

        self.second = tk.StringVar()
        self.entry_second = tk.Entry(self, width=width_time, textvariable=self.second)
        self.entry_second.grid(row=3, column=6)

        self.update_values_of_entry()
        self.button_read_time = tk.Button(self, text="Обновить время", command=self.update_values_of_entry)
        self.button_write_time = tk.Button(self, text="Записать время", command=self.write_time)
        self.button_close = tk.Button(self, text="Закрыть", command=self.close_window)
        self.button_read_time.grid(row=5, column=1)
        self.button_write_time.grid(row=5, column=3)
        self.button_close.grid(row=5, column=5)

    def update_values_of_entry(self):
        s_time = str(c_plc.parameters.p['s_TimeReadFromPC'].value)
        self.time_read_frompc.set(s_time[8:16])
        self.date_read_frompc.set('20' + s_time[0:8])
        self.year.set('20' + s_time[0:2])
        self.month.set(s_time[3:5])
        self.day.set(s_time[6:8])
        self.hour.set(s_time[8:10])
        self.minute.set(s_time[11:13])
        self.second.set(s_time[14:16])

    def write_time(self):
        message = "Подтвердите операцию"
        if mb.askyesno(message=message, parent=self):
            write_value(self.entry_year, 'w_TimeWriteToPC_year')
            write_value(self.entry_month, 'w_TimeWriteToPC_month')
            write_value(self.entry_day, 'w_TimeWriteToPC_day')
            write_value(self.entry_hour, 'w_TimeWriteToPC_hour')
            write_value(self.entry_minute, 'w_TimeWriteToPC_min')
            write_value(self.entry_second, 'w_TimeWriteToPC_sec')

            w_reg_control_1 = c_plc.parameters.p['w_RegControl_1'].value
            c_plc.parameters.p['w_RegControl_1'].write_value = set_kth_bit(w_reg_control_1, 1)
            c_plc.parameters.p['w_RegControl_1'].en_write = True

    def close_window(self):
        message = "Вы уверены, что хотите закрыть это окно?"
        if mb.askyesno(message=message, parent=self):
            self.destroy()


class FrameCurrentParams(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack()

        self.family_tester_1 = tk.StringVar()
        self.label_family_tester_1 = tk.Label(self, text='Фамилия испытателя')
        self.entry_family_tester_1 = tk.Entry(self, width=WIDTH_2, textvariable=self.family_tester_1)
        self.label_family_tester_1.grid(row=1, column=0, sticky="e")
        self.entry_family_tester_1.grid(row=1, column=1)
        # self.entry_family_tester_1.bind('<Return>', (
        #     lambda event: write_value(self.entry_family_tester_1, 's_FamilyTester_1')))
        # self.entry_family_tester_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.time_read_frompc = tk.StringVar()
        self.label_time_read_frompc = tk.Label(self, text='Время в ПЛК')
        self.entry_time_read_frompc = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.time_read_frompc)
        self.label_time_read_frompc.grid(row=1, column=3, sticky="e")
        self.entry_time_read_frompc.grid(row=2, column=4)

        self.date_read_frompc = tk.StringVar()
        self.entry_date_read_frompc = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.date_read_frompc)
        self.entry_date_read_frompc.grid(row=1, column=4)

        self.voltage_testing = tk.StringVar()
        self.label_voltage_testing = tk.Label(self, text='Напряжение тестирования')
        self.entry_voltage_testing = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.voltage_testing)
        self.label_voltage_testing.grid(row=2, column=0, sticky="e")
        self.entry_voltage_testing.grid(row=2, column=1)

        self.temp_test_unit_1 = tk.StringVar()
        self.label_temp_test_unit_1 = tk.Label(self, text='Температура трубы на входе')
        self.entry_temp_test_unit_1 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_unit_1)
        self.label_temp_test_unit_1.grid(row=3, column=0, sticky="e")
        self.entry_temp_test_unit_1.grid(row=3, column=1)

        self.temp_test_unit_2 = tk.StringVar()
        self.label_temp_test_unit_2 = tk.Label(self, text='Температура трубы на выходе')
        self.entry_temp_test_unit_2 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_unit_2)
        self.label_temp_test_unit_2.grid(row=4, column=0, sticky="e")
        self.entry_temp_test_unit_2.grid(row=4, column=1)

        self.button_ack = tk.Button(self, text="Сбросить аварию", command=self.ack_alarms)
        self.button_ack.grid(row=4, column=4)

    def ack_alarms(self):
        w_reg_control_1 = c_plc.parameters.p['w_RegControl_1'].value
        c_plc.parameters.p['w_RegControl_1'].write_value = set_kth_bit(w_reg_control_1, 15)
        c_plc.parameters.p['w_RegControl_1'].en_write = True

    def update_values_of_entry(self):
        # self.family_tester_1.set(str(c_plc.parameters.p['s_FamilyTester_1'].value))
        self.time_read_frompc.set(str(c_plc.parameters.p['s_TimeReadFromPC'].value)[8:16])
        self.date_read_frompc.set(str(c_plc.parameters.p['s_TimeReadFromPC'].value)[0:8])
        self.voltage_testing.set(str('%.1f' % c_plc.parameters.p['r_VoltageTesting'].value))
        self.temp_test_unit_1.set(str('%.1f' % c_plc.parameters.p['r_TempTestUnit_1'].value))
        self.temp_test_unit_2.set(str('%.1f' % c_plc.parameters.p['r_TempTestUnit_2'].value))


class FrameCurrentParamsUnit1(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack()

        self.kable_brand_test_1 = tk.StringVar()
        self.label_kable_brand_test_1 = tk.Label(self, text='Марка кабеля испытания 1')
        self.entry_kable_brand_test_1 = tk.Entry(self, width=WIDTH_2, textvariable=self.kable_brand_test_1)
        self.label_kable_brand_test_1.grid(row=1, column=0, sticky="e")
        self.entry_kable_brand_test_1.grid(row=1, column=1)
        # self.entry_kable_brand_test_1.bind('<Return>', (
        #     lambda event: write_value(self.entry_kable_brand_test_1, 's_KableBrandTest_1')))
        # self.entry_kable_brand_test_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.batch_number_test_1 = tk.StringVar()
        self.label_batch_number_test_1 = tk.Label(self, text='Номер партии испытания 1')
        self.entry_batch_number_test_1 = tk.Entry(self, width=WIDTH_2, textvariable=self.batch_number_test_1)
        self.label_batch_number_test_1.grid(row=2, column=0, sticky="e")
        self.entry_batch_number_test_1.grid(row=2, column=1)
        # self.entry_batch_number_test_1.bind('<Return>', (
        #     lambda event: write_value(self.entry_batch_number_test_1, 's_BatchNumberTest_1')))
        # self.entry_batch_number_test_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.temp_start_test_1 = tk.StringVar()
        self.label_temp_start_test_1 = tk.Label(self, text='Температура начала испытания 1, гр. С')
        self.entry_temp_start_test_1 = tk.Entry(self, width=WIDTH_1, textvariable=self.temp_start_test_1)
        self.label_temp_start_test_1.grid(row=3, column=0, sticky="e")
        self.entry_temp_start_test_1.grid(row=3, column=1)
        self.entry_temp_start_test_1.bind('<Return>', (
            lambda event: write_value(self.entry_temp_start_test_1, 'r_TempStartTest_1')))
        self.entry_temp_start_test_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.exp_time_test_1 = tk.StringVar()
        self.label_exp_time_test_1 = tk.Label(self, text='Время выдержки испытания 1, c.')
        self.entry_exp_time_test_1 = tk.Entry(self, width=WIDTH_1, textvariable=self.exp_time_test_1)
        self.label_exp_time_test_1.grid(row=4, column=0, sticky="e")
        self.entry_exp_time_test_1.grid(row=4, column=1)
        self.entry_exp_time_test_1.bind('<Return>', (
            lambda event: write_value(self.entry_exp_time_test_1, 'w_ExpTimeTest_1')))
        self.entry_exp_time_test_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.len_time_test_1 = tk.StringVar()
        self.label_len_time_test_1 = tk.Label(self, text='Время длительности испытания 1, сек.')
        self.entry_len_time_test_1 = tk.Entry(self, width=WIDTH_1, textvariable=self.len_time_test_1)
        self.label_len_time_test_1.grid(row=5, column=0, sticky="e")
        self.entry_len_time_test_1.grid(row=5, column=1)
        self.entry_len_time_test_1.bind('<Return>', (
            lambda event: write_value(self.entry_len_time_test_1, 'w_LenTimeTest_1')))
        self.entry_len_time_test_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.time_pusk_test_1 = tk.StringVar()
        self.label_time_pusk_test_1 = tk.Label(self, text='Время пуска испытания 1')
        self.entry_time_pusk_test_1 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.time_pusk_test_1)
        self.label_time_pusk_test_1.grid(row=6, column=0, sticky="e")
        self.entry_time_pusk_test_1.grid(row=6, column=1)

        self.time_start_test_1 = tk.StringVar()
        self.label_time_start_test_1 = tk.Label(self, text='Время начала испытания 1')
        self.entry_time_start_test_1 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.time_start_test_1)
        self.label_time_start_test_1.grid(row=7, column=0, sticky="e")
        self.entry_time_start_test_1.grid(row=7, column=1)

        self.current_test_1 = tk.StringVar()
        self.label_current_test_1 = tk.Label(self, text='Ток образца кабеля 1, А')
        self.entry_current_test_1 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.current_test_1)
        self.label_current_test_1.grid(row=9, column=0, sticky="e")
        self.entry_current_test_1.grid(row=9, column=1)

        self.temp_test_1 = tk.StringVar()
        self.label_temp_test_1 = tk.Label(self, text='Температура образца кабеля 1, гр С')
        self.entry_temp_test_1 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_1)
        self.label_temp_test_1.grid(row=10, column=0, sticky="e")
        self.entry_temp_test_1.grid(row=10, column=1)

    def update_values_of_entry(self):
        # self.kable_brand_test_1.set(str(c_plc.parameters.p['s_KableBrandTest_1'].value))
        # self.batch_number_test_1.set(str(c_plc.parameters.p['s_BatchNumberTest_1'].value))
        self.temp_start_test_1.set(str('%.1f' % c_plc.parameters.p['r_TempStartTest_1'].value))
        self.exp_time_test_1.set(str(c_plc.parameters.p['w_ExpTimeTest_1'].value))
        self.len_time_test_1.set(str(c_plc.parameters.p['w_LenTimeTest_1'].value))
        self.time_pusk_test_1.set(str(c_plc.parameters.p['s_TimePuskTest_1'].value))
        self.time_start_test_1.set(str(c_plc.parameters.p['s_TimeStartTest_1'].value))
        self.current_test_1.set(str('%.3f' % c_plc.parameters.p['r_CurrentTest_1'].value))
        self.temp_test_1.set(str('%.1f' % c_plc.parameters.p['r_TempTest_1'].value))


class FrameCurrentParamsUnit2(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack()

        self.kable_brand_test_2 = tk.StringVar()
        self.label_kable_brand_test_2 = tk.Label(self, text='Марка кабеля испытания 2')
        self.entry_kable_brand_test_2 = tk.Entry(self, width=WIDTH_2, textvariable=self.kable_brand_test_2)
        self.label_kable_brand_test_2.grid(row=1, column=0, sticky="e")
        self.entry_kable_brand_test_2.grid(row=1, column=1)
        # self.entry_kable_brand_test_2.bind('<Return>', (
        #     lambda event: write_value(self.entry_kable_brand_test_2, 's_KableBrandTest_2')))
        # self.entry_kable_brand_test_2.bind('<Key>', (lambda event: set_skipp_update()))

        self.batch_number_test_2 = tk.StringVar()
        self.label_batch_number_test_2 = tk.Label(self, text='Номер партии испытания 2')
        self.entry_batch_number_test_2 = tk.Entry(self, width=WIDTH_2, textvariable=self.batch_number_test_2)
        self.label_batch_number_test_2.grid(row=2, column=0, sticky="e")
        self.entry_batch_number_test_2.grid(row=2, column=1)
        # self.entry_batch_number_test_2.bind('<Return>', (
        #     lambda event: write_value(self.entry_batch_number_test_2, 's_BatchNumberTest_2')))
        # self.entry_batch_number_test_2.bind('<Key>', (lambda event: set_skipp_update()))

        self.temp_start_test_2 = tk.StringVar()
        self.label_temp_start_test_2 = tk.Label(self, text='Температура начала испытания 2, гр. С')
        self.entry_temp_start_test_2 = tk.Entry(self, width=WIDTH_1, textvariable=self.temp_start_test_2)
        self.label_temp_start_test_2.grid(row=3, column=0, sticky="e")
        self.entry_temp_start_test_2.grid(row=3, column=1)
        self.entry_temp_start_test_2.bind('<Return>', (
            lambda event: write_value(self.entry_temp_start_test_2, 'r_TempStartTest_2')))
        self.entry_temp_start_test_2.bind('<Key>', (lambda event: set_skipp_update()))

        self.exp_time_test_2 = tk.StringVar()
        self.label_exp_time_test_2 = tk.Label(self, text='Время выдержки испытания 2, c.')
        self.entry_exp_time_test_2 = tk.Entry(self, width=WIDTH_1, textvariable=self.exp_time_test_2)
        self.label_exp_time_test_2.grid(row=4, column=0, sticky="e")
        self.entry_exp_time_test_2.grid(row=4, column=1)
        self.entry_exp_time_test_2.bind('<Return>', (
            lambda event: write_value(self.entry_exp_time_test_2, 'w_ExpTimeTest_2')))
        self.entry_exp_time_test_2.bind('<Key>', (lambda event: set_skipp_update()))

        self.len_time_test_2 = tk.StringVar()
        self.label_len_time_test_2 = tk.Label(self, text='Время длительности испытания 2, сек.')
        self.entry_len_time_test_2 = tk.Entry(self, width=WIDTH_1, textvariable=self.len_time_test_2)
        self.label_len_time_test_2.grid(row=5, column=0, sticky="e")
        self.entry_len_time_test_2.grid(row=5, column=1)
        self.entry_len_time_test_2.bind('<Return>', (
            lambda event: write_value(self.entry_len_time_test_2, 'w_LenTimeTest_2')))
        self.entry_len_time_test_2.bind('<Key>', (lambda event: set_skipp_update()))

        self.time_pusk_test_2 = tk.StringVar()
        self.label_time_pusk_test_2 = tk.Label(self, text='Время пуска испытания 2')
        self.entry_time_pusk_test_2 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.time_pusk_test_2)
        self.label_time_pusk_test_2.grid(row=6, column=0, sticky="e")
        self.entry_time_pusk_test_2.grid(row=6, column=1)

        self.time_start_test_2 = tk.StringVar()
        self.label_time_start_test_2 = tk.Label(self, text='Время начала испытания 2')
        self.entry_time_start_test_2 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.time_start_test_2)
        self.label_time_start_test_2.grid(row=7, column=0, sticky="e")
        self.entry_time_start_test_2.grid(row=7, column=1)

        self.current_test_2 = tk.StringVar()
        self.label_current_test_2 = tk.Label(self, text='Ток образца кабеля 2, А')
        self.entry_current_test_2 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.current_test_2)
        self.label_current_test_2.grid(row=9, column=0, sticky="e")
        self.entry_current_test_2.grid(row=9, column=1)

        self.temp_test_2 = tk.StringVar()
        self.label_temp_test_2 = tk.Label(self, text='Температура образца кабеля 2, гр С')
        self.entry_temp_test_2 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_2)
        self.label_temp_test_2.grid(row=10, column=0, sticky="e")
        self.entry_temp_test_2.grid(row=10, column=1)

    def update_values_of_entry(self):
        # self.kable_brand_test_2.set(str(c_plc.parameters.p['s_KableBrandTest_2'].value))
        # self.batch_number_test_2.set(str(c_plc.parameters.p['s_BatchNumberTest_2'].value))
        self.temp_start_test_2.set(str('%.1f' % c_plc.parameters.p['r_TempStartTest_2'].value))
        self.exp_time_test_2.set(str(c_plc.parameters.p['w_ExpTimeTest_2'].value))
        self.len_time_test_2.set(str(c_plc.parameters.p['w_LenTimeTest_2'].value))
        self.time_pusk_test_2.set(str(c_plc.parameters.p['s_TimePuskTest_2'].value))
        self.time_start_test_2.set(str(c_plc.parameters.p['s_TimeStartTest_2'].value))
        self.current_test_2.set(str('%.3f' % c_plc.parameters.p['r_CurrentTest_2'].value))
        self.temp_test_2.set(str('%.1f' % c_plc.parameters.p['r_TempTest_2'].value))


class FrameCurrentParamsUnit3(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack()

        self.kable_brand_test_3 = tk.StringVar()
        self.label_kable_brand_test_3 = tk.Label(self, text='Марка кабеля испытания 3')
        self.entry_kable_brand_test_3 = tk.Entry(self, width=WIDTH_2, textvariable=self.kable_brand_test_3)
        self.label_kable_brand_test_3.grid(row=1, column=0, sticky="e")
        self.entry_kable_brand_test_3.grid(row=1, column=1)
        # self.entry_kable_brand_test_3.bind('<Return>', (
        #     lambda event: write_value(self.entry_kable_brand_test_3, 's_KableBrandTest_3')))
        # self.entry_kable_brand_test_3.bind('<Key>', (lambda event: set_skipp_update()))

        self.batch_number_test_3 = tk.StringVar()
        self.label_batch_number_test_3 = tk.Label(self, text='Номер партии испытания 3')
        self.entry_batch_number_test_3 = tk.Entry(self, width=WIDTH_2, textvariable=self.batch_number_test_3)
        self.label_batch_number_test_3.grid(row=2, column=0, sticky="e")
        self.entry_batch_number_test_3.grid(row=2, column=1)
        # self.entry_batch_number_test_3.bind('<Return>', (
        #     lambda event: write_value(self.entry_batch_number_test_3, 's_BatchNumberTest_3')))
        # self.entry_batch_number_test_3.bind('<Key>', (lambda event: set_skipp_update()))

        self.temp_start_test_3 = tk.StringVar()
        self.label_temp_start_test_3 = tk.Label(self, text='Температура начала испытания 3, гр. С')
        self.entry_temp_start_test_3 = tk.Entry(self, width=WIDTH_1, textvariable=self.temp_start_test_3)
        self.label_temp_start_test_3.grid(row=3, column=0, sticky="e")
        self.entry_temp_start_test_3.grid(row=3, column=1)
        self.entry_temp_start_test_3.bind('<Return>', (
            lambda event: write_value(self.entry_temp_start_test_3, 'r_TempStartTest_3')))
        self.entry_temp_start_test_3.bind('<Key>', (lambda event: set_skipp_update()))

        self.exp_time_test_3 = tk.StringVar()
        self.label_exp_time_test_3 = tk.Label(self, text='Время выдержки испытания 3, c.')
        self.entry_exp_time_test_3 = tk.Entry(self, width=WIDTH_1, textvariable=self.exp_time_test_3)
        self.label_exp_time_test_3.grid(row=4, column=0, sticky="e")
        self.entry_exp_time_test_3.grid(row=4, column=1)
        self.entry_exp_time_test_3.bind('<Return>', (
            lambda event: write_value(self.entry_exp_time_test_3, 'w_ExpTimeTest_3')))
        self.entry_exp_time_test_3.bind('<Key>', (lambda event: set_skipp_update()))

        self.len_time_test_3 = tk.StringVar()
        self.label_len_time_test_3 = tk.Label(self, text='Время длительности испытания 3, сек.')
        self.entry_len_time_test_3 = tk.Entry(self, width=WIDTH_1, textvariable=self.len_time_test_3)
        self.label_len_time_test_3.grid(row=5, column=0, sticky="e")
        self.entry_len_time_test_3.grid(row=5, column=1)
        self.entry_len_time_test_3.bind('<Return>', (
            lambda event: write_value(self.entry_len_time_test_3, 'w_LenTimeTest_3')))
        self.entry_len_time_test_3.bind('<Key>', (lambda event: set_skipp_update()))

        self.time_pusk_test_3 = tk.StringVar()
        self.label_time_pusk_test_3 = tk.Label(self, text='Время пуска испытания 3')
        self.entry_time_pusk_test_3 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.time_pusk_test_3)
        self.label_time_pusk_test_3.grid(row=6, column=0, sticky="e")
        self.entry_time_pusk_test_3.grid(row=6, column=1)

        self.time_start_test_3 = tk.StringVar()
        self.label_time_start_test_3 = tk.Label(self, text='Время начала испытания 3')
        self.entry_time_start_test_3 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.time_start_test_3)
        self.label_time_start_test_3.grid(row=7, column=0, sticky="e")
        self.entry_time_start_test_3.grid(row=7, column=1)

        self.current_test_3 = tk.StringVar()
        self.label_current_test_3 = tk.Label(self, text='Ток образца кабеля 3, А')
        self.entry_current_test_3 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.current_test_3)
        self.label_current_test_3.grid(row=9, column=0, sticky="e")
        self.entry_current_test_3.grid(row=9, column=1)

        self.temp_test_3 = tk.StringVar()
        self.label_temp_test_3 = tk.Label(self, text='Температура образца кабеля 3, гр С')
        self.entry_temp_test_3 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_3)
        self.label_temp_test_3.grid(row=10, column=0, sticky="e")
        self.entry_temp_test_3.grid(row=10, column=1)

    def update_values_of_entry(self):
        # self.kable_brand_test_3.set(str(c_plc.parameters.p['s_KableBrandTest_3'].value))
        # self.batch_number_test_3.set(str(c_plc.parameters.p['s_BatchNumberTest_3'].value))
        self.temp_start_test_3.set(str('%.1f' % c_plc.parameters.p['r_TempStartTest_3'].value))
        self.exp_time_test_3.set(str(c_plc.parameters.p['w_ExpTimeTest_3'].value))
        self.len_time_test_3.set(str(c_plc.parameters.p['w_LenTimeTest_3'].value))
        self.time_pusk_test_3.set(str(c_plc.parameters.p['s_TimePuskTest_3'].value))
        self.time_start_test_3.set(str(c_plc.parameters.p['s_TimeStartTest_3'].value))
        self.current_test_3.set(str('%.3f' % c_plc.parameters.p['r_CurrentTest_3'].value))
        self.temp_test_3.set(str('%.1f' % c_plc.parameters.p['r_TempTest_3'].value))


class FrameTechnologicalScheme(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack(expand=1)

        canvas = tk.Canvas(self)
        x0, y0 = 30, 100
        tube_width, tube_height = 1200, 450
        zone_width = tube_width // 3
        # Рисуем трубу
        canvas.create_rectangle(x0, y0, x0 + tube_width, y0 + tube_height, width=3)
        # Рисуем отводы к трубе
        canvas.create_line(x0 // 4, y0 + tube_height // 2, x0, y0 + tube_height // 2, width=3)
        canvas.create_line(x0 + tube_width, y0 + tube_height // 2, x0 + tube_width + x0 * 3 // 4, y0 + tube_height // 2, width=3)
        # Рисуем разделители зон
        canvas.create_line(x0 + zone_width, y0, x0 + zone_width, y0 + tube_height, dash=(4, 2))
        canvas.create_line(x0 + 2 * zone_width, y0, x0 + 2 * zone_width, y0 + tube_height, dash=(4, 2))
        canvas.pack(fill=tk.BOTH, expand=1)

        self.label_voltage_testing = tk.Label(self, text='Напряжение тестирования')
        self.label_voltage_testing_val = tk.Label(self, text='Напряжение')
        self.label_voltage_testing_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_voltage_testing.place(x=5, y=0)
        self.label_voltage_testing_val.place(x=5, y=20)

        self.label_temp_test_unit_1 = tk.Label(self, text='Температура трубы на входе')
        self.label_temp_test_unit_1_val = tk.Label(self, text='Температура установки 1')
        self.label_temp_test_unit_1_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_temp_test_unit_1.place(x=x0, y=y0+tube_height+10)
        self.label_temp_test_unit_1_val.place(x=x0, y=y0+tube_height+30)

        self.label_temp_test_unit_2 = tk.Label(self, text='Температура трубы на выходе')
        self.label_temp_test_unit_2_val = tk.Label(self, text='Температура установки 2')
        self.label_temp_test_unit_2_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_temp_test_unit_2.place(x=x0+tube_width-200, y=y0+tube_height+10)
        self.label_temp_test_unit_2_val.place(x=x0+tube_width-200, y=y0+tube_height+30)

        x0_zone1, y0_zone1 = x0 + zone_width // 10, y0 + 5
        # zone 1
        self.label_current_test_1 = tk.Label(self, text='Ток образца кабеля 1, А')
        self.label_current_test_1_val = tk.Label(self, text='Ток образца кабеля 1, А')
        self.label_current_test_1_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_current_test_1.place(x=x0_zone1, y=y0_zone1)
        self.label_current_test_1_val.place(x=x0_zone1, y=y0_zone1+20)

        self.label_power_test_1 = tk.Label(self, text='Мощность образца кабеля 1, Вт')
        self.label_power_test_1_val = tk.Label(self, text='Мощность образца кабеля 1, Вт')
        self.label_power_test_1_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_power_test_1.place(x=x0_zone1, y=y0_zone1+90)
        self.label_power_test_1_val.place(x=x0_zone1, y=y0_zone1+110)

        self.label_temp_test_1 = tk.Label(self, text='Температура образца кабеля 1, гр С')
        self.label_temp_test_1_val = tk.Label(self, text='Температура образца кабеля 1, гр С')
        self.label_temp_test_1_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_temp_test_1.place(x=x0_zone1, y=y0_zone1+190)
        self.label_temp_test_1_val.place(x=x0_zone1, y=y0_zone1+210)

        self.label_status_test_1 = tk.Label(self, text='Статус 1')
        self.label_status_test_1.config(font=("Times", "40", "bold"), bg="White")
        self.label_status_test_1.place(x=x0_zone1, y=y0_zone1+300)

        self.button_start_test_1 = tk.Button(self, text="Пуск", command=lambda: self.pusk_measurement(1, 4))
        self.button_start_test_1.config(font=("Times", "20", "bold"), bg="Green")
        self.button_start_test_1.place(x=x0_zone1, y=y0_zone1 + 380)
        self.button_stop_test_1 = tk.Button(self, text="Стоп", command=lambda: self.set_bit_control_word(5))
        self.button_stop_test_1.config(font=("Times", "20", "bold"), bg="Red")
        self.button_stop_test_1.place(x=x0_zone1+zone_width//3, y=y0_zone1+380)

        # zone 2
        self.label_current_test_2 = tk.Label(self, text='Ток образца кабеля 2 А')
        self.label_current_test_2_val = tk.Label(self, text='Ток образца кабеля 2, А')
        self.label_current_test_2_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_current_test_2.place(x=x0_zone1+zone_width, y=y0_zone1)
        self.label_current_test_2_val.place(x=x0_zone1+zone_width, y=y0_zone1+20)

        self.label_power_test_2 = tk.Label(self, text='Мощность образца кабеля 2, Вт')
        self.label_power_test_2_val = tk.Label(self, text='Мощность образца кабеля 2, Вт')
        self.label_power_test_2_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_power_test_2.place(x=x0_zone1+zone_width, y=y0_zone1+90)
        self.label_power_test_2_val.place(x=x0_zone1+zone_width, y=y0_zone1+110)

        self.label_temp_test_2 = tk.Label(self, text='Температура образца кабеля 2, гр С')
        self.label_temp_test_2_val = tk.Label(self, text='Температура образца кабеля 2, гр С')
        self.label_temp_test_2_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_temp_test_2.place(x=x0_zone1+zone_width, y=y0_zone1+190)
        self.label_temp_test_2_val.place(x=x0_zone1+zone_width, y=y0_zone1+210)

        self.label_status_test_2 = tk.Label(self, text='Статус 2')
        self.label_status_test_2.config(font=("Times", "40", "bold"), bg="White")
        self.label_status_test_2.place(x=x0_zone1+zone_width, y=y0_zone1 + 300)

        self.button_start_test_2 = tk.Button(self, text="Пуск", command=lambda: self.pusk_measurement(2, 7))
        self.button_start_test_2.config(font=("Times", "20", "bold"), bg="Green")
        self.button_start_test_2.place(x=x0_zone1+zone_width, y=y0_zone1 + 380)
        self.button_stop_test_2 = tk.Button(self, text="Стоп", command=lambda: self.set_bit_control_word(8))
        self.button_stop_test_2.config(font=("Times", "20", "bold"), bg="Red")
        self.button_stop_test_2.place(x=x0_zone1+zone_width//3+zone_width, y=y0_zone1+380)

        # zone 3
        self.label_current_test_3 = tk.Label(self, text='Ток образца кабеля 3, А')
        self.label_current_test_3_val = tk.Label(self, text='Ток образца кабеля 3, А')
        self.label_current_test_3_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_current_test_3.place(x=x0_zone1+2*zone_width, y=y0_zone1)
        self.label_current_test_3_val.place(x=x0_zone1+2*zone_width, y=y0_zone1+20)

        self.label_power_test_3 = tk.Label(self, text='Мощность образца кабеля 3, Вт')
        self.label_power_test_3_val = tk.Label(self, text='Мощность образца кабеля 3, Вт')
        self.label_power_test_3_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_power_test_3.place(x=x0_zone1+2*zone_width, y=y0_zone1+90)
        self.label_power_test_3_val.place(x=x0_zone1+2*zone_width, y=y0_zone1+110)

        self.label_temp_test_3 = tk.Label(self, text='Температура образца кабеля 3, гр С')
        self.label_temp_test_3_val = tk.Label(self, text='Температура образца кабеля 3, гр С')
        self.label_temp_test_3_val.config(font=("Times", "40", "bold"), bg="Black", fg='Red')
        self.label_temp_test_3.place(x=x0_zone1+2*zone_width, y=y0_zone1+190)
        self.label_temp_test_3_val.place(x=x0_zone1+2*zone_width, y=y0_zone1+210)

        self.label_status_test_3 = tk.Label(self, text='Статус 3')
        self.label_status_test_3.config(font=("Times", "40", "bold"), bg="White")
        self.label_status_test_3.place(x=x0_zone1+2*zone_width, y=y0_zone1 + 300)

        self.button_start_test_3 = tk.Button(self, text="Пуск", command=lambda: self.pusk_measurement(3, 10))
        self.button_start_test_3.config(font=("Times", "20", "bold"), bg="Green")
        self.button_start_test_3.place(x=x0_zone1+2*zone_width, y=y0_zone1 + 380)
        self.button_stop_test_3 = tk.Button(self, text="Стоп", command=lambda: self.set_bit_control_word(11))
        self.button_stop_test_3.config(font=("Times", "20", "bold"), bg="Red")
        self.button_stop_test_3.place(x=x0_zone1+zone_width//3+2*zone_width, y=y0_zone1+380)

    def pusk_measurement(self, zone_num: int, bit_num: int):
        if self.set_bit_control_word(bit_num):
            saving_parameters_at_start(sample_num=zone_num)

    def set_bit_control_word(self, pos):
        message = "Подтвердите операцию"
        if mb.askyesno(message=message, parent=self):
            w_reg_control_1 = c_plc.parameters.p['w_RegControl_1'].value
            c_plc.parameters.p['w_RegControl_1'].write_value = set_kth_bit(w_reg_control_1, pos)
            c_plc.parameters.p['w_RegControl_1'].en_write = True
            return True

    def update_values(self):
        self.label_voltage_testing_val['text'] = str('%.1f' % c_plc.parameters.p['r_VoltageTesting'].value) + ' V'
        self.label_temp_test_unit_1_val['text'] = str('%.2f' % c_plc.parameters.p['r_TempTestUnit_1'].value) + ' °C'
        self.label_temp_test_unit_2_val['text'] = str('%.2f' % c_plc.parameters.p['r_TempTestUnit_2'].value) + ' °C'

        self.label_current_test_1_val['text'] = str('%.3f' % c_plc.parameters.p['r_CurrentTest_1'].value) + ' A'
        self.label_temp_test_1_val['text'] = str('%.2f' % c_plc.parameters.p['r_TempTest_1'].value) + ' °C'

        self.label_current_test_2_val['text'] = str('%.3f' % c_plc.parameters.p['r_CurrentTest_2'].value) + ' A'
        self.label_temp_test_2_val['text'] = str('%.2f' % c_plc.parameters.p['r_TempTest_2'].value) + ' °C'

        self.label_current_test_3_val['text'] = str('%.3f' % c_plc.parameters.p['r_CurrentTest_3'].value) + ' A'
        self.label_temp_test_3_val['text'] = str('%.2f' % c_plc.parameters.p['r_TempTest_3'].value) + ' °C'

        power_1 = float(c_plc.parameters.p['r_VoltageTesting'].value) * float(
            c_plc.parameters.p['r_CurrentTest_1'].value)
        power_2 = float(c_plc.parameters.p['r_VoltageTesting'].value) * float(
            c_plc.parameters.p['r_CurrentTest_2'].value)
        power_3 = float(c_plc.parameters.p['r_VoltageTesting'].value) * float(
            c_plc.parameters.p['r_CurrentTest_3'].value)

        self.label_power_test_1_val['text'] = str('%.1f' % power_1) + ' Вт'
        self.label_power_test_2_val['text'] = str('%.1f' % power_2) + ' Вт'
        self.label_power_test_3_val['text'] = str('%.1f' % power_3) + ' Вт'

        self.control_status(self.label_status_test_1, c_plc.parameters.p['w_RegStatus_1'].value, 0, 1, 2,
                            revers_time=c_plc.parameters.p['w_revers_time_1'].value)
        self.control_status(self.label_status_test_2, c_plc.parameters.p['w_RegStatus_1'].value, 3, 4, 5,
                            revers_time=c_plc.parameters.p['w_revers_time_2'].value)
        self.control_status(self.label_status_test_3, c_plc.parameters.p['w_RegStatus_1'].value, 6, 7, 8,
                            revers_time=c_plc.parameters.p['w_revers_time_3'].value)

        '''st_start = str(c_plc.parameters.p['s_TimeStartTest_3'].value)[8, -1]
        try:
            t_start = dt.datetime.strptime("{}".format(st_start), '%H:%M:%S')
        except TypeError:
            t_start = 0
        '''

    def control_status(self, label, status_word, pos_1, pos_2, pos_3, revers_time: int):
        if get_bit(status_word, pos_1):
            label['text'] = 'Выдержка - ' + str(revers_time) + 'с'
            label.config(bg="Yellow")
        elif get_bit(status_word, pos_2):
            label['text'] = 'Испытание - ' + str(revers_time) + 'с'
            label.config(bg="Green")
        elif get_bit(status_word, pos_3):
            label['text'] = 'Завершено'
            label.config(bg="Red")
        else:
            label['text'] = ''
            label.config(bg="White")


def saving_parameters_at_start(sample_num: int):
    additional_information = {'w_sample_num': sample_num,
                              's_FamilyTester': frm_cur_pars.entry_family_tester_1.get()
                              }
    if sample_num == 1:
        additional_information['s_KableBrandTest'] = frm_cur_pars_unit_1.entry_kable_brand_test_1.get()
        additional_information['s_BatchNumberTest'] = frm_cur_pars_unit_1.entry_batch_number_test_1.get()
        additional_information['r_TempStartTest'] = frm_cur_pars_unit_1.entry_temp_start_test_1.get()
        additional_information['w_ExpTimeTest'] = frm_cur_pars_unit_1.entry_exp_time_test_1.get()
        additional_information['w_LenTimeTest'] = frm_cur_pars_unit_1.entry_len_time_test_1.get()
    elif sample_num == 2:
        additional_information['s_KableBrandTest'] = frm_cur_pars_unit_2.entry_kable_brand_test_2.get()
        additional_information['s_BatchNumberTest'] = frm_cur_pars_unit_2.entry_batch_number_test_2.get()
        additional_information['r_TempStartTest'] = frm_cur_pars_unit_2.entry_temp_start_test_2.get()
        additional_information['w_ExpTimeTest'] = frm_cur_pars_unit_2.entry_exp_time_test_2.get()
        additional_information['w_LenTimeTest'] = frm_cur_pars_unit_2.entry_len_time_test_2.get()
    elif sample_num == 3:
        additional_information['s_KableBrandTest'] = frm_cur_pars_unit_3.entry_kable_brand_test_3.get()
        additional_information['s_BatchNumberTest'] = frm_cur_pars_unit_3.entry_batch_number_test_3.get()
        additional_information['r_TempStartTest'] = frm_cur_pars_unit_3.entry_temp_start_test_3.get()
        additional_information['w_ExpTimeTest'] = frm_cur_pars_unit_3.entry_exp_time_test_3.get()
        additional_information['w_LenTimeTest'] = frm_cur_pars_unit_3.entry_len_time_test_3.get()
    csv_filename = save_additional_information(sample=additional_information)
    write_csv_filename(sample_num, csv_filename)


def write_csv_filename(sample_num, filename):
    csv_filename = os.path.splitext(filename)[0]
    if sample_num == 1:
        write_parametr(key='s_FileNameTest_1', value=csv_filename[0:16])
        write_parametr(key='s_FileNameTestEnd_1', value=csv_filename[16:])
        print(csv_filename)
        print(c_plc.parameters.p['s_FileNameTest_1'].value)
        print(c_plc.parameters.p['s_FileNameTestEnd_1'].value)
    elif sample_num == 2:
        write_parametr(key='s_FileNameTest_2', value=csv_filename[0:16])
        write_parametr(key='s_FileNameTestEnd_2', value=csv_filename[16:])
    elif sample_num == 3:
        write_parametr(key='s_FileNameTest_3', value=csv_filename[0:16])
        write_parametr(key='s_FileNameTestEnd_3', value=csv_filename[16:])


# Создается новое окно с заголовком.
window = tk.Tk()
#window.attributes('-fullscreen', True)
# window.attributes('-topmost', True)

window.title("Испытание саморегулирующегося нагревательного кабеля")

main_menu = MainMenu(window)

note = ttk.Notebook(window)

frm_params = tk.Frame(note, relief=tk.SUNKEN, borderwidth=3)
frm_params.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)
note.add(frm_params, text="Стенд")
frm_archives = ttk.Frame(note)
note.add(frm_archives, text="Архив")
note.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.BOTH)

frm_cur_pars = FrameCurrentParams(frm_params)
frm_cur_pars['relief'] = tk.SUNKEN
frm_cur_pars['borderwidth'] = 1
frm_cur_pars.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)

frm_cur_pars_units = tk.Frame(frm_params, relief=tk.SUNKEN, borderwidth=1)
frm_cur_pars_units.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)

frm_cur_pars_unit_1 = FrameCurrentParamsUnit1(frm_cur_pars_units)
frm_cur_pars_unit_1['relief'] = tk.SUNKEN
frm_cur_pars_unit_1['text'] = 'Образец № 1'
frm_cur_pars_unit_1['borderwidth'] = 3
frm_cur_pars_unit_1.pack(side=tk.LEFT, anchor=tk.N)

frm_cur_pars_unit_2 = FrameCurrentParamsUnit2(frm_cur_pars_units)
frm_cur_pars_unit_2['relief'] = tk.SUNKEN
frm_cur_pars_unit_2['text'] = 'Образец № 2'
frm_cur_pars_unit_2['borderwidth'] = 3
frm_cur_pars_unit_2.pack(side=tk.LEFT, anchor=tk.N)

frm_cur_pars_unit_3 = FrameCurrentParamsUnit3(frm_cur_pars_units)
frm_cur_pars_unit_3['relief'] = tk.SUNKEN
frm_cur_pars_unit_3['text'] = 'Образец № 3'
frm_cur_pars_unit_3['borderwidth'] = 3
frm_cur_pars_unit_3.pack(side=tk.LEFT, anchor=tk.N)

frm_technolgical_scheme = FrameTechnologicalScheme(frm_params)
frm_technolgical_scheme.pack(side=tk.BOTTOM, anchor=tk.SW, fill=tk.BOTH)

frm_window_open_dialog = window_open_dialog.FrameOpenFile(frm_archives)
frm_window_open_dialog.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.BOTH)
# =================================================================================================

skipp_update = 0


def set_skipp_update():
    global skipp_update
    skipp_update = 5


def update():
    c_plc.update_parameters()

    global skipp_update
    if skipp_update > 0:
        skipp_update -= 1
    else:
        # Обновляем значение полей ввода вывода
        frm_cur_pars.update_values_of_entry()
        frm_cur_pars_unit_1.update_values_of_entry()
        frm_cur_pars_unit_2.update_values_of_entry()
        frm_cur_pars_unit_3.update_values_of_entry()
        frm_technolgical_scheme.update_values()

    window.after(1000, update)


def write_value(entry, key):
    c_plc.parameters.p[key].write_value = entry.get()
    c_plc.parameters.p[key].en_write = True
    global skipp_update
    skipp_update = 0


def write_parametr(key, value):
    c_plc.parameters.p[key].write_value = value
    c_plc.parameters.p[key].en_write = True

update()
window.after(3000, update)
# Запуск приложения.
window.mainloop()
