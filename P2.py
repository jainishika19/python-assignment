#MAXIMUM OF THREE NUMBERS
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if a>=b and a>=c:
   greatest = a
elif b>=c and b>=a:
   greatest =b
else:
   greatest =c
print("the greatest number is:",greatest)
