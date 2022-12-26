n=int(input())
pt1=0
pt2=0
for i in range(n) :
    p1=int(input())
    p2=int(input())
    pt1=pt1+p1
    pt2=pt2+p2
if pt1>pt2 :
    print("L'équipe 1 a un avantage ")
    print("Poids total pour l'équipe 1 : "+str(pt1) )
    print("Poids total pour l'équipe 2 : "+str(pt2) )
else :
    print("L'équipe 2 a un avantage ")
    print("Poids total pour l'équipe 1 : "+str(pt1) )
    print("Poids total pour l'équipe 2 : "+str(pt2) )