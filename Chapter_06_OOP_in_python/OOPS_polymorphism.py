"""
Polymoorphism:
method overriding
operator overloading
method overloading
"""

class Father():
    user = 'test'

    def __init__(self):
        self.name = 'Darshan'

    def mobile(self):
        print("Father has Samsung")

class Son(Father):
    def __init__(self):
        pass
    #print("te,self.name)

    def mobile(self):
        print("Son has Oneplus \n")


S = Son()
S.mobile()


"""
operator overloading
"""
a = 4 + 4           #integer addition
print(a)
print()
p = "Py" + "thon"   #string concatenation
print(p)

#method overloding in other language we will have method with some names but with different parameter set
#where as in python we are achieveing this s mentioned below

def add(x, y=0, z=0):
    return x + y + z

print()
#driver code
print(add(5))
print(add(2, 3))
print(add(2, 3, 4))