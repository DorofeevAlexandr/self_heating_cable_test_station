from ftplib import FTP

from config import IP_PLC, PLC_USERNAME, PLC_PASSWORD
import os


class CsvFileReader:
    def __init__(self, year=2021, month=8, day=9, host=IP_PLC, username=PLC_USERNAME, password=PLC_PASSWORD):
        self.year = year
        self.month = month
        self.day = day
        self.host = host
        self.username = username
        self.password = password
        self.ftp = FTP(self.host)

    def __enter__(self):
        print('enter')
        print(self.ftp.login(self.username, self.password))
        # print(self.ftp.dir())
        # self.ftp.retrlines('LIST')
        # print(self.ftp.pwd())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self.ftp.quit()

    def path_dir_in_plc(self):
        result = '/sd0/' + str(self.year) + '/' + str(self.month) + '/'
        return result

    def get_path(self):
        result = self.ftp.pwd()
        print(result)
        return result

    def copy_file(self, ftp_path, file_name, pc_path=''):
        self.ftp.cwd(ftp_path)
        my_file = open(os.path.join(pc_path, file_name), 'wb')
        self.ftp.retrbinary('RETR ' + file_name, my_file.write, 1024)
        my_file.close()

    def get_dir_list(self, path):
        print('=================')
        print('cwd - ' + path + ' - ' + self.ftp.cwd(path))
        # result = self.ftp.dir()
        answer_list = []
        self.ftp.retrlines('LIST', answer_list.append)
        result = []
        for answer in answer_list:
            # print(answer)
            result.append(answer.split()[-1])
        print(*result, sep='\n')
        print(type(result))
        print('==================')
        return result

    def open_file(self, file_name):
        import csv
        with open(file_name) as File:
            reader = csv.reader(File, delimiter=';', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                print(row)


if __name__ == '__main__':
    pass
