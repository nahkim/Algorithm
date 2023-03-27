#include <stdio.h>

int    main(void)
{
    int res = 0, i = 0;
    int index;
    char a[101];
    
    scanf("%d", &index);
    getchar();
    scanf("%s", a);
    while (i < index)
    {
        res += a[i] - 48;
        i++;
    }
    printf("%d", res);
    return (0);
}
