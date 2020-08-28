#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int n;
	int b;
	int i = 0;
	int j;
	int k = 0;
	int *array;
	int *res;

	scanf("%d", &n);

	while (n > 0)
	{
		scanf("%d", &b);
		array = (int*)malloc(sizeof(int) * b);
		res = (int*)malloc(sizeof(int) * (b - 2));
		for (j = 0; j < b; j++)
		{
			array[j] = (rand() % 99) + 2;
			printf("%d ", array[j]);
		}
		j--;
		printf("\n");
		while (b != 2)
		{
			while (k < (b / 2))
			{
				res[k] = array[k] + array[j];
				k++;
				j--;
			}
			if (b % 2 == 1)
				res[k++] = array[k++] + array[k++];
			free(array);
			if (k != 2)
			{
				array = (int*)malloc(sizeof(int) * (k));
				array = res;
				b = k;
				k = 0;
				free(res);
				res = (int*)malloc(sizeof(int) * (k - 2));
			}
		}
		if (res[0] >= res[1])
			printf("Case #%d: Alice\n", i);
		else
			printf("Case #%d: Bob\n", i);
		i++;
		n--;
	}
	return 0;
}