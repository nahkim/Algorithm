#include <stdio.h>

int ft_check_zero(int num)    // 숫자에 0이 있을 경우 0 반환
{
    int first, second;
    if ((first = num % 1000) == 0 || first <= 100)
      return (0);
    else
    {
      if ((second = first % 100) == 0 || second <= 10)
        return (0);
      else
      {
        if (second % 10 == 0)
          return (0);
        else
          return (1);
      }
    }
}

int ft_min(int min)   // 시계추 방향을 기준으로 제일 작은 수 찾기
{
  int i = 0, tmp = min;
  while (i < 3)
  {
      tmp = (tmp % 1000) * 10 + tmp / 1000;
      if (tmp < min)
          min = tmp;
      i++;
  }
  return (min);
}

int main(void)
{
  int a, b, c, d, min, res = 0;
  scanf ("%d %d %d %d", &a, &b, &c, &d);    // 입력 받기
  getchar();
  min = 1000 * a + 100 * b + 10 * c + d;
  min = ft_min(min);
  for (int i = 1111; i <= min; i++)
  {
      if (ft_check_zero(i) == 0)    // 0이 들어있을 경우 제외시키기
        continue ;
      if (ft_min(i) == i)
        res++;
  }
  printf("%d", res);
  return (0);
}
