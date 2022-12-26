nb_lignes,nb_colonnes=map(int,input().split(" "))
liste=[["."]*nb_colonnes for i in range(nb_lignes)]
for n in range(int(input())) : #nb_rectangles
    iLig1,iCol1,iLig2,iCol2,ch=input().split(" ")
    for i in range(int(iLig1),int(iLig2)+1) :
        for j in range(int(iCol1),int(iCol2)+1) :
            liste[i][j] =ch
for c in liste :
    print(''.join(c))