#********List Other Operations********

'INPUT'
list1 = [1, 2, 3, 4, 5, 4, 3, 2, 1]

#********************

'(1.) length'

print(len(list1))

# Output is :9

#*********************

'(2.) Iteration'

for int in list1:
    print(int)

# Output is [10, 20, 30, 40, 50, 60] in Vertically

#*********************

'(3.) Membership'

if 12 in list1:
    print("100 is present in the list")
else:
    print("element is not present in the list")

#OUTPUT : element is not present in list

#*********************

'(4.) Concatenation '

list2 = [20, 40, 60, 80, 100]
list3 = list1 + list2
print(list3)

#OUTPUT : [10, 20, 30, 40, 50, 60, 20, 40, 60, 80, 100]

#***********************

'(5.) Append'

print(list2.append(120))
print(list2)

#Output : [20, 40, 60, 80, 100, 120]

'(6.) Extend'

print(list2.extend([140, 160, 180]))
print(list2)

#Output : [20, 40, 60, 80, 100, 120, 140, 160, 180]

'(7.) Insert'

list2.insert(3, 0)
print(list2)

#Output : [20, 40, 60, 0, 80, 100, 120, 140, 160, 180]

#***********************

'''INPUT'''
X = list1
Y = list2

'(8.) Append'

X.append([-1, -2, -3])
print(X)

#Output : [10, 20, 30, 40, 50, 60, [-1, -2, -3]]

'(9.) Extend'

X.extend(["Darshan"])
print(X)

#Output : [10, 20, 30, 40, 50, 60, [-1, -2, -3], 'Darshan']

#***********************
