#####################

# Slicing:
# -WAP to print last 3 characters of a string(regular order)
# -WAP to print last 3 characters of a string(reverse order)
# -WAP to print a string except last 3 characters(fwd order)
# -WAP to print a string except last 3 characters(reverse order)
# -WAP to reverse a string
# -Take an index and element from user and change the element at index in hardcoded list
# l1=[1,2,3,4,5]
# index=3
# element='ethans'	
# Output --> [1,2,3,'ethans',5]

######################

name=input(str('Enter the name: '))

print('last 3 characters of a string:',name[-3:])
print('last 3 characters of a string in reverse:',name[:-4:-1])
print('except last 3 characters of a string:',name[:-3])
print('except last 3 characters of a string in reverse:',name[-4::-1])
print('reverse string:',name[::-1])

#######################