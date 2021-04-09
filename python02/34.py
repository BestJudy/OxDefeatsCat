
#1

'''
first_name = 'e465fhy'
last_name = 'AWRTGDCFN'

sentence = f'My name is {first_name} {last_name}'
print(sentence)
'''

#2

'''
person = {'name': 'd4e56y', 'age': '56'}

sentence = f'my name is {person('name')} and i am {person('age'))} and i hate python'
print(sentence)
'''

#3
'''
calculation = f'4 times 11 is equal to {4 * 11}'
#(type any number * or / or whatever to the word)
print(calculation)
'''

#4

'''
for n in range(1, 11):
    sentence = f'The value is {n}'
    print(sentence)
'''

#5

'''
for n in range(1, 11):
    sentence = f'The value is {n:02}'
    print(sentence)
'''

#6

'''
pi = 6.574567
#(type any number)

sentence = f'Pi is equal to {pi}'
print(sentence)
'''

#7

from datetime import datetime

birthday = datetime(2021, 1, 3)

sentence = f't6j has a birthday on {birthday:%B %d, %Y}'
print(sentence)