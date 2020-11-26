#include <stdio.h>

int    main(void)
{
    int x, y;
    int index;
    int i = 0;
    scanf("%d", &index);
    while (i < index)
    {
        scanf("%d,%d", &x, &y);
        printf("%d\n", x + y);
        i++;
    }
    return (0);
}
