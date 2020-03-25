from cryptography.fernet import Fernet


class createKey:
    def __init__(self):
        self.key = Fernet.generate_key()
        print(self.key)
        self.createFile()

    def createFile(self):
        file = open("key.key", "wb")
        file.write(self.key)
        file.close()


class secureFile:
    def __init__(self, filename, key):
        self.key = key
        self.filename = filename
        self.fernet = Fernet(self.key)

    def readFile(self, filename):
        with open(str(filename), "rb") as f:
            self.data = f.read()
            print("skrt")

    def encryptFile(self):
        self.readFile(self.filename)
        self.encrypted = self.fernet.encrypt(self.data)
        with open(str(self.filename) + ".encrypted", "wb") as f:
            f.write(self.encrypted)
            print("finish")

    def decryptFile(self):
        self.readFile(self.filename + ".encrypted")
        self.decrypted = self.fernet.decrypt(self.data)
        with open(str(self.filename), "wb") as f:
            f.write(self.decrypted)
            print("finish")
