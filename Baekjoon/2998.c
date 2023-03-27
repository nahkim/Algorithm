#include <stdio.h>
#include <stdlib.h>

int ft_numlen(char *num)
{
    int i = 0;

    while (num[i] != '\0')
        i++;
    return (i);
}

// 3자리씩 한그룹을 2진수 -> 8진수 변환
char process(char* num, int i)
{
    int two = 1;
    int save = 0;
    int res = 0;
    int k = 3;

    while (k-- > 0)
    {
        save = 0;
        if (i < 0)
            return (res + '0');
        if (num[i] == '0' || num[i] == '1')
            save += num[i] - '0';
        res += save * two;
        two *= 2;
        i--;
    }
    return (res + '0');
}

int main(void)
{
    char num[101];
    int i = 0;
    char *res;
    int index;

    scanf("%s", num);
    index = ft_numlen(num);
    i = index / 3;
    if (index % 3 > 0)
        i++;
    index--;
    if((res = (char *)malloc(sizeof(char) * (i + 1))) == NULL)
        return (0);
    res[i] = '\0';
    while (i > 0)
    {
        res[i - 1] = process(num, index);
        index -= 3;
        i--;
    }
    printf ("%s", res);
    free (res);
    return (0);
}
