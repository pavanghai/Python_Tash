'''
Read the two parts of the question below: 

Write a program such that it asks users to “guess the lucky number”. 
If the correct number is guessed the program stops, otherwise it continues forever. 

Modify the program so that it asks users whether they want to guess again each time. 
Use two variables, ‘number’ for the number and ‘answer’ for the answer to the 
question of whether they want to continue guessing. The program stops if the user 
guesses the correct number or answers “no”. ( The program continues as long as a 
user has not answered “no” and has not guessed the correct number)
'''
msg = '''
This program continues working till 
the user guess correct number
from 0-10 or enters 'NO' to stop program
are you ready ?'''
print (msg)
user_guess = int(input("Guess a number between 0 to 10 :"))
guess = 