#include <stdio.h>

int main(void)
{
    int num;
    int i = 0;
    
    scanf("%d", &num);
    while (num > 0)
    {
        i = 0;
        while (i < num)
        {
            printf("*");
            i++;
        }
        printf(" \n");
        num--;
    }
    return (0);
}
