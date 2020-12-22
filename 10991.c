#include <stdio.h>

int main(void)
{
    int num, tmp, idx;

    scanf("%d", &num);
    for (int i = 1; i <= num; i++)
    {
        tmp = num;
        idx = 0;
        while (num - i > idx)
        {
            printf(" ");
            idx++;
        }
        idx = 0;
        while (i > idx)
        {
            printf("* ");
            idx++;
        }
        printf("\n");
    }
    return (0);
}
