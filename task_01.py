# Task 1.1 : 3 variables with data type as int, float & string in same line
int_v,flo_v,str_v = 50, 25.50, 'String data'

# Task 1.2 : variable with complex number and swap with int
com_v,int_v1  = 5j, 5 # unable to understand question well

# Task 1.4 : print value given by user in both version
user_value = eval(input("Enter value : "))
print (f"You entered :  {user_value} ")

#Task 1.5a: ask 2 number between 1-10 and add them in z
num1 = eval(input("Enter 1st number between 1-10 : "))
num2 = eval(input("Enter 2nd number between 1-10 : "))
z = num1+num2

#Task 1.5b : add 30 to z and print
print (f"value of z is {z} and + 30 is {z+30}  !")

# Task 1.3 : swap 2 numbers using and without using  the 3rd variable 

# temp = num1
# num1 = num2
# num2 = temp
print (f"1st value is {num1} and 2nd value is {num2} before swap")
num1, num2 = num2,num1
print (f"After swap 1st value is {num1} and 2nd value is {num2} ")

# Task 1.6 : check input datatype
check_type = eval(input("Enter something to check its data type: "))
print (f"you entered {check_type} and its daa type is {type(check_type)}")

# Task 1.7 
'''
If one data type value is assigned to ‘a’ variable and 
then a different data type value is assigned to ‘a’ again. 
Will it change the value. If Yes then Why? 
Yes: as 'a' is a variable and its pointing to a value which is stored in memory, 
when we reassign a different value to it, it points to a new value 
'''




