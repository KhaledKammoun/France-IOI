#include <stdio.h>
void fonction(int n)
{
    if(n==0){
        printf("%c",'0') ;
        return ;
    }
    printf("%c",'(') ;
    fonction(n-1) ;
    printf("%s"," + ");
    fonction(n-1);
    printf("%c",')');
}
int main ()
{
    int n;
    scanf("%d",&n) ;
    printf("0 = ") ;
    fonction(n) ;
    return 0 ;
}