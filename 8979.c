#include <stdio.h>

int main(void)
{
    int num, target, i;

    scanf("%d %d", &num, &target);
    getchar();
    int array[num][4];
    int res = 1;
    int n, gold, silver, bronze;


    for (i = 0; i < num; i++)   //각 나라 및 메달 수 저장
    {
        scanf("%d %d %d %d", &array[i][0], &array[i][1], &array[i][2], &array[i][3]);
        getchar();
        if (array[i][0] == target)  // 찾고자하는 나라의 메달 수 저장
        {
            gold = array[i][1];
            silver = array[i][2];
            bronze = array[i][3];
        }
    }
    for (i = 0; i < num; i++)   // 비교
    {
        if (array[i][1] > gold)
            res++;
        else if (array[i][1] == gold && array[i][2] > silver)
            res++;
        else if (array[i][1] == gold && array[i][2] == silver && array[i][3] > bronze)
            res++;
    }
    printf("%d", res);  // 결과 출력
    return (0);
}
