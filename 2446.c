#include <stdio.h>

int    main(void)
{
    int num, tmp, i, idx;
    
    scanf("%d", &num);
    tmp = num;
    for(i = 0; i < 2 * num - 1; i++)
    {
        idx = 0;
        if (i < num)
        {
            while (i - idx)
            {
                printf(" ");
                idx++;
            }
            idx = 0;
            while (idx < 2 * tmp - 1)
            {
                printf("*");
                idx++;
            }
            printf("\n");
            tmp--;
        }
        else
        {
            if (tmp == 0)
                tmp = 2;
            idx = i;
            while(2 * num - 1 - idx > 1)
            {
                printf(" ");
                idx++;
            }
            idx = 0;
            while(idx < 2 * tmp - 1)
            {
                printf("*");
                idx++;
            }
            printf("\n");
            tmp++;
        }
    }
    return (0);
}
