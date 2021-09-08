import tkinter as tk
import window_open_dialog
# import control_plc as cplc


WIDTH_1 = 15
WIDTH_2 = 25
# Создается новое окно с заголовком.
window = tk.Tk()
window.title("Испытание самогреющегося кабеля")

frm_params = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_params.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)

frm_current_params = tk.Frame(frm_params, relief=tk.SUNKEN, borderwidth=3)
frm_current_params.pack(side=tk.TOP, anchor=tk.N, fill=tk.X)

frm_current_params_unit_1 = tk.LabelFrame(frm_params, text='Образец № 1', relief=tk.SUNKEN, borderwidth=3)
frm_current_params_unit_1.pack(side=tk.LEFT, anchor=tk.N)

frm_current_params_unit_2 = tk.LabelFrame(frm_params, text='Образец № 2', relief=tk.SUNKEN, borderwidth=3)
frm_current_params_unit_2.pack(side=tk.LEFT, anchor=tk.N)

frm_current_params_unit_3 = tk.LabelFrame(frm_params, text='Образец № 3', relief=tk.SUNKEN, borderwidth=3)
frm_current_params_unit_3.pack(side=tk.LEFT, anchor=tk.N)

fr = window_open_dialog.FrameOpenFile()
fr.pack(side=tk.LEFT, anchor=tk.NW, fill=tk.BOTH)


label_family_tester_1 = tk.Label(master=frm_current_params, text='Фамилия испытателя')
entry_family_tester_1 = tk.Entry(master=frm_current_params, width=WIDTH_2)
label_family_tester_1.grid(row=1, column=0, sticky="e")
entry_family_tester_1.grid(row=1, column=1)

label_time_read_frompc = tk.Label(master=frm_current_params, text='Время в ПЛК')
entry_time_read_frompc = tk.Entry(master=frm_current_params, width=WIDTH_1, state='disabled')
label_time_read_frompc.grid(row=1, column=3, sticky="e")
entry_time_read_frompc.grid(row=1, column=4)

label_voltage_testing = tk.Label(master=frm_current_params, text='Напряжение тестирования')
entry_voltage_testing = tk.Entry(master=frm_current_params, width=WIDTH_1, state='disabled')
label_voltage_testing.grid(row=3, column=0, sticky="e")
entry_voltage_testing.grid(row=3, column=1)

label_temp_test_unit_1 = tk.Label(master=frm_current_params, text='Температура испытательной установки 1')
entry_temp_test_unit_1 = tk.Entry(master=frm_current_params, width=WIDTH_1, state='disabled')
label_temp_test_unit_1.grid(row=4, column=0, sticky="e")
entry_temp_test_unit_1.grid(row=4, column=1)

label_temp_test_unit_2 = tk.Label(master=frm_current_params, text='Температура испытательной установки 2')
entry_temp_test_unit_2 = tk.Entry(master=frm_current_params, width=WIDTH_1, state='disabled')
label_temp_test_unit_2.grid(row=4, column=3, sticky="e")
entry_temp_test_unit_2.grid(row=4, column=4)


# ==========================================================================================================
label_kable_brand_test_1 = tk.Label(master=frm_current_params_unit_1, text='Марка кабеля испытания 1')
entry_kable_brand_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_2)
label_kable_brand_test_1.grid(row=1, column=0, sticky="e")
entry_kable_brand_test_1.grid(row=1, column=1)

label_batch_number_test_1 = tk.Label(master=frm_current_params_unit_1, text='Номер партии испытания 1')
entry_batch_number_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_2)
label_batch_number_test_1.grid(row=2, column=0, sticky="e")
entry_batch_number_test_1.grid(row=2, column=1)

label_temp_start_test_1 = tk.Label(master=frm_current_params_unit_1, text='Температура начала испытания 1, гр. С')
entry_temp_start_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_1)
label_temp_start_test_1.grid(row=3, column=0, sticky="e")
entry_temp_start_test_1.grid(row=3, column=1)

label_exp_time_test_1 = tk.Label(master=frm_current_params_unit_1, text='Время выдержки испытания 1, мин.')
entry_exp_time_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_1)
label_exp_time_test_1.grid(row=4, column=0, sticky="e")
entry_exp_time_test_1.grid(row=4, column=1)

label_len_time_test_1 = tk.Label(master=frm_current_params_unit_1, text='Время длительности испытания 1, сек.')
entry_len_time_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_1)
label_len_time_test_1.grid(row=5, column=0, sticky="e")
entry_len_time_test_1.grid(row=5, column=1)

label_time_pusk_test_1 = tk.Label(master=frm_current_params_unit_1, text='Время пуска испытания 1')
entry_time_pusk_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_1, state='disabled')
label_time_pusk_test_1.grid(row=6, column=0, sticky="e")
entry_time_pusk_test_1.grid(row=6, column=1)

label_time_start_test_1 = tk.Label(master=frm_current_params_unit_1, text='Время начала испытания 1')
entry_time_start_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_1, state='disabled')
label_time_start_test_1.grid(row=7, column=0, sticky="e")
entry_time_start_test_1.grid(row=7, column=1)

label_current_test_1 = tk.Label(master=frm_current_params_unit_1, text='Ток образца 1, А')
entry_current_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_1, state='disabled')
label_current_test_1.grid(row=9, column=0, sticky="e")
entry_current_test_1.grid(row=9, column=1)

label_temp_test_1 = tk.Label(master=frm_current_params_unit_1, text='Температура образца 1, гр С')
entry_temp_test_1 = tk.Entry(master=frm_current_params_unit_1, width=WIDTH_1, state='disabled')
label_temp_test_1.grid(row=10, column=0, sticky="e")
entry_temp_test_1.grid(row=10, column=1)

# =================================================================================================
label_kable_brand_test_2 = tk.Label(master=frm_current_params_unit_2, text='Марка кабеля испытания 2')
entry_kable_brand_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_2)
label_kable_brand_test_2.grid(row=1, column=0, sticky="e")
entry_kable_brand_test_2.grid(row=1, column=1)

label_batch_number_test_2 = tk.Label(master=frm_current_params_unit_2, text='Номер партии испытания 2')
entry_batch_number_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_2)
label_batch_number_test_2.grid(row=2, column=0, sticky="e")
entry_batch_number_test_2.grid(row=2, column=1)

label_temp_start_test_2 = tk.Label(master=frm_current_params_unit_2, text='Температура начала испытания 2, гр. С')
entry_temp_start_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_1)
label_temp_start_test_2.grid(row=3, column=0, sticky="e")
entry_temp_start_test_2.grid(row=3, column=1)

label_exp_time_test_2 = tk.Label(master=frm_current_params_unit_2, text='Время выдержки испытания 2, мин.')
entry_exp_time_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_1)
label_exp_time_test_2.grid(row=4, column=0, sticky="e")
entry_exp_time_test_2.grid(row=4, column=1)

label_len_time_test_2 = tk.Label(master=frm_current_params_unit_2, text='Время длительности испытания 2, сек.')
entry_len_time_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_1)
label_len_time_test_2.grid(row=5, column=0, sticky="e")
entry_len_time_test_2.grid(row=5, column=1)

label_time_pusk_test_2 = tk.Label(master=frm_current_params_unit_2, text='Время пуска испытания 2')
entry_time_pusk_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_1, state='disabled')
label_time_pusk_test_2.grid(row=6, column=0, sticky="e")
entry_time_pusk_test_2.grid(row=6, column=1)

label_time_start_test_2 = tk.Label(master=frm_current_params_unit_2, text='Время начала испытания 2')
entry_time_start_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_1, state='disabled')
label_time_start_test_2.grid(row=7, column=0, sticky="e")
entry_time_start_test_2.grid(row=7, column=1)

label_current_test_2 = tk.Label(master=frm_current_params_unit_2, text='Ток образца 2, А')
entry_current_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_1, state='disabled')
label_current_test_2.grid(row=9, column=0, sticky="e")
entry_current_test_2.grid(row=9, column=1)

label_temp_test_2 = tk.Label(master=frm_current_params_unit_2, text='Температура образца 2, гр С')
entry_temp_test_2 = tk.Entry(master=frm_current_params_unit_2, width=WIDTH_1, state='disabled')
label_temp_test_2.grid(row=10, column=0, sticky="e")
entry_temp_test_2.grid(row=10, column=1)


# ==========================================================================================================
label_kable_brand_test_3 = tk.Label(master=frm_current_params_unit_3, text='Марка кабеля испытания 3')
entry_kable_brand_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_2)
label_kable_brand_test_3.grid(row=1, column=0, sticky="e")
entry_kable_brand_test_3.grid(row=1, column=1)

label_batch_number_test_3 = tk.Label(master=frm_current_params_unit_3, text='Номер партии испытания 3')
entry_batch_number_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_2)
label_batch_number_test_3.grid(row=2, column=0, sticky="e")
entry_batch_number_test_3.grid(row=2, column=1)

label_temp_start_test_3 = tk.Label(master=frm_current_params_unit_3, text='Температура начала испытания 3, гр. С')
entry_temp_start_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_1)
label_temp_start_test_3.grid(row=3, column=0, sticky="e")
entry_temp_start_test_3.grid(row=3, column=1)

label_exp_time_test_3 = tk.Label(master=frm_current_params_unit_3, text='Время выдержки испытания 3, мин.')
entry_exp_time_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_1)
label_exp_time_test_3.grid(row=4, column=0, sticky="e")
entry_exp_time_test_3.grid(row=4, column=1)

label_len_time_test_3 = tk.Label(master=frm_current_params_unit_3, text='Время длительности испытания 3, сек.')
entry_len_time_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_1)
label_len_time_test_3.grid(row=5, column=0, sticky="e")
entry_len_time_test_3.grid(row=5, column=1)

label_time_pusk_test_3 = tk.Label(master=frm_current_params_unit_3, text='Время пуска испытания 3')
entry_time_pusk_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_1, state='disabled')
label_time_pusk_test_3.grid(row=6, column=0, sticky="e")
entry_time_pusk_test_3.grid(row=6, column=1)

label_time_start_test_3 = tk.Label(master=frm_current_params_unit_3, text='Время начала испытания 3')
entry_time_start_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_1, state='disabled')
label_time_start_test_3.grid(row=7, column=0, sticky="e")
entry_time_start_test_3.grid(row=7, column=1)

label_current_test_3 = tk.Label(master=frm_current_params_unit_3, text='Ток образца 3, А')
entry_current_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_1, state='disabled')
label_current_test_3.grid(row=9, column=0, sticky="e")
entry_current_test_3.grid(row=9, column=1)

label_temp_test_3 = tk.Label(master=frm_current_params_unit_3, text='Температура образца 3, гр С')
entry_temp_test_3 = tk.Entry(master=frm_current_params_unit_3, width=WIDTH_1, state='disabled')
label_temp_test_3.grid(row=10, column=0, sticky="e")
entry_temp_test_3.grid(row=10, column=1)

# =================================================================================================

'''
label_ = tk.Label(master=frm_current_params_unit_1, text='qqqqqqqq')
entry_ = tk.Entry(master=frm_current_params_unit_1, width=50)
label_.grid(row=1, column=0, sticky="e")
entry_.grid(row=1, column=1)
'''

# Запуск приложения.
window.mainloop()
