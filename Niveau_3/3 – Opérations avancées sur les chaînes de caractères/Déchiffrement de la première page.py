ch,ch1=input(),input()#qwertyuiopasdfghjklzxcvbnm      #Xiyqigd !
liste=[]
for c in ch1 :
    if "A"<=c<="Z" :
        liste.append(ch[ord(c.upper())-65].upper())
    elif "a"<=c<="z" :
        liste.append(ch[ord(c.upper())-65].lower())
    else :
        liste.append(c)
print(''.join(liste))