import time
from threading import Thread, Lock
from pyModbusTCP.client import ModbusClient

from config import IP_PLC
import hmi_parameters

SERVER_HOST = IP_PLC
SERVER_PORT = 502

plc_in_network = False

# set global
regs = {key: 0 for key in range(100, 600)}
parameters = hmi_parameters.Parameters()

# init a thread lock
regs_lock = Lock()


# modbus polling thread
def polling_thread():
    global regs
    c = ModbusClient(host=SERVER_HOST, port=SERVER_PORT)
    # polling loop
    while True:
        # keep TCP open
        plc_in_network = c.is_open()
        if not plc_in_network:
            print('plc_in_network', plc_in_network)
            c.open()
        # do modbus reading on socket
        reg_list_1 = c.read_holding_registers(100, 100)
        reg_list_2 = c.read_holding_registers(200, 100)
        reg_list_3 = c.read_holding_registers(300, 100)
        reg_list_4 = c.read_holding_registers(400, 100)
        reg_list_5 = c.read_holding_registers(500, 100)

        # if read is ok, store result in regs (with thread lock synchronization)
        if reg_list_1 and reg_list_2 and reg_list_3 and reg_list_4 and reg_list_5:
            with regs_lock:
                for i in range(0, 100):
                    regs[100 + i] = reg_list_1[i]
                for i in range(0, 100):
                    regs[200 + i] = reg_list_2[i]
                for i in range(0, 100):
                    regs[300 + i] = reg_list_3[i]
                for i in range(0, 100):
                    regs[400 + i] = reg_list_4[i]
                for i in range(0, 100):
                    regs[500 + i] = reg_list_5[i]

                while parameters.stack_of_writable_values:
                    regs_addr, regs_values = parameters.stack_of_writable_values.pop()
                    print('write->', regs_addr, regs_values)
                    c.write_multiple_registers(regs_addr, regs_values)

        # 1s before next polling
        time.sleep(1)



# start polling thread
tp = Thread(target=polling_thread)
# set daemon: polling thread will exit if main thread exit
tp.daemon = True
tp.start()


def update_parameters():
    # print('=====================================================================')
    with regs_lock:
        # print(regs)
        parameters.read_values(regs)
        parameters.write_values()


if __name__ == '__main__':
    while True:
        update_parameters()
        time.sleep(1)
