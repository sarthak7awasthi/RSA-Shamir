from shamir import Shamir
from rsaKeys import RSAKey


import unittest
import random
import string

class cliTest(unittest.TestCase):
    def test_cli(self):
        letters = string.ascii_lowercase
        # random string of 7 characters
        text = ''.join(random.choice(letters) for i in range(7))
        # Creates the RSA key pairs
        rsaObject=RSAKey(text)
        shamirObject=Shamir(rsaObject.getPrivateKey())
        # Private Key broken into 5 shards.
        shamirObject.shard()
        # Encrypts a random plain text string using the RSA Public Key.
        rsaObject.encryptText()
        # Reassembles the Private Key using shard 2 & 5.
        privKey=shamirObject.recover([2,5])
        # Decrypts the cypher text back into the plain text using the reassembled Private Key.
        decryptedText=rsaObject.decryptText(privKey)
        # Asserts the decrypted plain text is equal to the original random plain text 
        self.assertEqual(text,decryptedText)
    
if __name__ == '__main__':
    unittest.main()


