n = nbLettres = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"
lignes=[[alphabet[0]]*(n*2-1)]
for i in range(1,n) :
    ligne=lignes[i-1][:]
    for j in range(i,n*2-1-i) :
        ligne[j]=alphabet[i]
    lignes.append(ligne)
for i in range(n) :
   print(''.join(lignes[i]))
for i in range(n-2,-1,-1) :
    print(''.join(lignes[i]))