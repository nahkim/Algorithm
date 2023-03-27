#include <stdio.h>

int    main(void)
{
    int index;
    int min;
    int max;
    int i = 0;
    
    scanf("%d", &index);
    int array[index];
    while (i < index)
    {
        scanf("%d ", &array[i]);
        i++;
    }
    i = 0;
    min = array[i];
    max = array[i];
    i++;
    while (i < index)
    {
        if (min > array[i])
            min = array[i];
        if (max < array[i])
            max = array[i];
        i++;
    }
    printf("%d %d", min, max);
    return (0);
}
