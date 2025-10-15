#John and his Series
a=int(input("enter 1st term:"))
d=int(input("enter common diff:"))
n=int(input("enter no.of terms:"))
print("AP is")
for i in range(1,n+1):
    term=a+(i-1)*d
    print(term,end=" ")
nth_term=a=(n-1)*d
print("\nthe nth term of AP is:",nth_term)

