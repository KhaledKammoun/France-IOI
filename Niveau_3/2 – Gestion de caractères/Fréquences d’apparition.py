ch,ch1=input().lower(),"abcdefghijklmnopqrstuvwxyz"
b=0
for i in range(len(ch)) :
    if "a"<=ch[i]<="z" :    b+=1
for i in range(len(ch1)) :  print(format(ch.count(ch1[i])/b,".6f"))