from time import sleep

while True:

    number = eval(input("how many numbers do you want to add? - "))
    result = 0

    while number >= 1 :
        a = input("")
        number = number-1
        result = result + int(a)
        
    print("calculating total... \n")
    sleep(2)
    print("total of numbers is : {result} \n\n".format(result=result))
