# What is the output of the following code examples?

'''
# TypeError: 'int' object is not iterable
x = 123
for i in x: # x has to be list or range to get it iterable 
    print(i)
'''

'''
# in this code i value is 0, loop till i is 5 or breaking of loop prints i, add 1 to i, break a loop once i = 3
# output: 0, error, 1, error, 2
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
'''

'''
# output 0 to 4 and error once enters in if condition
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        Break # NameError: name 'Break' is not defined
...