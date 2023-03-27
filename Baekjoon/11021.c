#include <stdio.h>

int    main(void)
{
    int x, y;
    int index;
    int i = 1;
    
    scanf("%d", &index);
    while (i <= index)
    {
        scanf("%d %d", &x, &y);
        printf("Case #%d: %d\n", i, x + y);
        i++;
    }
    return (0);
}
