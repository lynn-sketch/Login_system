"""FILE HANDLING IN PYTHON"""


def main():
    display()


def registration():
    name = input('Enter your name: ').upper()
    while True:
        try:
            phone = int(input('Enter your phone number: '))
            break
        except ValueError:
            print('Your phone number is invalid')

    while True:
        email = input('Enter you email: ')
        if email.islower():
            pass
            break
        if any(c.isupper() for c in email):
            print('The email is invalid')

    def details():
        # lists = ['@', ',', '#']
        password = input('Enter your password: ')
        upper = any(c.isupper() for c in password)
        lower = any(c.islower() for c in password)
        digit = any(c.isdigit() for c in password)
        # symbol = any(lists for lists in password)
        length = len(password) >= 6
        verification = upper and lower and length and digit
        while not verification:
            if verification:
                pass
                break
            else:
                if not upper:
                    print('The password should at least have an uppercase letter')
                    return details()
                elif not lower:
                    print('Password should at least have a lowercase letter')
                    return details()
                elif not digit:
                    print('Password should at least have one digit')
                    return details()
                elif not length:
                    print('The password should at least have 6 characters')
                    return details()

        confirm_password = input('Confirm your password: ')
        if confirm_password != password:
            print('The password is not matching')
            return details()
        else:
            print('Account successfully created')

        with open('database1.txt', 'a') as file:
            file.write(f'{name}, {phone}, {email}, {password}\n')

    details()


def display():
    print('\t\tWelcome to the user login system')
    print('1. login')
    print('2. Register account')

    try:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            with open('database1.txt', 'r') as file2:
                saved_name = []
                saved_phone = []
                saved_email = []
                saved_password = []
                for names in file2:
                    name1, phone1, email1, password1 = names.split(', ')
                    password1 = password1.strip()
                    saved_name.append(name1)
                    saved_phone.append(phone1)
                    saved_email.append(email1)
                    saved_password.append(password1)
                    data = dict(zip(saved_name, saved_password))
                    # data2 = dict(zip(saved_email, saved_phone))
            try:
                Username = input('Enter your username: ').upper()

                if Username in data:
                    count = 0
                    userPassword = ''
                    while userPassword != data[Username]:
                        count += 1
                        userPassword = input('Enter your user password: ')
                        if userPassword == data[Username]:
                            def userData():
                                print(f'\n\n\t\tHi {Username}, WELCOME TO THE SYSTEM')
                                print('1. Deposit money')
                                print('2. Check balance')
                                print('3. Send money')
                                print('4. Withdraw cash')
                                print('5. User information')
                                print('6. Change pin')
                                choice2 = int(input('Enter your choice: '))
                                if choice2 == 1:
                                    pass
                                    # with open('database1.txt', 'w') as file:
                                    #     data[Username] = 'NewPassword'
                                    #     file.write(data[Username])
                            userData()
                        else:
                            print('Wrong password, four un successful attempts will block your account')
                            print(f'Your have {4 - count} attempts remaining\n')

                        if count == 4 and userPassword != data[Username]:
                            with open('database.txt', 'r') as file2:
                                for line in file2:
                                    if Username in line:
                                        del line
                                # del data[Username]
                                # del data[Username]  # How to delete a text from files
                            print('Account blocked! Please contact customer care for more information.')
                            break
                else:
                    print('Account with the above name is not registered\n')
                    return display()
            except UnboundLocalError:
                print('Account not registered')
                return display()

        elif choice == 2:
            return registration()

        else:
            print('Invalid input, please enter the right options\n')
            return display()
    except ValueError:
        print('Invalid input, please enter the above options\n')
        return display()


if __name__ == '__main__':
    main()



