import re
import csv

email_chk = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
pwd_chk = re.compile(r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{5,}$')


def EmailValid(email):
    if re.fullmatch(email_chk, email):
      return True
    else:
      return False

def PwdValid(pwd):
    if len(pwd) < 16 and len(pwd) > 5 and re.fullmatch(pwd_chk, pwd):
      return True
    else:
      return False

def register():
    print('\nNew User Registeration\n')
    email = input('Email id: ')
    if EmailValid(email):
        password = input('Password: ')
        if PwdValid(password):
            write_file(email, password)
            print('\n.......Registeration Success............')
        else:
            print('\nInvalid Password, Please Try Again...')
    else:
        print('\nInvalid Email id, Please Try Again...')

    

def login():
    email = input('Email id: ')
    auth  = False
    if EmailValid(email):
        password = input('Password: ')
        if PwdValid(password):
            if search_file(email, password):
                print ('\n....Welcome!! Logged In Successfully...')
            else:
                print('\nUser Not Found !!!')
                register()
        else:
            print('\nInvalid Password, Please Try Again...')
    else:
        print('\nInvalid Username, Please Try Again...')

def forget_pwd():
    email = input('email id: ')
    if EmailValid(email):
        if search_pwd(email):
            print ('\nPlease Login...\n')
            login()
        else:
            print('\nUser Not Found !!!')
            register()
    else:
        print('\nInvalid Username, Please Try Again...')

def search_file(email, pwd , mode = 'r', encoding = 'UTF8', newline = ''):
    with open('users.csv', mode, encoding = encoding, newline = newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0] and pwd == row[1]:
                return True
        return False

def search_pwd(email, mode = 'r', encoding = 'UTF8', newline = ''):
    with open('users.csv', mode, encoding = encoding, newline = newline) as f:
        reader = csv.reader(f)
        for row in reader:
            if email == row[0]:
                print('\nPassword for '+ email + ' is '+ row[1])
                return True
        return False
        
def write_file(email, pwd , mode = 'a', encoding = 'UTF8', newline = ''):
    with open('users.csv', mode, encoding = encoding, newline = newline) as f:
        writer = csv.writer(f)
        writer.writerow([email, pwd])

if __name__ == "__main__":
   
    try:
        while True:
            print(''' \nHow would you like to proceed, Select an Option 1 or 2 or 3 \n
                1. Register
                2. Login
                3. Forget Password
                4. Exit
                ''')
            option = int(input())
            if option == 1:
                register()
            elif option == 2:
                login()
            elif option == 3:
                forget_pwd()
            elif option == 4:
                break
            else:
                print("Invalid Option")
    except:
        print("Type Error")