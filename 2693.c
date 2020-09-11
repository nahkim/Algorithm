#include <stdio.h>
#include <stdlib.h>

int main()
{
	int* array;
	int count;
	int i = 0;
	int j = 1;
	int k = 0;
	int temp;
	int* res;

	scanf("%d", &count);
	getchar();
	if (!(res = (int*)calloc(count, sizeof(int))))
		return (NULL);
	while (k < count)
	{
		if (!(array = (int*)calloc(10, sizeof(int))))
			return (NULL);
		i = 0;
		while (i < 10)
		{
			scanf("%d", &array[i++]);
			getchar();
		}
		i = 0;
		while (i < 9)
		{
			j = i + 1;
			while (j < 10)
			{
				if (array[i] > array[j])
				{
					temp = array[i];
					array[i] = array[j];
					array[j] = temp;
				}
				j++;
			}
			i++;
		}
		res[k++] = array[7];
		free(array);
	}
	k = 0;
	while (k < count)
		printf("%d\n", res[k++]);
	free(res);
	return (0);
}