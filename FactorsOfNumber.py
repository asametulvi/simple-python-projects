while True:
    number = eval(input("enter the number whose factors you want to find? - "))

    print("\nmultipliers of '{number}'".format(number=number))

    for i in range (1, number+1):
        if number%i == 0:
            print (i)
    print("\n")