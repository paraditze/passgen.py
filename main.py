import random
import array
import pandas as pd


LENGTH = 20
NUMBER = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOWER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
         'z']
UPPER = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
         'Z']
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
characterList = NUMBER + UPPER + LOWER + SYMBOLS

digit_random = random.choice(NUMBER)
upper_random = random.choice(UPPER)
lower_random = random.choice(LOWER)
symbol_random = random.choice(SYMBOLS)

temppw = digit_random + upper_random + lower_random + symbol_random

for i in range(LENGTH - 4):
    temppw = temppw + random.choice(characterList)
    temppw_array = array.array('u', temppw)
    random.shuffle(temppw_array)

password = ""
for i in temppw_array:
    password = password + i

pw = pd.DataFrame([password])
pw.to_clipboard(index=False,header=False)


print(password)
