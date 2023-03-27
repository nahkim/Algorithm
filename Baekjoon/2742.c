#include <stdio.h>

int main(void)
{
    int num;
    
    scanf("%d", &num);
    for (num; num > 0; num--)
        printf("%d\n", num);
    return (0);
}
