#include <stdio.h>

int main(void)
{
    int num, target, i, target1;
    int n, gold, silver, bronze;
    int res = 1;

    scanf("%d %d", &num, &target);
    getchar();
    long long array[num][2];
    for (i = 0; i < num; i++)
    {
        scanf("%d %d %d %d", &n, &gold, &silver, &bronze);
        array[i][0] = n;
        array[i][1] = gold * 1e12 + silver * 1e6 + bronze;
        if (n == target)
            target1 = i;
    }
    for (i = 0; i < num; i++)
    {
        if (array[i][1] > array[target1][1])
            res++;
    }
    printf("%d", res);    // 결과 출력
    return (0);
}
