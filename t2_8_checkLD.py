# Write a program that accepts a string as an input from the user and calculates the number of digits and letters.
# Expected output: consul12 ; Letters 6 ; Digits 2

user_string = input ("Enter a string : ")

letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ"
digit = "0123456789"
le=dg="" 

for i in user_string:
    if i in letter:
        le=le+i
    elif i in digit:
        dg=dg+i

print (user_string)    
print ("Letters ",len(le))
print ("Digits ",len(dg))    

# new programe with sam euser input
l=d=""
for i in user_string:
    if i.isalpha() == True: l=l+i
    elif i.isdigit() == True: d=d+i
print (user_string, "Letters: ",len(l), " Digits: ",len(d))
