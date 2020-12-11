#include <stdio.h>

int main(void)
{
    int num, i, j, k = num;
    
    scanf("%d", &num);
    for (i = 0; i < 2 * num - 1; i++)
    {
        for (j = 0; j < num; j++)
        {
            if (j == num - 1)
                printf("*");
            else if (j < num - 1)
            {
                printf (" ");
            }
            else
                printf("*");
        }
        printf("\n");
    }
    return (0);
}
