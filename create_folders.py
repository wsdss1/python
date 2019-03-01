#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
connect to ftp server, create dir and generate file
'''

import os, logging, logging.config, time, datetime, shutil, random, uuid, sys
from ftplib import FTP

HOST = "10.200.12.228"
PORT = 21
UNAME = "ftpuser"
PS = "12345"
ftp = FTP('10.200.12.228', 'ftpuser', '12345')

waveform_archive_t = ['to','t01','t02','t03','t04','t05','t06','t07','t08','t09','t0A','t0B','t0C','t0D','t0E','t0F']
waveform_archive_d = ['do','d01','d02','d03','d04','d05','d06','d07','d08','d09','d0A','d0B','d0C','d0D','d0E','d0F']

temp_folder = './temp_folder'

# создаём logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# создаём консольный и файловый handler-ы и задаём уровень
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'./log_{time.strftime("%Y%m%d")}.log')
fh.setLevel(logging.DEBUG)
# создаём formatter для handler-ов
formatter = logging.Formatter('%(asctime)s  [PID %(process)d]  %(levelname)s  [%(message)s]')
# добавляем formatter в ch и fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# добавляем ch к logger
logger.addHandler(ch)
logger.addHandler(fh)


# create dirrectory
def create_dir(created_directory):
    try:
        # Create target Directory
        os.mkdir(created_directory)
        logger.info(f'{sys._getframe().f_code.co_name}  {created_directory}:created')
    except FileExistsError:
        logger.info(f'{sys._getframe().f_code.co_name}  {created_directory}:already exists')

# create random file 
def rnd_file_create():
    archives = [waveform_archive_t, waveform_archive_d]
    used_archive = random.choice(archives)
    # generate a random UUID
    filename = f"{uuid.uuid4()}"
    for i in used_archive:
        full_filename = f"./temp_folder/{filename}.{i}"
        newfile = open(full_filename, "wb")
        size = random.randint(100000, 9999999) # in bytes
        newfile.seek(size)
        newfile.write(b"\0")
        logger.info(f'{sys._getframe().f_code.co_name}  {full_filename}  size= {size} bytes')
        newfile.close()

# upload file on ftp
def upload_ftp(file):
    func_name = sys._getframe().f_code.co_name
    ftp.connect(HOST, PORT)
    ftp.login(UNAME, PS)
    # Перейти в директорию
    ftp.cwd('/')
    myfile = open(src, 'rb')
    ftp.storbinary(f'STOR {filename}', myfile)
    ftp.storbinary(f'STOR {filename}.flag', myfile)
    myfile.close()

'''
def main():
    file_list = os.listdir(temp_folder)
    num_files = len(os.listdir(temp_folder))
    logger.info(f'read {num_files} files in {temp_folder}')
    for file in file_list:
        upload_ftp(file_name)
        logger.info(f'try upload {file_name} to ftp server') 


                print("пытаюсь загрузить файл")
                upload_ftp(SUP, F1, file_name)
                print("загрузил файл")
                i = i+1
                if i != num_files:
                    print("еще не все передано")
                    print(f"transfer {i} ({file_name}) from {num_files} files")
                    if j <= (num_files - 1):
                        delay_time = create_time_delay(time_sorted_list[j], time_sorted_list[j + 1])
                        print(delay_time)
                        j = j + 1
                        time.sleep(delay_time)
                        # move copied file to other path
                        shutil.move(F1, NEW_PATH)
                else:
                    shutil.move(F1, NEW_PATH)
                    print(f"\nWill be transfered {num_files} files. \n\t\tDone!")
                    # move all files
                    break
'''

if __name__ == '__main__':  
    create_dir(temp_folder)
    rnd_file_create()

