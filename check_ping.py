#!/usr/bin/python

'''
check response from remote host
'''

import os, datetime, sys, time, logging

def check_ping():
    response = os.system(f'ping -c 1 {HOSTNAME}')
    if response == 0:
        pingstatus = 'network active'
        log('INFO', HOSTNAME, pingstatus)
    else:
        pingstatus = 'network error'
        log('ERROR', HOSTNAME, pingstatus)
    return pingstatus

def log(severiry, host, message):
    # создаём logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # создаём консольный handler и задаём уровень
    # ch = logging.StreamHandler()
    ch = logging.FileHandler(f'./log_{time.strftime("%Y%m%d")}.log')
    ch.setLevel(logging.DEBUG)
    # создаём formatter
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
    #formatter = logging.Formatter(f'{asctime} {name} {levelname} {hostname} {message}')
    # добавляем formatter в ch
    ch.setFormatter(formatter)
    # добавляем ch к logger
    logger.addHandler(ch)
    # код "приложения"
    if severiry == 'INFO':
        logger.info(message)
    if severiry == 'ERROR':
        logger.error(message)

if __name__ == "__main__":
    HOSTNAME = sys.argv[1]
    pingstatus = check_ping()
    print(pingstatus)
    if pingstatus == 'network error':
        os.system(f'ipsec stop')
        log("INFO", HOSTNAME, 'ipsec stop')
        time.sleep(3)
        os.system(f'ipsec start')
        log("INFO", HOSTNAME, 'ipsec start')
        time.sleep(3)