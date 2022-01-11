import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ['@', '#', '%', '!', '?', '*', '&', '(', ')']

num_letters = int(input('How many letters: '))
num_nums = int(input('How many numbers: '))
num_sym = int(input('How many symbols: '))

password = ''

for i in range (num_letters):
    rand = random.randint(0, 25)
    upper_or_lower = random.randint(0, 2)
    if upper_or_lower == 0:
        password = password + letters[rand]
    else:
        password = password + letters[rand].lower()

for i in range (num_nums):
    rand = random.randint(0, 9)
    password = password + str(numbers[rand])

for i in range(num_sym):
    rand = random.randint(0, 8)
    password = password + symbols[rand]

real_pass = ''

for i in range(len(password)):
    rand = random.randint(0, len(password)-1)
    real_pass = real_pass + password[rand]
    password = password.replace(password[rand], '', 1)

print(real_pass)
