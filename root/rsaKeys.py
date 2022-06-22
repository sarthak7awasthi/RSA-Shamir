import rsa
from cryptography.fernet import Fernet

class RSAKey:
    def __init__(self,text):
        self.text=text
        self.publicKey, self.privateKey = rsa.newkeys(512)
    def PublicKeyFile(self):
        name='Public.TXT'
        with open (name, 'w') as File:
            File.write(str(self.publicKey))
    def encryptText(self):
        self.PublicKeyFile()
        return rsa.encrypt(self.text.encode(),
                         self.publicKey)
    def decryptText(self,keyPrivate):
        return rsa.decrypt(self.encryptText(), keyPrivate).decode()

    def getPrivateKey(self):
        return self.privateKey

    def getPublicKey(self):
        return self.publicKey

