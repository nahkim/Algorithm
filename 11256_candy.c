#include <stdio.h>

int *ft_descending(int array[])		// 내림차순으로 정렬
{
    int i, j, tmp;

    j = 0;
    while (array[j])
    {
        i = 0;
        while (array[i + 1])
        {
            if (array[i] < array[i + 1])
            {
                tmp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = tmp;
            }
            i++;
        }
        j++;
    }
    return (array);
}

int main(void)
{
    int T, j, N, x, y, res, i;

    scanf("%d", &T);
    getchar();
    while (T--)					// 케이스 T 만큼 반복
    {
        scanf("%d %d", &j, &N);
        getchar();
        int array[N];
        res = 0;
        for (i = 0; i < N; i++)		// 사탕의 갯수 * 상자의 개수 배열에 넣음
        {
            scanf("%d %d", &x, &y);
            array[i] = x * y;
            getchar();
        }
        array[i] = '\0';
        ft_descending(array);		// 내림차순 정렬
        i = 0;
        while (j > 0)				// 보낼 사탕의 개수가 0이상일때까지 (사탕 수 * 상자 수)가 큰 순으로 뺌
        {
            j -= array[i];
            i++;
            res++;
        }
        printf("%d\n", res);
    }
    return (0);
}
