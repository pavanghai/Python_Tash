# Task Two operators and Decision-making statements
# take input from user, check if its divisible by 3, 5 or both
# print msg 
msg = ''' This program is to check if the given number from 
user is divisible by 3, 5 and both and print msg accordingly 
'''
print (msg)
# try_again = 0
num = int(input("Enter a number :" ))
# for try_again == 0:
if num % 3 == 0 and num % 5 == 0:
    print ("Consultadd Python Training")
    # try_again = 1
elif num % 5 == 0:
    print ("c")
    # try_again = 1
elif num % 3 == 0:
    print ('Consultadd')
    # try_again = 1
else:
    print ("you entered", num, "Sorry! its not divisible 😌 " )

