'''
Write a program in Python to break and continue if the following cases occur:
● If a user enters a negative number just break the loop and print “It’s
Over”

● If a user enters a positive number just continue in the loop and print
“Good Going”
'''
msg = int(input('Enter number between -5 & 5 to print its searies : '))
no=0
while no <= 10:
    if msg <=0:
        print ("It's Over ")
        break
    elif msg > 0:
        print (no)
        no = no + 1
        continue

print ("\nGood Going")
    
#     for i in range (msg):
#     if msg <= 0:
#         print ("It's Over ")
#     else:
#         print (i, end = " ")
# print ("\nGood Going")
# print (type(msg), msg)