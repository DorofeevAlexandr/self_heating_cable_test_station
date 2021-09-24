import tkinter as tk
import window_open_dialog
import control_plc as c_plc

WIDTH_1 = 15
WIDTH_2 = 25


class FrameCurrentParams(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack()

        self.family_tester_1 = tk.StringVar()
        self.label_family_tester_1 = tk.Label(self, text='Фамилия испытателя')
        self.entry_family_tester_1 = tk.Entry(self, width=WIDTH_2, textvariable=self.family_tester_1)
        self.label_family_tester_1.grid(row=1, column=0, sticky="e")
        self.entry_family_tester_1.grid(row=1, column=1)
        self.entry_family_tester_1.bind('<Return>', (
            lambda event: write_value(self.entry_family_tester_1, 's_FamilyTester_1')))
        self.entry_family_tester_1.bind('<Key>', (lambda event: set_skipp_update()))

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
        self.label_voltage_testing.grid(row=3, column=0, sticky="e")
        self.entry_voltage_testing.grid(row=3, column=1)

        self.temp_test_unit_1 = tk.StringVar()
        self.label_temp_test_unit_1 = tk.Label(self, text='Температура испытательной установки 1')
        self.entry_temp_test_unit_1 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_unit_1)
        self.label_temp_test_unit_1.grid(row=4, column=0, sticky="e")
        self.entry_temp_test_unit_1.grid(row=4, column=1)

        self.temp_test_unit_2 = tk.StringVar()
        self.label_temp_test_unit_2 = tk.Label(self, text='Температура испытательной установки 2')
        self.entry_temp_test_unit_2 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_unit_2)
        self.label_temp_test_unit_2.grid(row=4, column=3, sticky="e")
        self.entry_temp_test_unit_2.grid(row=4, column=4)

    def update_values_of_entry(self):
        self.family_tester_1.set(str(c_plc.parameters.p['s_FamilyTester_1'].value))
        self.time_read_frompc.set(str(c_plc.parameters.p['s_TimeReadFromPC'].value)[8:16])
        self.date_read_frompc.set(str(c_plc.parameters.p['s_TimeReadFromPC'].value)[0:8])
        self.voltage_testing.set(str(c_plc.parameters.p['r_VoltageTesting'].value))
        self.temp_test_unit_1.set(str(c_plc.parameters.p['r_TempTestUnit_1'].value))
        self.temp_test_unit_2.set(str(c_plc.parameters.p['r_TempTestUnit_2'].value))


class FrameCurrentParamsUnit1(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack()

        self.kable_brand_test_1 = tk.StringVar()
        self.label_kable_brand_test_1 = tk.Label(self, text='Марка кабеля испытания 1')
        self.entry_kable_brand_test_1 = tk.Entry(self, width=WIDTH_2, textvariable=self.kable_brand_test_1)
        self.label_kable_brand_test_1.grid(row=1, column=0, sticky="e")
        self.entry_kable_brand_test_1.grid(row=1, column=1)
        self.entry_kable_brand_test_1.bind('<Return>', (
            lambda event: write_value(self.entry_kable_brand_test_1, 's_KableBrandTest_1')))
        self.entry_kable_brand_test_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.batch_number_test_1 = tk.StringVar()
        self.label_batch_number_test_1 = tk.Label(self, text='Номер партии испытания 1')
        self.entry_batch_number_test_1 = tk.Entry(self, width=WIDTH_2, textvariable=self.batch_number_test_1)
        self.label_batch_number_test_1.grid(row=2, column=0, sticky="e")
        self.entry_batch_number_test_1.grid(row=2, column=1)
        self.entry_batch_number_test_1.bind('<Return>', (
            lambda event: write_value(self.entry_batch_number_test_1, 's_BatchNumberTest_1')))
        self.entry_batch_number_test_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.temp_start_test_1 = tk.StringVar()
        self.label_temp_start_test_1 = tk.Label(self, text='Температура начала испытания 1, гр. С')
        self.entry_temp_start_test_1 = tk.Entry(self, width=WIDTH_1, textvariable=self.temp_start_test_1)
        self.label_temp_start_test_1.grid(row=3, column=0, sticky="e")
        self.entry_temp_start_test_1.grid(row=3, column=1)
        self.entry_temp_start_test_1.bind('<Return>', (
            lambda event: write_value(self.entry_temp_start_test_1, 'r_TempStartTest_1')))
        self.entry_temp_start_test_1.bind('<Key>', (lambda event: set_skipp_update()))

        self.exp_time_test_1 = tk.StringVar()
        self.label_exp_time_test_1 = tk.Label(self, text='Время выдержки испытания 1, мин.')
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
        self.label_current_test_1 = tk.Label(self, text='Ток образца 1, А')
        self.entry_current_test_1 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.current_test_1)
        self.label_current_test_1.grid(row=9, column=0, sticky="e")
        self.entry_current_test_1.grid(row=9, column=1)

        self.temp_test_1 = tk.StringVar()
        self.label_temp_test_1 = tk.Label(self, text='Температура образца 1, гр С')
        self.entry_temp_test_1 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_1)
        self.label_temp_test_1.grid(row=10, column=0, sticky="e")
        self.entry_temp_test_1.grid(row=10, column=1)

    def update_values_of_entry(self):
        self.kable_brand_test_1.set(str(c_plc.parameters.p['s_KableBrandTest_1'].value))
        self.batch_number_test_1.set(str(c_plc.parameters.p['s_BatchNumberTest_1'].value))
        self.temp_start_test_1.set(str(c_plc.parameters.p['r_TempStartTest_1'].value))
        self.exp_time_test_1.set(str(c_plc.parameters.p['w_ExpTimeTest_1'].value))
        self.len_time_test_1.set(str(c_plc.parameters.p['w_LenTimeTest_1'].value))
        self.time_pusk_test_1.set(str(c_plc.parameters.p['s_TimePuskTest_1'].value))
        self.time_start_test_1.set(str(c_plc.parameters.p['s_TimeStartTest_1'].value))
        self.current_test_1.set(str(c_plc.parameters.p['r_CurrentTest_1'].value))
        self.temp_test_1.set(str(c_plc.parameters.p['r_TempTest_1'].value))


class FrameCurrentParamsUnit2(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack()

        self.kable_brand_test_2 = tk.StringVar()
        self.label_kable_brand_test_2 = tk.Label(self, text='Марка кабеля испытания 2')
        self.entry_kable_brand_test_2 = tk.Entry(self, width=WIDTH_2, textvariable=self.kable_brand_test_2)
        self.label_kable_brand_test_2.grid(row=1, column=0, sticky="e")
        self.entry_kable_brand_test_2.grid(row=1, column=1)
        self.entry_kable_brand_test_2.bind('<Return>', (
            lambda event: write_value(self.entry_kable_brand_test_2, 's_KableBrandTest_2')))
        self.entry_kable_brand_test_2.bind('<Key>', (lambda event: set_skipp_update()))

        self.batch_number_test_2 = tk.StringVar()
        self.label_batch_number_test_2 = tk.Label(self, text='Номер партии испытания 2')
        self.entry_batch_number_test_2 = tk.Entry(self, width=WIDTH_2, textvariable=self.batch_number_test_2)
        self.label_batch_number_test_2.grid(row=2, column=0, sticky="e")
        self.entry_batch_number_test_2.grid(row=2, column=1)
        self.entry_batch_number_test_2.bind('<Return>', (
            lambda event: write_value(self.entry_batch_number_test_2, 's_BatchNumberTest_2')))
        self.entry_batch_number_test_2.bind('<Key>', (lambda event: set_skipp_update()))

        self.temp_start_test_2 = tk.StringVar()
        self.label_temp_start_test_2 = tk.Label(self, text='Температура начала испытания 2, гр. С')
        self.entry_temp_start_test_2 = tk.Entry(self, width=WIDTH_1, textvariable=self.temp_start_test_2)
        self.label_temp_start_test_2.grid(row=3, column=0, sticky="e")
        self.entry_temp_start_test_2.grid(row=3, column=1)
        self.entry_temp_start_test_2.bind('<Return>', (
            lambda event: write_value(self.entry_temp_start_test_2, 'r_TempStartTest_2')))
        self.entry_temp_start_test_2.bind('<Key>', (lambda event: set_skipp_update()))

        self.exp_time_test_2 = tk.StringVar()
        self.label_exp_time_test_2 = tk.Label(self, text='Время выдержки испытания 2, мин.')
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
        self.label_current_test_2 = tk.Label(self, text='Ток образца 2, А')
        self.entry_current_test_2 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.current_test_2)
        self.label_current_test_2.grid(row=9, column=0, sticky="e")
        self.entry_current_test_2.grid(row=9, column=1)

        self.temp_test_2 = tk.StringVar()
        self.label_temp_test_2 = tk.Label(self, text='Температура образца 2, гр С')
        self.entry_temp_test_2 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_2)
        self.label_temp_test_2.grid(row=10, column=0, sticky="e")
        self.entry_temp_test_2.grid(row=10, column=1)

    def update_values_of_entry(self):
        self.kable_brand_test_2.set(str(c_plc.parameters.p['s_KableBrandTest_2'].value))
        self.batch_number_test_2.set(str(c_plc.parameters.p['s_BatchNumberTest_2'].value))
        self.temp_start_test_2.set(str(c_plc.parameters.p['r_TempStartTest_2'].value))
        self.exp_time_test_2.set(str(c_plc.parameters.p['w_ExpTimeTest_2'].value))
        self.len_time_test_2.set(str(c_plc.parameters.p['w_LenTimeTest_2'].value))
        self.time_pusk_test_2.set(str(c_plc.parameters.p['s_TimePuskTest_2'].value))
        self.time_start_test_2.set(str(c_plc.parameters.p['s_TimeStartTest_2'].value))
        self.current_test_2.set(str(c_plc.parameters.p['r_CurrentTest_2'].value))
        self.temp_test_2.set(str(c_plc.parameters.p['r_TempTest_2'].value))


class FrameCurrentParamsUnit3(tk.LabelFrame):
    def __init__(self, parent=None):
        tk.LabelFrame.__init__(self, parent)
        self.pack()

        self.kable_brand_test_3 = tk.StringVar()
        self.label_kable_brand_test_3 = tk.Label(self, text='Марка кабеля испытания 3')
        self.entry_kable_brand_test_3 = tk.Entry(self, width=WIDTH_2, textvariable=self.kable_brand_test_3)
        self.label_kable_brand_test_3.grid(row=1, column=0, sticky="e")
        self.entry_kable_brand_test_3.grid(row=1, column=1)
        self.entry_kable_brand_test_3.bind('<Return>', (
            lambda event: write_value(self.entry_kable_brand_test_3, 's_KableBrandTest_3')))
        self.entry_kable_brand_test_3.bind('<Key>', (lambda event: set_skipp_update()))

        self.batch_number_test_3 = tk.StringVar()
        self.label_batch_number_test_3 = tk.Label(self, text='Номер партии испытания 3')
        self.entry_batch_number_test_3 = tk.Entry(self, width=WIDTH_2, textvariable=self.batch_number_test_3)
        self.label_batch_number_test_3.grid(row=2, column=0, sticky="e")
        self.entry_batch_number_test_3.grid(row=2, column=1)
        self.entry_batch_number_test_3.bind('<Return>', (
            lambda event: write_value(self.entry_batch_number_test_3, 's_BatchNumberTest_3')))
        self.entry_batch_number_test_3.bind('<Key>', (lambda event: set_skipp_update()))

        self.temp_start_test_3 = tk.StringVar()
        self.label_temp_start_test_3 = tk.Label(self, text='Температура начала испытания 3, гр. С')
        self.entry_temp_start_test_3 = tk.Entry(self, width=WIDTH_1, textvariable=self.temp_start_test_3)
        self.label_temp_start_test_3.grid(row=3, column=0, sticky="e")
        self.entry_temp_start_test_3.grid(row=3, column=1)
        self.entry_temp_start_test_3.bind('<Return>', (
            lambda event: write_value(self.entry_temp_start_test_3, 'r_TempStartTest_3')))
        self.entry_temp_start_test_3.bind('<Key>', (lambda event: set_skipp_update()))

        self.exp_time_test_3 = tk.StringVar()
        self.label_exp_time_test_3 = tk.Label(self, text='Время выдержки испытания 3, мин.')
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
        self.label_current_test_3 = tk.Label(self, text='Ток образца 3, А')
        self.entry_current_test_3 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.current_test_3)
        self.label_current_test_3.grid(row=9, column=0, sticky="e")
        self.entry_current_test_3.grid(row=9, column=1)

        self.temp_test_3 = tk.StringVar()
        self.label_temp_test_3 = tk.Label(self, text='Температура образца 3, гр С')
        self.entry_temp_test_3 = tk.Entry(self, width=WIDTH_1, state='disabled', textvariable=self.temp_test_3)
        self.label_temp_test_3.grid(row=10, column=0, sticky="e")
        self.entry_temp_test_3.grid(row=10, column=1)

    def update_values_of_entry(self):
        self.kable_brand_test_3.set(str(c_plc.parameters.p['s_KableBrandTest_3'].value))
        self.batch_number_test_3.set(str(c_plc.parameters.p['s_BatchNumberTest_3'].value))
        self.temp_start_test_3.set(str(c_plc.parameters.p['r_TempStartTest_3'].value))
        self.exp_time_test_3.set(str(c_plc.parameters.p['w_ExpTimeTest_3'].value))
        self.len_time_test_3.set(str(c_plc.parameters.p['w_LenTimeTest_3'].value))
        self.time_pusk_test_3.set(str(c_plc.parameters.p['s_TimePuskTest_3'].value))
        self.time_start_test_3.set(str(c_plc.parameters.p['s_TimeStartTest_3'].value))
        self.current_test_3.set(str(c_plc.parameters.p['r_CurrentTest_3'].value))
        self.temp_test_3.set(str(c_plc.parameters.p['r_TempTest_3'].value))


# Создается новое окно с заголовком.
window = tk.Tk()
window.title("Испытание самогреющегося кабеля")

frm_params = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_params.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)

frm_cur_pars = FrameCurrentParams(frm_params)
frm_cur_pars['relief'] = tk.SUNKEN
frm_cur_pars['borderwidth'] = 3
frm_cur_pars.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)

frm_cur_pars_unit_1 = FrameCurrentParamsUnit1(frm_params)
frm_cur_pars_unit_1['relief'] = tk.SUNKEN
frm_cur_pars_unit_1['text'] = 'Образец № 1'
frm_cur_pars_unit_1['borderwidth'] = 3
frm_cur_pars_unit_1.pack(side=tk.LEFT, anchor=tk.N)

frm_cur_pars_unit_2 = FrameCurrentParamsUnit2(frm_params)
frm_cur_pars_unit_2['relief'] = tk.SUNKEN
frm_cur_pars_unit_2['text'] = 'Образец № 2'
frm_cur_pars_unit_2['borderwidth'] = 3
frm_cur_pars_unit_2.pack(side=tk.LEFT, anchor=tk.N)

frm_cur_pars_unit_3 = FrameCurrentParamsUnit3(frm_params)
frm_cur_pars_unit_3['relief'] = tk.SUNKEN
frm_cur_pars_unit_3['text'] = 'Образец № 3'
frm_cur_pars_unit_3['borderwidth'] = 3
frm_cur_pars_unit_3.pack(side=tk.LEFT, anchor=tk.N)


fr = window_open_dialog.FrameOpenFile()
fr.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.BOTH)


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

    window.after(3000, update)


def write_value(entry, key):
    c_plc.parameters.p[key].write_value = entry.get()
    c_plc.parameters.p[key].en_write = True
    global skipp_update
    skipp_update = 0


update()
window.after(3000, update)
# Запуск приложения.
window.mainloop()
