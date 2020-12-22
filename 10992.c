#include <stdio.h>

int main(void)
{
    int num, tmp;

    scanf("%d", &num);      // 입력 값 저장
    for (int i = 1; i <= num; i++)
    {
        tmp = 0;
        if (i == 1)         // 맨 첫번째 줄 출력
        {
            while (num - i > tmp)
            {
                printf(" ");
                tmp++;
            }
            printf("*");
        }
        else if (i != num)      // 중간 줄들 출력
        {
            while (num - i > tmp)
            {
                printf(" ");
                tmp++;
            }
            printf("*");
            tmp = 0;
            while (2 * (i - 1) - 1 > tmp)
            {
                printf(" ");
                tmp++;
            }
            printf("*");
        }
        else                // 맨 마지막 줄 출력
        {
            while (2 * i - 1 > tmp)
            {
                printf("*");
                tmp++;
            }
        }
        printf("\n");
    }
    return (0);
}
