#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
check response from remote host
check pppID to create route
'''

import os, sys, time, logging

def log(severiry, message):
    # создаём logger
    logger = logging.getLogger('check response')
    logger.setLevel(logging.DEBUG)
    # создаём консольный и файловый handler-ы и задаём уровень
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    fh = logging.FileHandler(f'./log_{time.strftime("%Y%m%d")}.log')
    #fh = logging.FileHandler(f'/home/adminzabbix/check_response/log_{time.strftime("%Y%m%d")}.log')
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

def check_ping():
    response = os.system(f'ping -c 1 {HOSTNAME}')
    if response == 0:
        pingstatus = 'network active'
        log('INFO', f'{pingstatus} [{HOSTNAME}]')
    else:
        pingstatus = 'network down'
        log('ERROR',f'{pingstatus} [{HOSTNAME}]')
    return pingstatus

def get_pppid():
    network_interfaces = os.listdir('/sys/class/net/')
    for interface in network_interfaces:
        if 'ppp' in interface:
            log('INFO', f'network interfaces {interface}')
            return interface
        else:
            log('ERROR', 'not pppID in network interfaces')

if __name__ == '__main__':
    HOSTNAME = sys.argv[1]
    pingstatus = check_ping()
    if pingstatus == 'network down':
        # 1 step
        os.system(f'sudo service strongswan restart')
        time.sleep(3)
        log('WARNING', 'service strongswan restart')
        # 2 step
        os.system(f'sudo ipsec down akomovpn')
        log('WARNING', 'ipsec down akomovpn')
        time.sleep(3)
        os.system(f'sudo ipsec up akomovpn')
        log('WARNING', 'ipsec up akomovpn')
        time.sleep(3)
        # 3 step
        os.system(f'sudo service xl2tpd restart')
        log('WARNING', 'service xl2tpd restart')
        time.sleep(3)
        # 4 step
        pppID = get_pppid()
        os.system(f'sudo route add -net 192.168.0.0/24 dev {pppID}')
        log('WARNING', f'route add -net 192.168.0.0/24 dev {pppID}')
        sys.exit()
    else:
        sys.exit()