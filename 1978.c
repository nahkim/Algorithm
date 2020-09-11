#include <stdio.h>

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
int main()
{
	int* array;
	int count;
	int res = 0;
	int i = 0;

	scanf("%d", &count);
	getchar();
	if (!(array = (int*)malloc(sizeof(int) * count)))
		return (NULL);
	while (i < count)
	{
		scanf("%d", &array[i]);
		getchar();
		if (isprime(array[i]))
			res++;
		i++;
	}
	printf("%d", res);
	return (0);
}