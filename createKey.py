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


class encryptFile:
    def __init__(self, filename, key):
        self.key = key
        self.filename = filename
        self.fernet = Fernet(self.key)
        self.readFile()
        self.encrypted = self.fernet.encrypt(self.data)
        self.getKey()

    def getKey(self):
        file = open("key.key", "rb")
        file.read()
        file.close()

    def readFile(self):
        with open(str(self.filename), "rb") as f:
            self.data = f.read()

    def encryptFile(self):
        with open(str(self.filename) + ".encrypted", "wb") as f:
            f.write(self.encrypted)
