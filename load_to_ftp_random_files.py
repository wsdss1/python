#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
connect to ftp server, create dir and generate file
'''

import os, logging, logging.config, time, datetime, shutil, random, uuid, sys, pyodbc
from ftplib import FTP

HOST = "10.200.12.228"
PORT = 21
UNAME = "ftpuser"
PS = "12345"
ftp = FTP('10.200.12.228', 'ftpuser', '12345')
SQL_SERVER_CONNECT = "Driver={SQL Server Native Client 11.0};Server=10.200.12.223;Database=SSNTI;Trusted_Connection=no;uid=test;pwd=Password12!"

waveform_archive_t = ['to','t01','t02','t03','t04','t05','t06','t07','t08','t09','t0A','t0B','t0C','t0D','t0E','t0F']
waveform_archive_d = ['do','d01','d02','d03','d04','d05','d06','d07','d08','d09','d0A','d0B','d0C','d0D','d0E','d0F']

temp_folder = "temp_folder"
current_dir = os.path.dirname(os.path.realpath(__file__))
NEW_PATH = 'temp_folder_sended'

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
def create_dir(created_directory: str):
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
    filename = f'{uuid.uuid4()}'
    create_dir(temp_folder)
    for i in used_archive:
        full_filename = f'{current_dir}/temp_folder/{filename}.{i}'
        newfile = open(full_filename, 'wb')
        size = random.randint(100000, 9999999) # in bytes
        newfile.seek(size)
        newfile.write(b'\0')
        logger.info(f'{sys._getframe().f_code.co_name}  {full_filename}  size= {size} bytes')
        newfile.close()

# upload file on ftp
def upload_ftp(file: str):
    logger.info(f'{sys._getframe().f_code.co_name}  try connect to {HOST}:{PORT} ftp server')
    ftp.connect(HOST, PORT)
    logger.info(f'{sys._getframe().f_code.co_name}  try login to ftp server')
    ftp.login(UNAME, PS)
    # Перейти в директорию
    ftp.cwd('/home/ftpuser/')
    logger.info(f'{sys._getframe().f_code.co_name}  read file from temp_folder')
    myfile = open(f'{current_dir}/temp_folder/{file}', 'rb')
    logger.info(f'{sys._getframe().f_code.co_name}  try stor file to ftp server')
    ftp.storbinary(f'STOR {file}', myfile)
    logger.info(f'{sys._getframe().f_code.co_name}  file sended to ftp server')
    myfile.close()

def read_local_dir():
    file_list = os.listdir(f'./{temp_folder}')
    num_files = len(os.listdir(f'./{temp_folder}'))
    logger.info(f'{sys._getframe().f_code.co_name}  read {num_files} files in {temp_folder}')
    for file in file_list:
        logger.info(f'{sys._getframe().f_code.co_name}  try upload {file} to ftp server') 
        upload_ftp(file)
        create_dir(NEW_PATH)
        logger.info(f'{sys._getframe().f_code.co_name}  send file {file} to {NEW_PATH}') 
        shutil.move(f'{current_dir}\\temp_folder\{file}', f'{current_dir}\{NEW_PATH}')

def sql_connect():
    logger.info(f'{sys._getframe().f_code.co_name}  try connect to SQL Server:10.200.12.223') 
    cnxn = pyodbc.connect(SQL_SERVER_CONNECT)
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM [SSNTI_20190214].[dbo].[NTI_FILE]')
    for row in cursor:
            print(f'row = {row,}')

if __name__ == '__main__':  
    #rnd_file_create()
    #main()
    sql_connect()