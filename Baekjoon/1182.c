#include <stdio.h>

int	main(void)
{
	int N;
	int S;
	int count = 0;
	int *array;
	int i = 0;
	int input;
	scanf("%d %d", &N, &S);
	getchar();
	if (!(N >= 1 && N <= 20))
		return;
	if (!(array = (int*)malloc(sizeof(int) * N)))
		return (0);
	while (i < N)
	{
		scanf("%d", &array[i++]);
		getchar();
	}
	i = 0;
	while (array[i] > 0)
	{
		i++;
	}
}
