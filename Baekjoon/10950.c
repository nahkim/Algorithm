#include <stdio.h>

int    main(void)
{
    int x, y;
    int index;
    int i = 0;
    
    scanf("%d", &index);
    int array[index];
    while (i < index)
    {
        scanf("%d %d", &x, &y);
        getchar();
        array[i] = x + y;
        i++;
    }
    i = 0;
    while (i < index)
    {
        printf("%d\n", array[i]);
        i++;
    }
    return (0);
}
