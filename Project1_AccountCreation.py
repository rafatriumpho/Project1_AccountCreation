print ('To create your account:')
name = input ('Type in your first name: ')
lastname = input ('Type in your last name: ')
age = input ('Type in your age: ')
Email = input ('Type in your Email:')

if int (age) >= 18:
    password = input ('Create a password for your account:')
    conf_pass = input ('Confirme your password:')
    if (conf_pass) == (password):
        print ('Account successfully created!')
        file = open ('Users_info.txt', 'w')
        file.write (f'Users name: {name} {lastname}\n')
        file.write (f'Users age: {age}\n')
        file.write (f'Users Email: {Email}')
        file.close()
    else:
        print ('Incorrect password')
else:
    print ('You are too young to create an account')
