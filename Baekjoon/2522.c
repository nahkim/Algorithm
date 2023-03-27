#include <stdio.h>

int main(void)
{
    int num;
    int i = 0, tmp, idx;
    scanf("%d", &num);
    for (i = 1; i <= 2 * num - 1; i++)
    {
        idx = 0;
        tmp = num;
        if (i <= num)
        {
            while (idx++ < tmp - i)
                printf(" ");
            while(tmp++ < num + i)
                printf("*");
        }
        else
        {
            while (idx++ < i - num)
                printf(" ");
            while (tmp - idx >= 0)
            {
                printf("*");
                idx++;
            }
        }
        printf("\n");
    }
    return (0);
}
