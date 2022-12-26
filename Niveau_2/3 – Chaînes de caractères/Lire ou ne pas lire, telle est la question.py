nb=int(input())
a=0
for i in range(nb) :
    ch=input()
    if len(ch)>a :
        a=len(ch)
        print(ch)