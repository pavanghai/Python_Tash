# program in Python to implement the given flowchart:
# age>11, yes(printmsg - Check age -- yes/no ) no(print(msg))
age = int (input("Enter you age : "))
if age >= 11:
    print ("You are eligible to see football match.")
    if age <=20 or age >=60:
        print ("Ticket Price is $ 12")
    else:
        print ("Ticket Price is $ 20")
else:
    print ("You are not eligible to buy a ticket.")