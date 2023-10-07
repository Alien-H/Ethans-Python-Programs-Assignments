#####################

# Python program to check given string is Palindrome or not.
# Note : nitin,madam are palindromes and Nitin is not because Python is case sensitive
#####################

string=input('Enter a string:')
if string==string[::-1]:
    print('The string is palindrome')
else:
    print('The string is not palindrome ')

######################