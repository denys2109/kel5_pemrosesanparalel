#Kelompok 5

import psutil as ps
import time
import sys
import os
import subprocess

def get_monitoring(arg):
    ipadd = getip_by_iface(arg);
    
    print('\n')
    print('IP Address : '+ipadd)
        
    cpu = ps.cpu_percent()
    ram = ps.virtual_memory().percent
    print('CPU Used : {}\nRAM Used :{}'.format(cpu,ram))
    rx_bytes, tx_bytes = get_txrx(arg)
    rx_kb = int(rx_bytes)/1000
    tx_kb = int(tx_bytes)/1000
    print(f"Tx / Rx [eth] : {tx_kb}kbps / {rx_kb}kbps")
    time.sleep(2)
        
def get_txrx(interface):
    for line in open('/proc/net/dev', 'r'):
        if interface in line:
            data = line.split('%s:' % interface)[1].split()
            rx_bytes, tx_bytes = (data[0], data[8])
            return (rx_bytes, tx_bytes)
            
def getip_by_iface(iface):
    return os.popen("ip addr | grep "+iface+" | awk '{print $2}' | tail -n +2").read().strip();
    
def getalllinterface():
    return subprocess.check_output("nmcli d | awk '{print $1}' | tail -n +2 | head -n -1", shell = True, universal_newlines = True);
        
if __name__=="__main__":
    os.system("clear")
    print("Menu APPS")
    ifaces = getalllinterface().split('\n')
    ifaces.remove("")
    for idx, iface in enumerate(ifaces):
        if (iface != ''):
            print("{0}. Node {0}".format(idx+1));
        
    print("\nMasukkan Perintah/Pilihan anda :");
    opti = int(input());
    if (opti < 1) or (opti > len(ifaces)):
        print('perintah tidak dikenal')
    else:
        get_monitoring(ifaces[opti-1])
        sys.exit(1);
   