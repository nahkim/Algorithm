#include <stdio.h>
#include <stdlib.h>

int ft_check(int* array, int N)
{
    int count = 0;
    int min = 0;
    int max = N - 1;

    while (0 < N)
    {
        if ((max = ft_find(array, max, N)) != -1)
            N--;
        else
            return (N);
    }
    return (N);
}

// Array Locations of N
int ft_find(int* array, int max, int N)
{
    while (max > 0)
    {
        if (N != array[max])
            max--;
        else
            break;
    }
    if (N == array[max])
        return (max);
    return (-1);
}

int	main(void)
{
    int i = 0;
    int res = 0;
    int N;
    int* array;

    scanf("%d", &N);
    getchar();
    if (!(array = (int*)malloc(sizeof(int) * N)))
        return (NULL);
    while (i < N)
    {
        scanf("%d", &array[i++]);
        getchar();
    }
    res += ft_check(array, N);
    printf("%d", res);
    if (array)
        free(array);
    array = NULL;
    return (0);
}
