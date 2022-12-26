#include <stdio.h>
void reversed()
{
    char c ;
    scanf("%c",&c) ;
    if (c=='\n')
       return ;
    reversed() ;
    printf("%c",c) ;
}
int main()
{
    reversed() ;
    return 0 ;
}