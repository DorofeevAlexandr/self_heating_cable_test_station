import struct


class Parameter:
    def __init__(self, name, reg_adr, value_type='WORD', comment=''):
        self.name = name
        self.reg_adr = reg_adr
        self.type = value_type
        self.comment = comment
        self.value = None
        self.write_value = None
        self.en_write = False


class Parameters:
    def __init__(self):
        self.stack_of_writable_values = []
        self.p = {  's_TimePuskTest_1': Parameter('s_TimePuskTest_1', 100, 'WSTRING(16)', 'Время пуска испытания 1'),
                    's_TimeStartTest_1': Parameter('s_TimeStartTest_1', 120, 'WSTRING(16)', 'Время начала испытания 1'),
                    's_FamilyTester_1': Parameter('s_FamilyTester_1', 140, 'WSTRING(16)', 'Фамилия испытателя испытания 1'),
                    's_KableBrandTest_1': Parameter('s_KableBrandTest_1', 160, 'WSTRING(16)', 'Марка кабеля испытания 1'),
                    's_BatchNumberTest_1': Parameter('s_BatchNumberTest_1', 180, 'WSTRING(16)', 'Номер партии испытания 1'),
                    'r_TempStartTest_1': Parameter('r_TempStartTest_1', 200, 'REAL', 'Температура начала испытания 1'),
                    'w_ExpTimeTest_1': Parameter('w_ExpTimeTest_1', 202, 'WORD', 'Время выдержки испытания 1 (мин.) (по ГОСТ 4 часа)'),
                    'w_LenTimeTest_1': Parameter('w_LenTimeTest_1', 203, 'WORD', 'Время длительности испытания 1 (0-300 сек.)'),
                    's_TimePuskTest_2': Parameter('s_TimePuskTest_2', 210, 'WSTRING(16)', 'Время пуска испытания 2'),
                    's_TimeStartTest_2': Parameter('s_TimeStartTest_2', 230, 'WSTRING(16)', 'Время начала испытания 2'),
                    's_FamilyTester_2': Parameter('s_FamilyTester_2', 250, 'WSTRING(16)', 'Фамилия испытателя испытания 2'),
                    's_KableBrandTest_2': Parameter('s_KableBrandTest_2', 270, 'WSTRING(16)', 'Марка кабеля испытания 2'),
                    's_BatchNumberTest_2': Parameter('s_BatchNumberTest_2', 290, 'WSTRING(16)', 'Номер партии испытания 2'),
                    'r_TempStartTest_2': Parameter('r_TempStartTest_2', 310, 'REAL', 'Температура начала испытания 2'),
                    'w_ExpTimeTest_2': Parameter('w_ExpTimeTest_2', 312, 'WORD', 'Время выдержки испытания 2 (мин.) (по ГОСТ 4 часа)'),
                    'w_LenTimeTest_2': Parameter('w_LenTimeTest_2', 313, 'WORD', 'Время длительности испытания 2 (0-300 сек.)'),
                    's_TimePuskTest_3': Parameter('s_TimePuskTest_3', 320, 'WSTRING(16)', 'Время пуска испытания 3'),
                    's_TimeStartTest_3': Parameter('s_TimeStartTest_3', 340, 'WSTRING(16)', 'Время начала испытания 3'),
                    's_FamilyTester_3': Parameter('s_FamilyTester_3', 360, 'WSTRING(16)', 'Фамилия испытателя испытания 3'),
                    's_KableBrandTest_3': Parameter('s_KableBrandTest_3', 380, 'WSTRING(16)', 'Марка кабеля испытания 3'),
                    's_BatchNumberTest_3': Parameter('s_BatchNumberTest_3', 400, 'WSTRING(16)', 'Номер партии испытания 3'),
                    'r_TempStartTest_3': Parameter('r_TempStartTest_3', 420, 'REAL', 'Температура начала испытания 3'),
                    'w_ExpTimeTest_3': Parameter('w_ExpTimeTest_3', 422, 'WORD', 'Время выдержки испытания 3 (мин.) (по ГОСТ 4 часа)'),
                    'w_LenTimeTest_3': Parameter('w_LenTimeTest_3', 423, 'WORD', 'Время длительности испытания 3 (0-300 сек.)'),
                    'w_TimeWriteToPC_year': Parameter('w_TimeWriteToPC_year', 430, 'WORD', 'Запись времени с ПК на ПЛК  (для синхр.) Год'),
                    'w_TimeWriteToPC_month': Parameter('w_TimeWriteToPC_month', 431, 'WORD', 'Запись времени с ПК на ПЛК  (для синхр.) Месяц'),
                    'w_TimeWriteToPC_day': Parameter('w_TimeWriteToPC_day', 432, 'WORD', 'Запись времени с ПК на ПЛК  (для синхр.) День'),
                    'w_TimeWriteToPC_hour': Parameter('w_TimeWriteToPC_hour', 433, 'WORD', 'Запись времени с ПК на ПЛК  (для синхр.) Часы'),
                    'w_TimeWriteToPC_min': Parameter('w_TimeWriteToPC_min', 434, 'WORD', 'Запись времени с ПК на ПЛК  (для синхр.) Минуты'),
                    'w_TimeWriteToPC_sec': Parameter('w_TimeWriteToPC_sec', 435, 'WORD', 'Запись времени с ПК на ПЛК  (для синхр.) Секунды'),
                    'w_RegControl_1': Parameter('w_RegControl_1', 436, 'WORD', 'Регистр управления 1 '),
                    'w_RegControl_2': Parameter('w_RegControl_2', 437, 'WORD', 'Регистр управления 2'),
                    'r_CurrentTest_1': Parameter('r_CurrentTest_1', 500, 'REAL', 'Ток образца 1 (0-15 А)'),
                    'r_CurrentTest_2': Parameter('r_CurrentTest_2', 502, 'REAL', 'Ток образца 2 (0-10 А)'),
                    'r_CurrentTest_3': Parameter('r_CurrentTest_3', 504, 'REAL', 'Ток образца 3 (0-10 А)'),
                    'r_VoltageTesting': Parameter('r_VoltageTesting', 506, 'REAL', 'Напряжение тестирования (на образцах) (0-300 В)'),
                    'r_TempTest_1': Parameter('r_TempTest_1', 508, 'REAL', 'Температура образца 1'),
                    'r_TempTest_2': Parameter('r_TempTest_2', 510, 'REAL', 'Температура образца 2'),
                    'r_TempTest_3': Parameter('r_TempTest_3', 512, 'REAL', 'Температура образца 3'),
                    'r_TempTestUnit_1': Parameter('r_TempTestUnit_1', 514, 'REAL', 'Температура испытательной установки 1'),
                    'r_TempTestUnit_2': Parameter('r_TempTestUnit_2', 516, 'REAL', 'Температура испытательной установки 2'),
                    's_TimeReadFromPC': Parameter('s_TimeReadFromPC', 520, 'WSTRING(16)', 'Чтение времени с ПЛК на ПК (для синхр.)'),
                    'w_RegStatus_1': Parameter('w_RegStatus_1', 540, 'WORD', 'Регистр статуса 1 '),
                    'w_RegStatus_2': Parameter('w_RegStatus_2', 541, 'WORD', 'Регистр статуса 2'),
                    'w_RegAlarm_1': Parameter('w_RegAlarm_1', 542, 'WORD', 'Регистр аварий 1 '),
                    'w_RegAlarm_2': Parameter('w_RegAlarm_2', 543, 'WORD', 'Регистр аварий 2'),
                    'w_revers_time_1': Parameter('w_revers_time_1', 544, 'WORD', 'Обратный отсчет 1'),
                    'w_revers_time_2': Parameter('w_revers_time_2', 545, 'WORD', 'Обратный отсчет 2'),
                    'w_revers_time_3': Parameter('w_revers_time_3', 546, 'WORD', 'Обратный отсчет 3'),
                }

    def read_values(self, registers):
        for key in self.p:
            parameter = self.p[key]
            # print(key)
            # print('===', parameter.comment)
            if parameter.type == 'WORD':
                parameter.value = registers[parameter.reg_adr]
                # print(parameter.reg_adr, parameter.type, parameter.value)
            elif parameter.type == 'REAL':
                word_0 = registers[parameter.reg_adr]
                word_1 = registers[parameter.reg_adr + 1]
                buffer = struct.pack('HH', word_0, word_1)
                # print(buffer)
                # parameter.value = '%.3f' % struct.unpack('f', buffer)[0]
                parameter.value = struct.unpack('f', buffer)[0]
                # print(parameter.reg_adr, parameter.type, parameter.value)
            elif parameter.type == 'WSTRING(16)':
                word = [0 for _ in range(17)]
                word[0] = registers[parameter.reg_adr + 0]
                word[1] = registers[parameter.reg_adr + 1]
                word[2] = registers[parameter.reg_adr + 2]
                word[3] = registers[parameter.reg_adr + 3]
                word[4] = registers[parameter.reg_adr + 4]
                word[5] = registers[parameter.reg_adr + 5]
                word[6] = registers[parameter.reg_adr + 6]
                word[7] = registers[parameter.reg_adr + 7]
                word[8] = registers[parameter.reg_adr + 8]
                word[9] = registers[parameter.reg_adr + 9]
                word[10] = registers[parameter.reg_adr + 10]
                word[11] = registers[parameter.reg_adr + 11]
                word[12] = registers[parameter.reg_adr + 12]
                word[13] = registers[parameter.reg_adr + 13]
                word[14] = registers[parameter.reg_adr + 14]
                word[15] = registers[parameter.reg_adr + 15]
                word[16] = registers[parameter.reg_adr + 16]
                n0 = word.index(0)
                for i in range(len(word)):
                    if i > n0:
                        word[i] = 0

                buffer = struct.pack('HHHHHHHHHHHHHHHHH',
                                     word[0], word[1], word[2], word[3], word[4], word[5], word[6], word[7],
                                     word[8], word[9], word[10], word[11], word[12], word[13], word[14], word[15],
                                     word[16])

                parameter.value = buffer.decode('UTF-16')
                # print(parameter.reg_adr, parameter.type, parameter.value)

            elif parameter.type == 'DATE_AND_TIME':
                pass
            else:
                print('Skipped - ', parameter.type)

    def write_values(self):
        for key in self.p:
            parameter = self.p[key]
            if parameter.type == 'WORD':
                if parameter.en_write:
                    try:
                        new_value = [int(parameter.write_value)]
                    except ValueError:
                        print('Введено некоректное значение', parameter.write_value, parameter.comment)
                    else:
                        self.stack_of_writable_values.append((parameter.reg_adr, new_value))
                    finally:
                        # print('===', key, parameter.comment)
                        parameter.en_write = False
            elif parameter.type == 'REAL':
                if parameter.en_write:
                    try:
                        new_value = float(parameter.write_value)
                        buffer = struct.pack('f', new_value)
                        word_1, word_2 = struct.unpack('HH', buffer)
                    except ValueError:
                        print('Введено некоректное значение', parameter.write_value, parameter.comment)
                    else:
                        self.stack_of_writable_values.append((parameter.reg_adr,  [word_1, word_2]))
                    finally:
                        # print('===', key, parameter.comment)
                        parameter.en_write = False
            elif parameter.type == 'WSTRING(16)':
                if parameter.en_write:
                    try:
                        buffer = parameter.write_value.encode('UTF-16')
                        # print('lenbufer=', len(buffer), 'buffer=',buffer)
                        word = []
                        for i, h in enumerate(buffer):
                            if i < 34:
                                if i % 2 == 0:
                                    word.append(h)
                                else:
                                    w = word.pop() + 256 * h
                                    word.append(w)
                        del word[0]
                        for _ in range(len(word), 16):
                            word.append(0)
                        # print(len(word), word)
                    except ValueError:
                        print('Введено некоректное значение', parameter.write_value, parameter.comment)
                    else:
                        self.stack_of_writable_values.append((parameter.reg_adr,  word))
                    finally:
                        # print('===', key, parameter.comment)
                        parameter.en_write = False

            elif parameter.type == 'DATE_AND_TIME':
                pass
            else:
                pass
                # print('Skipped - ', parameter.type)


if __name__ == '__main__':
    pass
