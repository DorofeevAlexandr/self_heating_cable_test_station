from datetime import datetime, timedelta
import os
import json

from config import BASE_DIR


def open_additional_information(file_name:str):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
    return data

def save_additional_information(sample):
    sample["s_csv_file_name"] = (f'Sample{str(sample["w_sample_num"])}_{st_time()}.csv')
    file_name = create_dir(sample)
    with open(file_name, 'w', encoding="utf-8") as outfile:
        json.dump(sample, outfile)

def st_time()->str:
    dt = datetime.now()
    year = str(dt.year)
    month = str(dt.month)
    day = str(dt.day)
    hour = str(dt.hour)
    minute = str(dt.minute)
    second = str(dt.second)
    return f'{year}_{month}_{day}__{hour}_{minute}_{second}'

def create_dir(sample):
    dt = datetime.now()
    year = str(dt.year)
    month = str(dt.month)
    file_name = (f'Образец{str(sample["w_sample_num"])}_{st_time()}_'
                 f'{sample["s_KableBrandTest"]}_{sample["s_BatchNumberTest"]}.json')
    path = os.path.join(BASE_DIR, 'data_base', year, month)
    file_name = os.path.join(path, file_name)
    if not os.path.isdir(path):
        os.makedirs(path)   
    return file_name


if __name__ == '__main__':
    sample_1 = {'w_sample_num': 1,
                's_csv_file_name': '',
                's_TimePuskTest': '',            
                's_TimeStartTest': '',
                's_FamilyTester': '',
                's_KableBrandTest': 'KableBrand',
                's_BatchNumberTest': 'BatchNumber',
                'r_TempStartTest': 0,
                'w_ExpTimeTest': 0,
                'w_LenTimeTest': 0,
    }    

    save_additional_information(sample=sample_1)
    open_additional_information('data.json')
