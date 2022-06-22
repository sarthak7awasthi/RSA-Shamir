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
       
        rsaObject=RSAKey(text)
        shamirObject=Shamir(rsaObject.getPrivateKey())
        shamirObject.shard()
        rsaObject.encryptText()
        privKey=shamirObject.recover([2,5])
    
        decryptedText=rsaObject.decryptText(privKey)

        self.assertEqual(text,decryptedText)
    
if __name__ == '__main__':
    unittest.main()


