N,M=map(int,input().split())
liste = [int(i) for i in input().split()]
liste.sort()
for i in range(1,M+1) :
    print(liste[-i],end=" ")
print()