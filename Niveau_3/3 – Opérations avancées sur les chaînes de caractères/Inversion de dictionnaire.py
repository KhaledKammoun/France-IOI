n=int(input())
liste=[]
for i in range(n) :
    mot_1,mot_2=map(str,input().split(" "))
    liste.append([mot_1,mot_2])
    liste[i]=list(reversed(liste[i]))
liste.sort()
for c in liste :
    print(' '.join(c))