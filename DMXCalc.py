'''
DipSwitch DMX Calculator

diegoHERNANDO_2020
www.diegohernando.es
'''

# Only for cleaning the screen in the 50 times loop
import os

# Calculate powers of 2
def potencias(x):
    powers = []
    i = 1
    while i<=x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers

# Decimal to binary
def dec_to_bin(x):
    return int(bin(x)[2:])
# Binary to decimal
def bin_to_dec(x):
    return int(x,2)
    
print("\ndH_ DMX DipSwitch Calculator\n")

for r in range(50):
    t = input("\nPin Position (0) | Address (1): ")
    if (t == '0'):
        h = input("\nFrom 1 to 9 (1 to 256)\nON = 1\nFill with zeroes if needed\nPosition of pins: ")
        h = h[0:9]
        j = h[::-1]
        print('\nDMX Address:',bin_to_dec(j))
    elif (t == '1'):
        h = int(input("\nDMX Address: "))
        z = str(dec_to_bin(h))
        y = z[::-1]
        print('\nPowers of 2:', potencias(h))
        print('Pin Position:', y)
    elif(t == 'c'):
        os.system("clear")
    else:
        print("\n"+str(t)," invalid command\n")
        pass
