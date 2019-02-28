#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
ssh connect to remote server and 
create dir on this server
'''

import os, logging, time, paramiko

config = {'HOST' : '10.200.12.228', 'USER' : 'adminki', 'SECRET' : 'Password12!', 'PORT' : '22'}

def log(severiry, message):
    # создаём logger
    logger = logging.getLogger('create_folders')
    logger.setLevel(logging.DEBUG)
    # создаём консольный и файловый handler-ы и задаём уровень
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    create_dir(f'{logs}')
    fh = logging.FileHandler(f'./log_{time.strftime("%Y%m%d")}.log')
    fh.setLevel(logging.DEBUG)
    # создаём formatter для handler-ов
    formatter = logging.Formatter('%(asctime)s [%(process)d] %(levelname)s [%(pathname)s] %(message)s')
    # добавляем formatter в ch и fh
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # добавляем ch к logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    # код "приложения"
    if severiry == 'INFO':
        logger.info(message)
    elif severiry == 'ERROR':
        logger.error(message)
    elif severiry == 'WARNING':
        logger.warning(message)
 
def create_dir(dirName):
    dirName = 'tempDir'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")        
    # Create target Directory if don't exist
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")
    dirName = 'tempDir2/temp2/temp'
    
    # Create target directory & all intermediate directories if don't exists
    try:
        os.makedirs(dirName)    
        print("Directory " , dirName ,  " Created ")
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")  
        
    
    # Create target directory & all intermediate directories if don't exists
    if not os.path.exists(dirName):
        os.makedirs(dirName)
        print("Directory " , dirName ,  " Created ")
    else:    
        print("Directory " , dirName ,  " already exists")    

def connect_by_ssh():
    # SSHClient – основной класс, который нужен для удаленного подключения
    client = paramiko.SSHClient()
    # вносим ключ сервера в перечень известных нам хостов - файл .ssh/known_hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # подключение к host
    client.connect(hostname=config['HOST'], username=config['USER'], password=config['SECRET'], port=config['PORT'])
    stdin, stdout, stderr = client.exec_command('ls -l')
    data = stdout.read() + stderr.read()
    client.close()
    
if __name__ == '__main__':
    # create_dir()
    connect_by_ssh()