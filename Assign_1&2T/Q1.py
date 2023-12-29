n = int(input("Enter the value of n  : "))
k=0
for i in range(n,0,-1):
    a=i
    for j in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print(a, end=" ")
    print()