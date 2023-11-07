while True:
    number = eval(input("enter the number whose factors you want to find? - "))

    if (number < 0):
        for i in range (number, 0):
            if number%i == 0:
                print (i)
    elif (number == 0):
        print("\nthere is no multiplier")
    else:
        print("\nmultipliers of '{number}'".format(number=number))
        
        for i in range (1, number+1):
            if number%i == 0:
                print (i)
    print("\n")