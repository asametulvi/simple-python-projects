while True:
    while True:
        number = eval (input("which number do you want to query? - "))
        a = number - 1
            
        if number < 2:
            print (" \nplease enter a number which is greater than 1 \n ")
            continue
        elif number == 2:
            print (" \n{number} is a prime number".format(number=number))
            break
        else:
            while a > 1:
                if number%a == 0:
                    print (" \n{number} is not a prime number".format(number=number))
                    break
                else:
                    a = a - 1
                    if a == 1:
                        print (" \n{number} is a prime number ".format(number=number))
            break
    print("\n")