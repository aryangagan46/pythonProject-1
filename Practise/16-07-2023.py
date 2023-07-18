"""print even number by using different ways """

" 1st method : for loop with using define function "
def Numbers():

    res = []
    for x in range(5):
        if x % 2 == 0:
            res.append(x)
    print("Even Numbers are: ", res)

Numbers()

print("*******************************************")
" 2nd method : for loop without using define function "

x =  [x for x in range(5) if x % 2 == 0]
print("Even numbers are:", x)

print("*******************************************")
" 3rd method : append with for loop & without using define function "

