#include <stdio.h>
#include <stdlib.h>

// Whether or not there is a continuous number on the left based on the maximum value.
int ft_check(int* array, int N)
{
    int count = 0;
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
/*
1. 최대값(N)의 배열 위치 찾기
2. 최대값 기준 왼쪽에 연속된 수의 유무
2-1. 연속된 수가 있으면 그 다음 연속된 수(N-1)찾기
2-2. 연속된 수가 없으면 옮겨야할 갯수(N)리턴
*/
