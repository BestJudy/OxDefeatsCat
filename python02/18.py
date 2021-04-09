
#1, Random values

#import random


#value = random.random()
#print(value)

#2, random values from numbers before the number you put

#import random


#value = random.uniform(1,10)
#(you can change the 1, 10 to whatever)
#print(value)

#3, random number before the number

#import random


#value = random.randint(1,6)
#(change to whatever number)
#print(value)

#4, GIVE ME FOOD

#import random

#food = ['FOOD', 'HUNGRY', 'GIVE ME FOOD', 'NO MORE FOOD', 'FULL']

#value = random.choice(food)
#print(value)

#5, FOOD NOW

#import random

#food = ['FOOD', 'HUNGRY', 'GIVE ME FOOD', 'NO MORE FOOD', 'FULL']

#value = random.choice(food)
#print(value + ' NOW')

#6, WHAT COLOR

#import random

#colors = ['FOOD COLOR', 'SISSY COLOR', 'JUDY COLOR', 'FAMILY COLOR']

#results = random.choices(colors, k=1)
#print(results)

#7, WHICH COLOR WILL YOU GET

#import random

#colors = ['FOOD COLOR', 'SISSY COLOR', 'JUDY COLOR', 'FAMILY COLOR']

#results = random.choices(colors, weights=[5, 8, 1, 37] ,k=1)
#print(results)

#8, NUMBERS

#import random

#deck = list(range(1, 53))

#random.shuffle(deck)
#print(deck)



import random

deck = list(range(1, 53))

hand = random.sample(deck, k=1)
print(hand)
