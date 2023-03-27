#include <stdio.h>

int    main(void)
{
    int i;
    
    scanf("%d", &i);
    for (int num = 1; num <= i; num++)
        printf("%d\n", num);
    return (0);
}
