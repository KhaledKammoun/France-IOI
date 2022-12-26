n=int(input())
T=[0]*n
for i in range (n) :
    T[i]=int(input())
for i in range(n-1,-1,-1) :
    if T[i]==1 :
        print("2")
    if T[i]==2 :
        print("1")
    if T[i]==5 :
        print("4")
    if T[i]==4 :
        print("5")
    if T[i]==3 :
        print("3")