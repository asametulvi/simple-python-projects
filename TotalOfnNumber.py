from time import sleep

while True:
    while True:
        number = eval (input ("how many consecutive numbers do you want to sum? - "))
        result = 0    
        if (number <= 1):
            print ("\nenter a number which is greater than 1 \n")
            continue
        else:
            print("enter {number} numbers".format(number=number))
            break
            
    while number >= 1 :
        a = input("")
        number = number-1
        result = result + int(a)
            
    print("calculating total... \n")
    sleep(2)
    print("total of numbers is : {result} \n\n".format(result=result))
