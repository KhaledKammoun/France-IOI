#include <stdio.h>
void tour(int n,int x,int z,int y)
{
    if (n>0)
    {
        tour(n-1,x,y,z) ;
        printf("%d -> %d\n",x,z) ;
        tour(n-1,y,z,x) ;
    }
}
int main()
{
    int n ;
    scanf("%d",&n) ;
    tour(n,1,3,2) ;
    return 0 ;
}