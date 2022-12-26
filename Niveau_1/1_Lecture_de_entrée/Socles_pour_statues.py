l=int(input())
lf=int(input())
v=0
while True :
    v=v+(l*l)
    l=l-1
    if l==lf-1 :
        break
print(v)