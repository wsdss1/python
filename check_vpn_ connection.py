#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time, pexpect

# check ping to the host
def check_ping():
    response = os.system('ping -c 1 192.1.10.12')
    if response == 0:
        pingstatus = 'network active'
    else:
        pingstatus = 'network down'
    return pingstatus

# get pppid to add correct route
def get_pppid():
    network_interfaces = os.listdir('/sys/class/net/')
    for interface in network_interfaces:
        if 'ppp' in interface:
            return interface
        else:
            print 'not pppID in network interfaces'

if __name__ == '__main__':
    pingstatus = check_ping()
    if pingstatus == 'network down':
        os.system('systemctl stop xl2tpd')
        os.system('nmcli con modify NPTS connection.interface-name ens192')
        child = pexpect.spawn("nmcli connection edit NPTS")
        child.expect ('nmcli> ')
        child.sendline ('activate ens192')
        child.sendline ('quit')
        time.sleep(3)
        pppID = get_pppid()
        cmd = 'sudo ip route add 192.1.10.0/24 dev ' + pppID
        os.system(str(cmd))
        sys.exit()
    else:
        sys.exit()
