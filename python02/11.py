
#11111111111111111

#my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
           #0, 1, 2, 3, 4, 5, 6, 7, 8, 9
           #-1, 2-, 3-, 4-, 5-, 6-, 7-, 8-, 9-

#list[start:end:step]

##print(my_list[:])

#22222222222222222

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = []
#for n in nums:
    #my_list.append(n)
#print(my_list)

#333333333333333333

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = [n for n in nums]
#print(my_list)

#444444444444444444

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = []
#for n in nums:
    #my_list.append(n*n)
#print(my_list)

#555555555555555555

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = [n*n for n in nums]
#print(my_list)

#666666666666666666

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = map(lambda n: n*n, nums)
#print(my_list)

#777777777777777777

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = []
#for n in nums:
    #if n%2 == 0:
        #my_list.append(n)
#print(my_list)

#888888888888888888

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = [n for n in nums if n%2 == 0]
#print(my_list)

#999999999999999999

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = filter(lambda n: n%2 == 0, nums)
#print(my_list)

#101010101010101010

#nums = [1,2,3,4,5,6,7,8,9,10]

#my_list = []
#for letter in'abcd':
    #for num in range(4):
        #my_list.append((letter,num))
#print(my_list)

#my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
#print(my_list)

#names = ['Judy', 'Luna']
#heros = ['Bat Judy', 'Wolver Luna']

#110110110110110110

#nums = [1,2,3,4,5,6,7,8,9,10]

#names = ['Judy', 'Luna']
#heros = ['Bat Judy', 'Wolver Luna']

#my_dict = {}
#for name, hero in zip(names, heros):
    #my_dict[name] = hero
#print(my_dict)

#120120120120120120120

#nums = [1,2,3,4,5,6,7,8,9,10]

#names = ['Judy', 'Luna']
#heros = ['Bat Judy', 'Wolver Luna']

#my_dict = {name: hero for name, hero in zip (names, heros)}
#print(my_dict)

#130130130130130130130
#nums = [1,2,3,4,5,6,7,8,9,10]


#nums = [1,2,2,1,1,3,4,3,4,5,5,6,7,8,7,9,9]
#my_set = set()
#for n in nums:
    #my_set.add(n)
#print(my_set)
'''
my_set = {n for n in nums}
print(my_set)
'''

#nums = [1,2,3,4,5,6,7,8,9,10]

#140140140140140140140140
nums = [1,2,3,4,5,6,7,8,9,10]


nums = [1,2,3,4,5,6,7,8,9,10]

#def gen_func(numms):
    #for n in nums:
        #yield n*n

#my_gen = gen_func(nums)

#for i in my_gen:
    #print (i)

#150150150150150150150
nums = [1,2,3,4,5,6,7,8,9,10]


nums = [1,2,3,4,5,6,7,8,9,10]

my_gen = (n*n for n in nums)

for i in my_gen:
    print (i)