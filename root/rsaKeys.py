import rsa
from cryptography.fernet import Fernet
# class for RSA key pair generation
class RSAKey:
    # has attributes text(original message) and key pair
    def __init__(self,text):
        self.text=text
        self.publicKey, self.privateKey = rsa.newkeys(512)
    # writes the public key to text file
    def PublicKeyFile(self):
        name='Public.TXT'
        with open (name, 'w') as File:
            File.write(str(self.publicKey))
    # encrypts the text using the public key
    def encryptText(self):
        self.PublicKeyFile()
        return rsa.encrypt(self.text.encode(),
                         self.publicKey)
    # decrypts the text using the private key
    def decryptText(self,keyPrivate):
        return rsa.decrypt(self.encryptText(), keyPrivate).decode()
    # getter for private key
    def getPrivateKey(self):
        return self.privateKey
    # getter for public key
    def getPublicKey(self):
        return self.publicKey

