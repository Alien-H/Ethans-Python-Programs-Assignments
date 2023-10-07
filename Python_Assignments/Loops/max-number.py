######################

# -Write a program to find out maximum number in the list

######################

l1=[]
num=int(input('Enter numbers of elements in list:'))
for i in range(1,num+1):
    ele=int(input('Enter elements:'))
    l1.append(ele)
    
print('Largest element is:',max(l1))

######################