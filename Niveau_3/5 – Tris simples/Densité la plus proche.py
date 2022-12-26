def test(quation,i,j) :
    global liste
    val_1=liste[i]
    val_2=liste[j]
    if i ==j :
        return val_1
    if i+1==j :
        if quation -val_1<=val_2-quation  :
            return val_1
        else :
            return val_2
    m=(i+j)//2
    if quation <=liste[m] :
        return test(quation,i,m)
    else :
        return test(quation,m,j)
def main()  :
    global liste
    n=int(input())
    liste=[int(i) for i in input().split()]
    liste.sort()
    for i in range(int(input())) :
        quation =int(input())
        print(test(quation,0,n-1))
main()