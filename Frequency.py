#count the occurences of a substring (here b) in a string(here a)
a=input("Enter the string")
b=input("Enter the character whose frequency is to be found")
for i in range(0,len(a)):
    count=a.count(b)
print(count)
