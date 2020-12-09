#include <stdio.h>

int main(void)
{
    int num;
    int i = 0, j, buf = 1;

    scanf("%d", &num);
    while (num > 0)
    {
        i = 0;
        while (i < num - 1)
        {
            printf(" ");
            i++;
        }
        j = 2 * buf - 1;
        while (j > 0)
        {
            printf("*");
            j--;
        }
        printf(" \n");
        buf++;
        num--;
    }
    return (0);
}