total=0
i = 1

while True:
     while True:
          number = eval (input ("how many consecutive numbers do you want to sum? - "))
               
          if (number < 1):
               print ("\nenter a number which is greater than 1 \n")
               continue
          else:
               break
               
     while i <= number:
          total = total + i
          i = i + 1
     print (" \n{total} \n\n".format(total=total))
