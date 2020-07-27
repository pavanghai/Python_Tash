# 1.Create a list of the 10 elements of four different types of Data Types like int, string, complex, and float.
t_wa01_list = [2, 'numbers',10j, 5.5, 'from', 10 , 20, 30.5, 20.5, 50j]
print (t_wa01_list)
for i in t_wa01_list: print (type(i),end = " is type & its Value is ") ; print (i)

# 2. Create a list of size 5 and execute the slicing structure
t_wa02_list = range(10,51,10) # this will not store the value of range, but just the command
print (t_wa02_list)
t_wa02_list = list(t_wa02_list)

print (t_wa02_list, ": full list without indexing")
print (t_wa02_list[:], ": full list using blank index")
print (t_wa02_list[1:3], ": list using start and end index")
print (t_wa02_list[::2], ": full list using blank index, skiping 1 value")