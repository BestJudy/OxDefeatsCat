
#!

#def HE():
    #print("DFHTDFYHDRTHD")

#HE()
#HE()
#HE()
#HE()

#2

#def HE():
    #return "DFHTDFYHDRTHD"

#print(HE())

#3

#def HE(greeting, name = 'Styh'):
    #return '{}, {}'.format(greeting, name)

#print(HE('Hfgjxfgtj', name = 'Styh'))

#4

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Art', 'Design']
info = {'name': 'Judy', 'age': 9}

student_info(*courses, **info)
