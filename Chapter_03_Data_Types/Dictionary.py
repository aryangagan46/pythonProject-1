dict = {'Darshan':30,'Prajwal':28,'Arbaz':27}

print(dict)
print(type(dict))


for key,value in dict.items():
    print("%s %s" %(key, value))

for key in dict.keys():
    print(key)

for value in dict.values():
    print(value)

#Upate in Dictionary

dict['key0'] = 12
print(dict)

print()
