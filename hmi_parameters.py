import struct


class Parameter:
    def __init__(self, name, reg_adr, value_type='WORD', comment=''):
        self.name = name
        self.reg_adr = reg_adr
        self.type = value_type
        self.comment = comment
        self.value = None


class Parameters:
    def __init__(self):
        self.p = {'dt_TimePuskTest_1': Parameter('dt_TimePuskTest_1', 100, 'DATE_AND_TIME', 'Время пуска испытания 1'),
                    'dt_TimeStartTest_1': Parameter('dt_TimeStartTest_1', 104, 'DATE_AND_TIME', 'Время начала испытания 1'),
                    's_FamilyTester_1': Parameter('s_FamilyTester_1', 108, 'WSTRING(16)', 'Фамилия испытателя испытания 1'),
                    's_KableBrandTest_1': Parameter('s_KableBrandTest_1', 128, 'WSTRING(16)', 'Марка кабеля испытания 1'),
                    's_BatchNumberTest_1': Parameter('s_BatchNumberTest_1', 148, 'WSTRING(16)', 'Номер партии испытания 1'),
                    'r_TempStartTest_1': Parameter('r_TempStartTest_1', 168, 'REAL', 'Температура начала испытания 1'),
                    'w_ExpTimeTest_1': Parameter('w_ExpTimeTest_1', 170, 'WORD', 'Время выдержки испытания 1 (мин.) (по ГОСТ 4 часа)'),
                    'w_LenTimeTest_1': Parameter('w_LenTimeTest_1', 171, 'WORD', 'Время длительности испытания 1 (0-300 сек.)'),
                    'dt_TimePuskTest_2': Parameter('dt_TimePuskTest_2', 172, 'DATE_AND_TIME', 'Время пуска испытания 2'),
                    'dt_TimeStartTest_2': Parameter('dt_TimeStartTest_2', 176, 'DATE_AND_TIME', 'Время начала испытания 2'),
                    's_FamilyTester_2': Parameter('s_FamilyTester_2', 180, 'WSTRING(16)', 'Фамилия испытателя испытания 2'),
                    's_KableBrandTest_2': Parameter('s_KableBrandTest_2', 200, 'WSTRING(16)', 'Марка кабеля испытания 2'),
                    's_BatchNumberTest_2': Parameter('s_BatchNumberTest_2', 220, 'WSTRING(16)', 'Номер партии испытания 2'),
                    'r_TempStartTest_2': Parameter('r_TempStartTest_2', 240, 'REAL', 'Температура начала испытания 2'),
                    'w_ExpTimeTest_2': Parameter('w_ExpTimeTest_2', 242, 'WORD', 'Время выдержки испытания 2 (мин.) (по ГОСТ 4 часа)'),
                    'w_LenTimeTest_2': Parameter('w_LenTimeTest_2', 243, 'WORD', 'Время длительности испытания 2 (0-300 сек.)'),
                    'dt_TimePuskTest_3': Parameter('dt_TimePuskTest_3', 244, 'DATE_AND_TIME', 'Время пуска испытания 3'),
                    'dt_TimeStartTest_3': Parameter('dt_TimeStartTest_3', 248, 'DATE_AND_TIME', 'Время начала испытания 3'),
                    's_FamilyTester_3': Parameter('s_FamilyTester_3', 252, 'WSTRING(16)', 'Фамилия испытателя испытания 3'),
                    's_KableBrandTest_3': Parameter('s_KableBrandTest_3', 272, 'WSTRING(16)', 'Марка кабеля испытания 3'),
                    's_BatchNumberTest_3': Parameter('s_BatchNumberTest_3', 292, 'WSTRING(16)', 'Номер партии испытания 3'),
                    'r_TempStartTest_3': Parameter('r_TempStartTest_3', 312, 'REAL', 'Температура начала испытания 3'),
                    'w_ExpTimeTest_3': Parameter('w_ExpTimeTest_3', 314, 'WORD', 'Время выдержки испытания 3 (мин.) (по ГОСТ 4 часа)'),
                    'w_LenTimeTest_3': Parameter('w_LenTimeTest_3', 315, 'WORD', 'Время длительности испытания 3 (0-300 сек.)'),
                    'dt_TimeWriteToPC': Parameter('dt_TimeWriteToPC', 316, 'DATE_AND_TIME', 'Запись времени с ПЛК на ПК (для синхр.)'),
                    'w_RegControl_1': Parameter('w_RegControl_1', 320, 'WORD', 'Регистр управления 1 '),
                    'w_RegControl_2': Parameter('w_RegControl_2', 321, 'WORD', 'Регистр управления 2'),
                    'r_CurrentTest_1': Parameter('r_CurrentTest_1', 500, 'REAL', 'Ток образца 1 (0-15 А)'),
                    'r_CurrentTest_2': Parameter('r_CurrentTest_2', 502, 'REAL', 'Ток образца 2 (0-10 А)'),
                    'r_CurrentTest_3': Parameter('r_CurrentTest_3', 504, 'REAL', 'Ток образца 3 (0-10 А)'),
                    'r_VoltageTesting': Parameter('r_VoltageTesting', 506, 'REAL', 'Напряжение тестирования (на образцах) (0-300 В)'),
                    'r_TempTest_1': Parameter('r_TempTest_1', 508, 'REAL', 'Температура образца 1'),
                    'r_TempTest_2': Parameter('r_TempTest_2', 510, 'REAL', 'Температура образца 2'),
                    'r_TempTest_3': Parameter('r_TempTest_3', 512, 'REAL', 'Температура образца 3'),
                    'r_TempTestUnit_1': Parameter('r_TempTestUnit_1', 514, 'REAL', 'Температура испытательной установки 1'),
                    'r_TempTestUnit_2': Parameter('r_TempTestUnit_2', 516, 'REAL', 'Температура испытательной установки 2'),
                    'dt_TimeReadFromPC': Parameter('dt_TimeReadFromPC', 520, 'DATE_AND_TIME', 'Чтение времени с ПК на ПЛК (для синхр.)'),
                    'w_RegStatus_1': Parameter('w_RegStatus_1', 524, 'WORD', 'Регистр статуса 1 '),
                    'w_RegStatus_2': Parameter('w_RegStatus_2', 525, 'WORD', 'Регистр статуса 2'),
                    'w_RegAlarm_1': Parameter('w_RegAlarm_1', 526, 'WORD', 'Регистр аварий 1 '),
                    'w_RegAlarm_2': Parameter('w_RegAlarm_2', 527, 'WORD', 'Регистр аварий 2')}

    def update_value(self, registers):
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
                parameter.value = struct.unpack('f', buffer)[0]
                # print(parameter.reg_adr, parameter.type, parameter.value)
            elif parameter.type == 'WSTRING(16)':
                word_0 = registers[parameter.reg_adr]
                word_1 = registers[parameter.reg_adr + 1]
                word_2 = registers[parameter.reg_adr + 2]
                word_3 = registers[parameter.reg_adr + 3]
                word_4 = registers[parameter.reg_adr + 4]
                word_5 = registers[parameter.reg_adr + 5]
                word_6 = registers[parameter.reg_adr + 6]
                word_7 = registers[parameter.reg_adr + 7]
                word_8 = registers[parameter.reg_adr + 8]
                word_9 = registers[parameter.reg_adr + 9]
                word_10 = registers[parameter.reg_adr + 10]
                word_11 = registers[parameter.reg_adr + 11]
                word_12 = registers[parameter.reg_adr + 12]
                word_13 = registers[parameter.reg_adr + 13]
                word_14 = registers[parameter.reg_adr + 14]
                word_15 = registers[parameter.reg_adr + 15]
                word_16 = registers[parameter.reg_adr + 16]
                buffer = struct.pack('HHHHHHHHHHHHHHHHH', word_0, word_1, word_2, word_3, word_4, word_5, word_6, word_7,
                                     word_8, word_9, word_10, word_11, word_12, word_13, word_14, word_15, word_16)
                print(buffer)
                # string_bytes = struct.unpack('ssssssssssssssssssssssssssssssssss', buffer)
                # print(string_bytes)
                parameter.value = buffer.decode('UTF-16')
                print(parameter.reg_adr, parameter.type, parameter.value)

            elif parameter.type == 'DATE_AND_TIME':
                pass
            else:
                print('Skipped - ', parameter.type)


if __name__ == '__main__':
   pass

pass
