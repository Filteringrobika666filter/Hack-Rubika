#!/bin/python
from os import system; from platform import system as sm
stm: str = str(sm())
if 'linux' in stm.lower() or 'mac' in stm.lower():
    s = system ('ls > data0101.txt')
    if '0' in str(s):
        print('\n\033[92myour linux system!\n')
    else:
        print('\033[31m[!] \033[36myour system is pydroid or not root, please run in linux system or command \'sudo su\' thanks')
        quit ()
    try:
        file_ = open('data0101.txt', 'r+').read()
    except:
        print('\033[31m[!] \033[36myour system is pydroid or not root, please run in linux system or command \'sudo su\' thanks')
        quit ()
    if 'hack-rubika' in str(file_):
        system('cd hack-rubika && chmod 777 * && python3 hack-rubika.py')
    else:
        system('rm -rf hack-rubika')
        system('git clone https://github.com/mester-root/hack-rubika')
        system ('cd hack-rubika')
        system ('python3 hack-rubika.py')
else:
    print('\n\033[31m[\033[36mgithun.com/mester-root/hack-rubika\033[31m]\n')
from time import sleep


print("###################################")
print("|                                 |")
print("|                                 |")
print("|    h a c k     r u b i k a      |")
print("|                                 |")
print("|                                 |")
print("|---------------------------------|")
print("|                                 |")
print("|   Manufacturer :    maziar      |")
print("|                                 |")
print("|                                 |")
print("###################################")


hack = input("TARGET  PHONE : ")

l = ["hacking the rubika 18%...", "hacking the rubika 32%....", "hacking the rubika 58%.....", "hacking the rubika 76%......", "hacking the rubika 99%.......", " * hacking failed - Done! Crack the code  rubika target :* "]

for i in l:
    print("\r" + i, end="")
    sleep(1.5)
print()

print("code : 6283" or "9473" or "9272")
