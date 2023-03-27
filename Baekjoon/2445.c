#include <stdio.h>

int main(void)
{
    int num, i, j, buf, buf2, check;

    scanf("%d", &num);
    j = 2 * num - 1;
    i = 0;
    check = 0;
    buf = num;
    buf2 = num;
    while (j > 0)
    {
        buf = buf2;
        while (buf - num + 1 > 0)
        {
            printf("*");
            buf--;
        }
        i = 0;
        while (i < num - 1)
        {
            printf(" ");
            i++;
        }
        while (i--)
            printf(" ");
        buf = buf2;
        while (buf - num + 1 > 0)
        {
            printf("*");
            buf--;
        }
        printf(" \n");
        j--;
        if (num > 1 && check == 0)
            num--;
        else if (num == 1 && check == 0)
        {
            check = 1;
            num += 1;
        }
        else if (check == 1)
            num++;
    }
    return (0);
}
