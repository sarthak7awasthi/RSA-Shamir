from cryptography.fernet import Fernet
from pyseltongue import PlaintextToHexSecretSharer
import rsa

# class for breaking the private key into shards
class Shamir:
    def __init__(self,key):
        # has attributes key(private key), and fernet key(for file encryption and decryption)
        self.key=key
        self.fernetKey=Fernet.generate_key()
        self.keyF=Fernet(self.fernetKey)
    # breaks private key into shards
    def shard(self):
        shares = PlaintextToHexSecretSharer.split_secret(str(self.key.n), 2, 5)
        self.encryptFiles(shares)

    # recovers the original private key from two of the shards
    def recover(self,indexes):
        shares=self.decryptShardFiles(indexes)
        nValue= PlaintextToHexSecretSharer.recover_secret(shares)
        privKey=rsa.PrivateKey(int(nValue), self.key.e, self.key.d, self.key.p, self.key.q)
        return privKey

    # encrypts shard files
    def encryptFiles(self,shards):
        for i in range(0,len(shards)):
            encrypted = self.keyF.encrypt(bytes(shards[i].encode()))
            name='Shard['+str(i+1)+'].TXT'
            with open (name, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
    # decrypt shard files and returns 2 of the shards in list
    def decryptShardFiles(self,indexes):
        shards=[]
        for i in range(0,len(indexes)):
            name='Shard['+str(indexes[i])+'].TXT'
            with open(name, 'rb') as encrypted_file:
                encrypted = encrypted_file.read()

            decrypted = self.keyF.decrypt(encrypted)
            shards.append((decrypted).decode("utf-8"))
        return shards