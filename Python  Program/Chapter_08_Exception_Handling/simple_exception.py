

result = 7 / 0
print(result)
print("end of the progrram ")

"""
 same program now we handle with try except i.e except handling so that program does not stop/halt
"""

try:
     result = 7/0
     print(result)

except:
    print("error in division ")

print("end of the program ")