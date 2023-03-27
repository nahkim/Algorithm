#include <stdio.h>

int    main(void)
{
    int num;
    int i = 0;
    int j = 0;
    
    scanf("%d", &num);
    while (i < num)
    {
        j = 0;
        while (j <= i)
        {
            printf("*");
            j++;
        }
        printf("\n");
        i++;
    }
    return (0);
}
