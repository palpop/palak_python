str1=input('Enter the First string: ')
str2=input('Enter the second string: ')

count1=0
i=0
while(i<len(str1)):
    count1=count1+ord(str1[i])
    i=i+1
print(count1)
count2=0
i=0
while(i<len(str2)):
    count2=count2+ord(str2[i])
    i=i+1
print(count2)
if(count1==count2):
    print('Anagram')
else:
    print('Not Anagram')