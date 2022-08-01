#prgm to find largest among three numbers
a=int(input("enter the first value"))
b=int(input("enter the second value"))
c=int(input("enter the third value"))
if(a>b and b>c):
    print(a, "largest of three numbers")
elif(b>c):
    print(b, "largest of three number")
else:
    print(c, "largest of three number")