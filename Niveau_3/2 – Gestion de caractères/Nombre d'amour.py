name_1,name_2=map(str,input().split(" "))
liste,liste1=[name_1,name_2],[0]*2
a=0
for c in liste :
    for i in range(len(c)) :
        liste1[a]+=ord(c[i])-65
    a+=1
for j in range(2) :
    while liste1[j] >=10 :
        b=str(liste1[j])
        liste1[j]=0
        for i in range(len(b)) :
            liste1[j]+=int(b[i])
print(liste1[0],liste1[1])