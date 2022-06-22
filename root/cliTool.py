from rsaKeys import RSAKey
from shamir import Shamir
from unitTest import cliTest
import os
import sys
def CLI():
    try:
        
        if sys.argv[1:3]==['run', 'program'] or sys.argv[1:3]==['run' ,'app']:
            message=input('Enter the message: ')
            rsaObject=RSAKey(message)
            rsaObject.PublicKeyFile()
            print("Public.TXT file created.")
            rsaObject.encryptText()
            print("Message encrypted!")
            shamirObject=Shamir(rsaObject.getPrivateKey())
            shamirObject.shard()
            print("Private key shard files created.\nSince files are encrypted, shards can't be used outside this program.")
            for x in os.listdir():
                if x.startswith("Shard"):
                    # prints shard files name
                    print(x)
            print("")
            indexes=[]
            index1=int(input("Enter index for 1st shard choice:" ))
            index2=int(input("Enter index for 2nd shard choice:" ))
            indexes.append(index1)
            indexes.append(index2)
            privKey=shamirObject.recover(indexes)
            print("Private key recovered with the shards given")
            print("decrypted message is: ", rsaObject.decryptText(privKey))
            print('deleting shards files!')
            for x in os.listdir():
                # delete shard files
                if x.startswith("Shard"):
                    os.remove(x)
            option=input("Press y to end program, n to restart: ")
            if option=="yes" or option=="y":
                print("Program Ending.")
                return
            elif option=="no" or option=="n":
                CLI()
        else:
            print("wrong command or typo")
    except:
        raise Exception("Command Not recognized")
    
   








if __name__ == '__main__':
    CLI()