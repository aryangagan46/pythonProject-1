# if else condition

a = 4

if a > 38:
    print(" Condition matches")
else:
    print(" condition does'nt match")
print(" if else condtion complets")

# for loop

# sum of first five natural numbers 1+2+3+4+5=15

obj = (1, 2, 3, 4, 5)

for i in obj:
    print(i+2)


# sum of First five natural number

summation = 0

for j in range(1, 6):
    summation = summation + j
print(summation)

print ("*****************************************")
#jump index
for k in range(1, 6, 2):
    print(k)

print ("*****************************************")
#without initial no.
for m in range(10):
    print(m)

print ("*****************************************")

#while loop

it = 4

while it>1:
    print(it)
    it = it -1

print ("*****************************************")

it = 5

while it>1:
    if it != 3:
        print(it)
    it = it -1

print ("*****************************************")

it = 10

while it>1:
    if it == 3:
        break
    print(it)
    it = it -1

print ("*****************************************")

it = 10

while it>1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break
    print(it)
    it = it - 1

print ("*****************************************")

