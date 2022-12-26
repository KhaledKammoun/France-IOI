n=int(input())
T=[0]*n
for i in range (n) :
    T[i]=int(input())
for i in range(n) :
    m=T.index(min(T))
    print(m)
    T[m]=1001
