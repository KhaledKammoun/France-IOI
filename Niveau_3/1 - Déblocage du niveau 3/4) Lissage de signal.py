# import sys
# n = 7
# diffMax = 1.120
n = int(input())
diffMax = float(input())
# l1 = [float(input()) for i in range(n)]
l1 = []
for i in range(n):
    l1.append(float(input()))
# l1 = [1.292, 1.343, 3.322, 4.789, -0.782, 7.313, 4.212]
# l1 = [*map(float, [e for e in sys.stdin])]
l2 = l1[:]
def diffTest(l, diffMax):
    for i in range(len(l)-1):
        if abs(l[i]-l[i+1]) > diffMax:
            return True
    return False
e = 0
while diffTest(l1, diffMax):
    for i in range(1,n-1):
        l2[i] = (l1[i-1] + l1[i+1])/2
    l1=l2[:]
    e+=1
print(e)
###################
###  2°méthode  ###
###################
nbValeurs = int(input())
seuil = float(input())
valeurs = [float(input()) for loop in range(nbValeurs)]
temp = [0.0] * nbValeurs
def lisse():
   for valeur in range(1,nbValeurs):
      if abs( valeurs[valeur] - valeurs[valeur-1] ) > seuil:
         return False
   return True
nbTours = 0
while not lisse():
   nbTours = nbTours + 1
   for valeur in range(1,nbValeurs - 1):
      temp[valeur] = (valeurs[valeur - 1] + valeurs[valeur + 1]) / 2
   for valeur in range(1,nbValeurs - 1):
      valeurs[valeur] = temp[valeur]
      
print(nbTours)