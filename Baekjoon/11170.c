#include <stdio.h>
#include <stdlib.h>

int ft_strlen(char *str)
{
    int count;

    count = 0;
    while (str[count] != '\0')
        count++;
    return (count);
}

int digit_count(int n)
{
    int res;

    res = 1;
    while (n > 9)
    {
        res++;
        n = n / 10;
    }
    return (res);
}

char *ft_itoa(int num)
{
    char *res;
    int len = digit_count(num);

    res = (char *)malloc(sizeof(char) * (len + 1));
    res[len] = '\0';
    while (len--)
    {
        res[len] = num % 10 + '0';
        num = num / 10;
    }
    return (res);
}

int ft_cal(int min, int max)
{
    int res = 0;

    for (min;min <= max;min++)
    {
        char *char_num = ft_itoa(min);
        int len = ft_strlen(char_num);
        int i = 0;
        while (i < len)
        {
            if (char_num[i] == '0')
                res++;
            i++;
        }
        free (char_num);
    }
    return (res);
}

int main(void)
{
    int num, min, max;
    int i = 0, res = 0;;

    scanf("%d", &num);
    getchar();
    while (i < num)
    {
        res = 0;
        scanf("%d %d", &min, &max);
        getchar();
        res += ft_cal(min, max);
        i++;
        printf("%d\n", res);
    }
    return (0);
}
