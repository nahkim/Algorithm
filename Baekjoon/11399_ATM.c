#include <stdio.h>

int main(void)
{
    int n;
    int p[1000] = {0, };
    int i = 0;
    int res = 0;
    int j;
    int temp;

    scanf("%d", &n);
    getchar();
    while(i < n)
    {
        scanf("%d", &p[i]);
        i++;
    }
    i = 0;
    while (i < n)
    {
        j = i + 1;
        while (j < n)
        {
            if (p[i] > p[j])
            {
                temp = p[i];
                p[i] = p[j];
                p[j] = temp;
            }
            j++;
        }
        i++;
    }
    i = 0;
    while (n > 0)
    {
        res += (p[i] * n);
        i++;
        n--;
    }
    printf("%d", res);
    return (0);
}
