n=int(input())
T=[0]*n
chan=int(input())
for i in range (n) :
    T[i]=int(input())
for i in range (chan) :
    a=int(input())
    b=int(input())
    v=T[a]
    T[a]=T[b]
    T[b]=v
for i in range(n) :
    print(T[i])

