liste_index=[]
n,m=map(int,input().split())
liste=[int(i) for i in input().split()]
liste_1=[int(i) for i in input().split()]
for c in liste_1 :
    x=0
    for i in range(len(liste)) :
        if c<=liste[i] :
            x=i
            break
        else :
            x=len(liste)
    liste=liste[:x]+[c]+liste[x:]
    liste_index.append(x)
    
for c in liste_index  :
    print(c,end=" ")
print()
for c in liste :
    print(c,end=" ")
print()