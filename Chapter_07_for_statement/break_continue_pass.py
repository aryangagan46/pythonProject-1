"""
break
continue
pass
"""
print("break")
for i in range(5):
    if i == 3:
        break
    print(i)

print("\ncontinue")
for i in range(5):
    if i == 3:
        continue
    print(i)

print("\npass")
for i  in range(5):
    if i == 3:
        pass
    print(i)
