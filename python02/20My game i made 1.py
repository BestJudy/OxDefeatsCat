import random

print('Hello whelcome to my game,')
print('this game will hatch you an pet,')
print('but you might get bad pets but its OK')

colors = ['common=cat', 'common=dog', 'uncommon=panther', 'uncommon=otter', 'rare=bee', 'rare=sea-turtle', 'ultra=red-panda', 'ultra=king-bee', 'legend=dragon', 'legend=queen-bee', 'legend=unicorn']


value = random.choices(colors, weights=[34, 34, 24, 24, 20, 20, 14, 14, 1, 1, 1] ,k=1)
print(value)





