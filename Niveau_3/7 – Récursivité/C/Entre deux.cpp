#include <stdio.h>
#include <string.h>
void tuto(int n,int nc)
{
    printf("%d",n) ;
    if (n==nc)
        return;
    printf("%c",' ') ;
    tuto(n+1,nc) ;
}
int main ()
{
    int n,nc ;
    scanf("%d %d",&n,&nc) ;
    tuto(n,nc) ;
    return 0 ;
}