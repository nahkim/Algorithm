int	ft_cmp(char src, char find)
{
	if (src == find)
		return (1);
	return (0);
}


int find(char *min, char *str)
{
	int res = 0;
	int minlen = ft_strlen(min) - 1;
	int strlen = ft_strlen(str) - 1;
	i = 0;
	j = 0;
	
	while(minlen - (strlen - 1) > i)
	{
		if(ft_cmp(min[i], str[j])
		{
			i++;
			j++;
			if (str[j] == NULL)
			{
				res++;
				j = 0;
			}
		}
		else
			j = 0;
	}
	return (res);
}

int main(void)
{
	int min;
	int max;
	int find;
	
	while (min <= max)
	{
		res += find(min, str);
		min++;
	}
	return (res);
}
