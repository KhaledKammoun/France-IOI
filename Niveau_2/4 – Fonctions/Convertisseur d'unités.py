from math import *
n=int(input())
for i in range(n) :
    ch=input()
    a=ch.find(" ")
    nb=float(ch[:a])
    nch=ch[a+1:]
    if nch=="m" :
        print(round(nb/0.3048,6),"p")
       
    
    
    elif nch=="g" :
        print(round(nb*0.002205,6),"l")
        
    else :
        print(float(round(32 + (1.8*nb),6)),"f")