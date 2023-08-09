"Input"
print()
a = 10
print('Input for a is:', a)
a1 = 10
print('Input for a1 is:', a1)


print()
print('find the value in "a" is same in "a1":- ')
if a is a1:
    print("yes they are same")

print()
print(id(a))
print(id(a1))

print()
a = 5 + a
a += 5
print("Value of A", a)
print()
print(id(a))

print()
if a is a1:
    print("yes they are same")
else:
    print("a is not same as a1")