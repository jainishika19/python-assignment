# WHO WINS

N = int(input("Number of stones:"))
i = 1  
while True:
    # Ramesh puts i stones
    N=N-i
    if N<=0:
        print("Ramesh")
        break

    # Suresh puts ix2 stones
    N=N-i*i
    if N<=0:
        print("Suresh")
        break

    i+=1