#GCD and LCM
T=int(input("enter no of testcase:"))

for i in range(T):
    x=int(input("enter 1st number:"))
    y=int(input("enter 2nd number:"))
    a=x
    b=y
    while b!=0:
        remainder=a%b
        a=b
        b=remainder
    gcd=a

    lcm=(x*y)//gcd
    print("LCM=",lcm)
    print("GCD=",gcd)
