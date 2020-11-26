#include <stdio.h>

int    main(void)
{
    int x, y;
    int i = 1;
    int index;
    
    scanf("%d", &index);
    while (i <= index)
    {
        scanf("%d %d", &x, &y);
        printf("Case #%d: %d + %d = %d\n", i, x, y, x + y);
        i++;
    }
    return (0);
}
