liste=[]
for i in range(int(input())) :
    nb,date=map(int,input().split())
    if nb>0 :
        liste+=[date for c in range(nb)]
    else :
        liste=liste[:len(liste)+nb]
print(min(liste))