n=int(input())
liste=[int(i) for i in input().split()]
liste_1=[]
for i in range(len(liste)) :
    
    c=min(liste)
    a=liste.index(c)
    liste_1.append(liste[a])
    liste.remove(liste[a])
print(" ".join([str(c) for c in liste_1]))