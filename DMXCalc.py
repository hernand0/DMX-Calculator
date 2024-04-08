'''
DipSwitch DMX Calculator

diegoHERNANDO_2020
www.diegohernando.es
'''

import os

def potencias(x):
    powers = []
    i = 1
    while i<=x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers

def dec_to_bin(x):
    return int(bin(x)[2:])

def bin_to_dec(x):
    return int(x,2)
    
print("\ndH_ DMX DipSwitch Calculator\n")

for r in range(50):
    t = input("Pin Position (0) | Address (1): ")
    if (t == '0'):
        h = input("\nFrom 1 to 9 (1 to 256)\nON = 1\nFill with zeroes if needed\nPosition of pins: ")
        h = h[0:9]
        j = h[::-1]
        print(bin_to_dec(j))
    elif (t == '1'):
        h = int(input("\nDMX Address: "))
        z = str(dec_to_bin(h))
        y = z[::-1]
        print(potencias(h))
        print(y)
    elif(t == 'c'):
        os.system("clear")
    else:
        print("\n"+str(t)," invalid command\n")
        pass
