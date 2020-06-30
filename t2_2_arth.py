# Python to perform the following operator based task:
msg = '''This program calculate arithmetic operations
Enter 1 - Addition 
Enter 2 - Subtraction
Enter 3 - Division
Enter 4 - Multiplication
Enter 5 - Average'''

print (msg)
opra = int (input("Enter Value : "))
if opra not in range (1,6):
    print ("Please enter value between 1 to 5 only")
else:
    n1,n2 = eval(input("Enter two values separated by ',' :"))
    if opra == 1:
        print ("Addition of",n1, "and", n2, "is : ", n1+n2 )
    elif opra == 2:
        print ("Subtraction of",n1, "and", n2, "is : ", n1-n2 )
    elif opra == 3:
        print ("Division of",n1, "and", n2, "is : ", n1/n2 )
    elif opra == 4:
        
        print ("Multiplication of",n1, "and", n2, "is : ", n1*n2 )
    elif opra == 5:
        print ("Average of",n1, "and", n2, "is : ", (n1+n2)/2)
    else:
        print ("Zsa")
    
