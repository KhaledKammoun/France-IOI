nbLivres,nbJours = map(int,input().split(" "))
bibli = [0]*nbLivres
for i in range(nbJours):
    nbClients = int(input())
    for i in range(nbClients):
        indice, duree = map(int, input().split(" "))
        if bibli[indice]==0: #livre libre
            bibli[indice] = duree
            print(1)
        else: #libre oqp
            print(0)
    bibli = [max(duree-1, 0) for duree in bibli] #Jour suivant