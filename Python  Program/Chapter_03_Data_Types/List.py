
list1 = [10,20,30,40,50, 60]

Subject=list1[5]
print(Subject)

Multiple_item=list1[3:5]
print(Multiple_item)

print(list1[5])

#*****Updating List*******
list1[4]=100
print(list1)

#*****Delete list********
del (list1[0])
print(list1)

# nestted list

collection = [1,2,3],[4,5,6],[7,8,9,10]

for list in collection:
    for num in list:
        print("\t",num)

print()
list_mixed = ['10','darshan-',['a','b','c']]

for List1 in list_mixed:
    for Dashboard in List1:
        print(Dashboard)

print()
'''
Integer is not iterable
String is iterable
List is iterable
'''
print()

Name= ({'Darshan'},{'12'},['89.4'])

for List2 in Name:
    for List3 in List2:
        print(List3[1])


