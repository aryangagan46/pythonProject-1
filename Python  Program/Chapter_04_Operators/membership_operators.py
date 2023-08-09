#IN & NOT IN OPERATORS

print()
if 'D' in 'Darshan':
    print('Yes D is present')

list = [10, 20, 30, 40, 50]

print()
c = 100 in list
print(c)

print()
if 100 in list:
    print('Yes, 100 is present in list')
else:
    print("No, 100 is NOT present in list")

print()
if 100 not in list:
    print('Yes, 100 is NOT present in list')
else:
    print('NO, 100 is Present in the list')

print()
tup1 = ('a', 'b', 'c')

if 'a' in tup1:
    print('Yes a is present in tuple')