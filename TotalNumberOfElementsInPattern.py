numberofelements = 0

while True:
    x = eval (input(" \n beginning number - "))
    y = eval (input(" \n ending number - "))

    if (x > y):
        print (" \n please enter a number which is x <= y \n ")
        continue
    elif x == y:
        print(" \n there is no element")
        break
    else:
        z = eval (input(" \n increment - "))
        while True:
            while x < y:
                x = x + z
                numberofelements += 1
            if numberofelements == 0:
                print(" \n there is no element ")
                break
            else:
                print(" \n {numberofelements}".format(numberofelements=numberofelements))
                print(" \n ''Answer includes only ending number''")
                break
        break