@decorator
def add(x,y):
    z = x+y
    print("summ",z)
    return z


def decorator(func):

    def inner(x,y):
        if x<0 and y < 0:
            print("negative values")
            return func(x,y)
        # else:
        #     return func(x,y)
    return inner

# add1 = decorator(add)

add(-1 ,-1)
# add1(4,2)