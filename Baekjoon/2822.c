#include <stdio.h>
#include <stdlib.h>

int *array_score(int *res)
{
    int i = 0;
    int j;
    int tmp;

    while (i < 5)
    {
        j = i + 1;
        while (j < 5)
        {
            if (res[i] > res[j])
            {
                tmp = res[i];
                res[i] = res[j];
                res[j] = tmp;
            }
            j++;
        }
        i++;
    }
    return (res);
}

int *res_num(int *score, int *res)
{
    int i;
    int j = 0;
    int num;
    int max;
    int total = 0;

    while (j < 5)
    {
        max = score[i];
        num = 0;
        i = 0;
        while (i < 8)
        {
            if (max < score[i])
            {
                num = i;
                max = score[i];
            }
            i++;
        }
        res[j] = num + 1;
        total += score[num];
        score[num] = -1;
        j++;
    }
    printf ("%d\n", total);
    array_score(res);
    return (res);
}

int main(void)
{
    int *score;
    int i = 0;
    int total = 0;
    int *res;

    if ((score = (int *)malloc(sizeof(int) * 8)) == NULL)
        return (0);
    if ((res = (int *)malloc(sizeof(int) * 5)) == NULL)
        return (0);
    while (i < 8)
    {
        scanf("%d", &score[i]);
        getchar();
        i++;
    }
    res_num(score, res);
    i = 0;
    while (i < 4)
    {
        printf("%d ", res[i]);
        i++;
    }
    printf("%d", res[i]);
    free (score);
    free (res);
    return (0);
}
