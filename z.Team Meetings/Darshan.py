# def Add(x, y):
#     while (y != 0):
#         carry = x & y
#         x = x ^ y
#         y = carry << 1
#     return x
#
# Add(3,6)
# print(Add(27,5))

def add(a,b):
    for i in range(1, b+1):
        a = a + 1
    return a

a = add(10, 32)
print(a)