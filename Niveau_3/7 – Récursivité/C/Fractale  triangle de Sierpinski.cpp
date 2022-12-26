#include <stdio.h>
#include <stdbool.h>
bool tab[64][64] ;
void triangle(int n,int x , int y)
{
    if (n==1)
    {
        tab[x][y]=true ;
        return ;
    }
    triangle(n/2,x,y) ;
    triangle(n/2,x+n/2,y) ;
    triangle(n/2,x,y+n/2) ;
}
int main ()
{
    int n ;
    scanf("%d",&n) ;
    int x=0,y=0 ;
    triangle(n,x,y) ;
    for (int i=0 ; i<n;i++)
    {
        for (int j=0 ;j<n;j++)
        {
            if (tab[i][j])
                printf("%c",'#') ;
            else
                printf("%c",' ') ;
        }
        printf("\n") ;
    }
}