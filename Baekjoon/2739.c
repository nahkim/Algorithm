#include <stdio.h>

int main(void)
{
    int num;
    int i = 1;
    
    scanf("%d", &num);
    for (i; i < 10; i++)
        printf("%d * %d = %d\n", num, i, num * i);
    return (0);
}
