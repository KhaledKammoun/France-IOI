from math import *
liste=["##","# "]
liste_copy=["##","# "]
n=int(input())
for i in range(int(sqrt(n))) :
    for j in range(len(liste)) :
        liste[j]*=2
    for c in liste_copy : 
        liste.append(c+" "*len(c))
    liste_copy=liste.copy()
    
for i in range(n) :
    print(liste[i][:n-i])