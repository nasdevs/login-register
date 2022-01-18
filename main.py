'''
@name : login-register
@author : Nasrullah
@version : 0.2.0
@url github : https://github.com/nasdevs
@url repository : https://github.com/nasdevs/login-register
'''

import json

accountsFile = open('./database/accounts.json', 'r+').read()
dataUser = json.loads(accountsFile)

class LoginRegister():
    def __init__(self, username = None, password = None):
        self.username = username
        self.password = password
    
    def login(self):
        for i in range(0, len(dataUser['accounts'])):
            if self.username == dataUser['accounts'][i]['username'] and self.password == dataUser['accounts'][i]['password']:
                return True
        return False

    def register(self):
        with open('./database/accounts.json', 'r+') as file:
            newUser = {
                'username': self.username,
                'password': self.password
            }
            dataUser['accounts'].append(newUser)
            file.seek(0)
            json.dump(dataUser, file, indent=4)

if __name__ == '__main__':
    print('===MENU===')
    print('1. Register')
    print('2. Login')
    choose = int(input('Pilih [1/2]: '))

    if choose == 1:
        print('-'*15, 'REGISTER', '-'*15)
        loop = True
        while (loop == True):
            print('Silahkan daftar username dan password anda')
            regUsername = str(input('Username : '))
            if regUsername.isalnum() == False or len(regUsername) not in range(8, 17):
                print('Username can only include letters, number and must be 8-16 characters')
            
            else: 
                while (True): 
                    regPassword = str(input('Password : '))
                    regPassword2 = str(input('Ulangin password : '))
                    if regPassword != regPassword2:
                        print('Password yang anda masukkan tidak sama')
                        print('Silahkan input ulang')
                        print('------------------------------------------')
                        print('Silahkan daftar username dan password anda')
                        print('Username :', regUsername)

                    else:
                        LoginRegister(regUsername, regPassword).register()
                        print('Registrasi akun selesai')
                        loop = False
                        login = str(input('Login [y/n] : '))
                        if login.lower() == 'y': 
                            choose = 2
                        break

    if choose == 2:
        for i in range(3):
            print('-'*15, 'LOGIN', '-'*15)
            username = str(input('username : '))
            password = str(input('password : '))
            result = LoginRegister(username, password).login()
            if result == True:
                print('Login Succes')
                break
            else:
                print('\nusername atau password anda salah\n')
        else:
            print('Anda telah gagal login sebanyak 3 kali, coba lagi setelah beberapa saat')
