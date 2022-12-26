#include <stdio.h>
void fonction(int n,int nc)
{
    if(nc==0)
    {
        printf("%d",n) ;
        return ;
    }
    printf("%c",'[') ;
    fonction(n,nc-1) ;
    printf("%c",']') ;
}
int main ()
{
    int n,nc ;
    scanf("%d %d",&n,&nc) ;
    fonction(n,nc) ;
    return 0 ;
}