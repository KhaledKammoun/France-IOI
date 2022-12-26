a=list(input())
nb_livres=int(input())
for i in range(nb_livres) :
    mots=input().title().split(" ")
    if [mot[0] for mot in mots] == a :  print(' '.join(mots))