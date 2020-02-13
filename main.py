# Excersise: 
# 1. ask username and password from user
# 2. print password and it's length
# 3. also, cover the password with * 


username = input('Hi, enter your username: ')
password = input('Enter your password: ')

password_length = len(password)
covered_password = '*' * password_length
print(f'Hi {username}, your password {covered_password} is {password_length} char(s) long!')