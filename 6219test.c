//time out

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int digit_count(int n)
{
    int i = 1;

    while (n >= 10)
    {
        i++;
        n /= 10;
    }
    return (i);
}

char *ft_itoa(int n)
{
    int len;
    char *str;

    len = digit_count(n);
    str = (char *)malloc(sizeof(char) * len + 1);
    str[len] = '\0';
    while (len-- > 0)
    {
        str[len] = n % 10 + '0';
        n = n / 10;
    }
    return (str);
}

int ft_count(int *str)
{
    int i = 0;
    while (str[i] != 0)
        i++;
    return (i);
}

int isprime(int n)
{
	int i = 2;

	while (i < n)
	{
		if (n % i != 0)
			i++;
		else
			return (0);
	}
	if (n == 1)
		return (0);
	return (1);
}

int ft_find(char *min, char *find)
{
    int res = 0;
    int i = 0;
    int j = 0;

    while (min[i])
    {
        if (min[i] == find[j])
        {
            j++;
            if (!find[j])
            {
                j = 0;
                res++;
            }
        }
        else
        {
            j = 0;
        }
        i++;
    }
    return (res);
}

int main(void)
{
    int min;
    int max;
    int find;
    int save[400000] = {0,};
    int i = 0;
    int res = 0;
    int count = 0;
    char *src;
    char *dest;

    scanf("%d %d %d", &min, &max, &find);
    while (max - min >= 0)
    {
        if (isprime(min))
        {
            save[i] = min;
            //printf("prime : %d\n", save[i]);
            i++;    
        }
        min++;
    }
    count = ft_count(save);
    i = 0;
    dest = ft_itoa(find);
    while (i < count)
    {
        src = ft_itoa(save[i]);
        res += ft_find(src, dest);
        i++;
        free(src);
    }
    printf("%d", res);
    free(dest);
    return (0);
}
