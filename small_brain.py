import os, time
from cryptography.fernet import Fernet

file = open("key.key", "rb")
key = file.read()
file.close()


with open("spoliers_DO_NOT_CLICK_ME.py.encrypted", "rb") as f:
    data = f.read()

fernet = Fernet(key)
encrypted = fernet.decrypt(data)

with open("spoliers_DO_NOT_CLICK_ME.py", "wb") as f:
    f.write(encrypted)

from spoliers_DO_NOT_CLICK_ME import *

os.system("cls")

print("(hit enter)")
for i in message:
    print(i)
    input()
    os.system("cls")
