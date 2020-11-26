//2차원 배열 시간

#include <stdio.h>
#include <stdlib.h>

void	print_array(int *array[], int index)
{
	for (int i = 0; i < index; i++)
	{
		printf("%d %d\n", array[i][0], array[i][1]);
	}
}

int	**sort_array(int *array[], int index)
{
	int i = 0;
	int j;
	int tmp;
	while (i < index - 1)
	{
		j = i + 1;
		while (j < index)
		{
			if (array[i][0] > array[j][0])
			{
				tmp = array[i][0];
				array[i][0] = array[j][0];
				array[j][0] = tmp;
				tmp = array[i][1];
				array[i][1] = array[j][1];
				array[j][1] = tmp;
			}
			else if (array[i][0] == array[j][0])
			{
				if (array[i][1] > array[j][1])
				{
					tmp = array[i][0];
					array[i][0] = array[j][0];
					array[j][0] = tmp;
					tmp = array[i][1];
					array[i][1] = array[j][1];
					array[j][1] = tmp;
				}
			}
			j++;
		}
		i++;
	}
	return (array);
}

int	*insert(int	array[], int x, int y)
{
	array[0] = x;
	array[1] = y;
	return (array);
 }

int	main(void)
{
	int index;
	int i = 0;
	int x = 0;
	int y = 0;
	scanf("%d", &index);
	getchar();
	int	**array;
	if ((array = (int **)malloc(sizeof(int*) * index)) == NULL)
		return (0);
	for (i = 0; i < index; i++)
	{
		if ((array[i] = (int *)malloc(sizeof(int) * 2)) == NULL)
			return (0);
	}
	i = 0;
	while (i < index)
	{
		scanf("%d %d", &x, &y);
		getchar();
		array[i] = insert(array[i], x, y);
		i++;
	}
	array = sort_array(array, index);
	print_array(array, index);
	for (i = 0; i < index; i++)
	{
		free (array[i]);
	}
	free (array);
	return (0);
}
