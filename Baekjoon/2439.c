#include <stdio.h>

int    main(void)
{
    int num;
    int i = 1, j;
    int buf;
    scanf("%d", &num);
    buf = num;
    while (num)
    {
        i = 1;
        j = 0;
        while (i < num)
        {
            printf(" ");
            i++;
        }
        while (buf - i + 1 > 0)
        {
            printf("*");
            i++;
        }
        printf("\n");
        num--;
    }
    return (0);
}
