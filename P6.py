#REVERSE NUMBER
T=int(input("enter no. of testcases:"))

for i in range(T):
    a=int(input("enter 1st number:")) 
    b=int(input("enter 2nd number:"))
    
    #reverse 1st number
    rev1=0
    while a>0:
        rem=a%10
        rev1=rev1*10+rem
        a=a//10
    #reverse 2nd number
    rev2=0 
    while b>0:
        rem=b%10
        rev2=rev2*10+rem
        b=b//10
    #adding both reverse numbers
    sum=rev1+rev2

    #reversing the sum
    rev_sum=0
    while sum>0:
        rem=sum%10
        rev_sum=rev_sum*10+rem
        sum=sum//10
    print("reverse of sum is",rev_sum)

