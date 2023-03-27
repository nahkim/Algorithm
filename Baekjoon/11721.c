#include <stdio.h>
#include <unistd.h>

int    main(void)
{
    char s[101];
    int i = 0;
    int j = 0;
    
    scanf("%s", s);
    while (s[i] != '\0')
    {
        write(1, &s[i], 1);
        i++;
        j++;
        if (j == 10)
        {
            write(1, "\n", 1);
            j = 0;
        }
    }
    return (0);
}
