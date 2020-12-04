import sys
import os
import subprocess

valid = "1234567890,"

def getip_by_iface(iface):
    return os.popen("ip addr | grep "+iface+" | awk '{print $2}' | tail -n +2").read().strip();

def getalllinterface():
    return subprocess.check_output("nmcli d | awk '{print $1}' | tail -n +2 | head -n -1", shell = True, universal_newlines = True);

def NodesMenu():
    ifaces = getalllinterface().split('\n')
    ifaces.remove("")
    
    for idx, iface in enumerate(ifaces):
        if (iface != ''):
            print("{0}. Node {0}".format(idx+1));
    nodes = input("Masukkan Perintah/Pilihan anda : ")
    return nodes.split(",")

def OperasiMenu():
    print("\n")
    print("1. Hitung Luas dan keliling Segitiga")
    print("2. Hitung Luas dan keliling Lingkaran")
    print("3. Hitung Luas dan keliling Persegi")
    
    opti = input("Masukkan Node yang akan melakukan komputasi? ")
    return opti.split()
    
def validate(arr, lim):
    validate = True
    for i in arr:
        if (i not in valid):
            validate = False
        elif (int(i) > lim or int(i) < 1):
            validate = False
    return validate
    
def luas_segitiga():
    alas = int(input("\nAlas Segitita : "))
    tinggi = int(input("Tinggi Segitita : "))
    luas = (alas * tinggi) / 2
    return luas
    
def kel_segitiga():
    sisiA = int(input("\nSisi A : "))
    sisiB = int(input("Sisi B : "))
    sisiC = int(input("Sisi C : "))
    kel = sisiA + sisiB + sisiC
    return kel

def lingkaran():
    jari = int(input("\nJari-jari Lingkaran : "))
    return jari
    
def Persegi():
    sisi = int(input("\nSisi Persegi : "))
    return sisi
    
        
if __name__=="__main__":
    os.system("clear")
    print("Pilihan Node")
    ifaces = getalllinterface().split('\n')  
    ifaces.remove("")
    nodes = NodesMenu();        
    if (not validate(nodes, 4)):
        print('Node tidak dikenal')
    else:
        ops = OperasiMenu()
        if (not validate(ops, 3)):
            print('Operasi tidak dikenal')
        else:
            print("\nDiketahui :")
            luas = 0
            kel = 0
            if (int(ops[0]) == 1):
                luas = luas_segitiga()
                kel = kel_segitiga()
            elif (int(ops[0]) == 2):
                jari = lingkaran()
                kel = 2*3.14*jari
                luas = 3.14*(jari**2)
            elif (int(ops[0]) == 3):
                sisi = Persegi()
                luas = sisi*sisi
                kel = 4*sisi
                
            print("\nHASIL :")
            for i in nodes:
                ip = getip_by_iface(ifaces[int(i)-1])
                print("Node " + str(i) + ": " + ip)
                print("Luas : " + str(luas))
                print("Keliling : " + str(kel) + "\n")
    
    sys.exit(1);