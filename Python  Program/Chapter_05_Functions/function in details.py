
print("Using *arg Argument")
def function(L, L1, L2):
    print("hello world")
    data = L
    data1 = L1
    data2 = L2
    print(data)
    print(data1)
    print(data2)

function(10, 20, 30)

print("Using *arg Argument")

print()
def function(*arg,):
    print("hello world")
    for i in arg:
        print(i)

function(10, 20, 30, 40, 50,)

print()

def function(**L):

    print("hello world")
    data = L
    for key, value in data.items():
        print("{} is {}".format(key, value))

function(Firstname='sita', Lastname='sharma', Age = 22, Phone=1234567890)

print()

def function(**L):

    print("Welcome to kempegowda International Airport-Bengaluru")
    data = L
    for key, value in data.items():
        print("{} is {}".format(key, value))

function(Firstname='Karan', Lastname='Arjun', Age = [{45},34], Address='Bengaluru')

print()

def function(*args,**kwargs):
    print("hello world")
    data = args
    data_kw = kwargs
    for i in data:
        print(i)

    for key, value in data_kw.items():
        print("{} is {}" .format(key, value))
    print(type(data_kw))

function(10, 20, name = 'pritam', section = 'D Sec')