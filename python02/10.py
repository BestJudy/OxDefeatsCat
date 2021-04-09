
#1 SO BAD AND STUPID

#import builtins


#def my_min():
    #pass

#m = my_min[(5, 1, 4, 2, 3)]
#print(m)


#x = 'global x'

#def test(z):
    #x = 'local y'
    #print(y)
    #print(z)

#test('local z')
#print(x)

x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()