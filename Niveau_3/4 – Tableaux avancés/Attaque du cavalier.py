def blanc(liste) :
    for i in range(len(liste)) :
        for j in range(len(liste[i])) :
            if liste[i][j]=="C" :
                for h in range(len(liste)) :
                    for k in range(len(liste[h])) :
                        if liste[h][k].islower() :
                            if (i-2==h and j+1==k) or (i-1==h and j+2==k) or (i+1==h and j+2==k) or (i+2==h and j+1==k) or (i-2==h and j-1==k) or (i-1==h and j-2==k) or (i+1==h and j-2==k) or (i+2==h and j-1==k) :
                                return True
liste=[input() for i in range(8)]
print("yes" if blanc(liste) else "no")