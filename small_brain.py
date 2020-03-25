import os, time
from cryptography.fernet import Fernet

from fileEncrypting import secureFile

file = open("key.key", "rb")
key = file.read()
file.close()


secureFile("spoliers_DO_NOT_CLICK_ME.py", key).decryptFile()

from spoliers_DO_NOT_CLICK_ME import *

os.system("cls")

print("(hit enter)")
for i in message:
    print(i)
    input()
    os.system("cls")
