#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct node
{
    char value[20];
    struct node *next;
};

struct node array[20];
int g_index = -1;

void insert(char *v)
{
    g_index++;

    struct node* cur = &array[g_index];
    strcpy(cur->value, (const char *)v);
    cur->next = &array[g_index + 1];
    cur = cur->next;
}

void print()
{
    struct node* cur = &array[0];
	while (cur->next != NULL)
	{
		printf("%s\n", cur->value);
		cur = cur->next;
	}
	printf("%s", cur->value);
}

char ft_uppercase(char (*array)[20], int i, int j)
{
    char c;

    if (array[i][j] >= 'A' && array[i][j] <= 'Z')
        c = array[i][j] + 32;
    else
        c = array[i][j];
    return (c);
}

int ft_compare(char (*save)[20], int res, int i, int j)
{
    char A;
    char B;
    int Alen = strlen(save[res]);
    int Blen = strlen(save[i]);

    while (save[res][j] && save[i][j])
    {
        A = ft_uppercase(save, res, j);
        B = ft_uppercase(save, i, j);
        if (A - B < 0)
            return (res);
        else if (A == B)
            j++;
        else
            return (i);
    }
    if (Alen > Blen)
        return (i);
    else
        return (res);
}

int main(void)
{
   int N;
   int i = 0;
   int j = 0;
   int res = 0;

    scanf("%d", &N);
    getchar ();
    while (1)
    {
        if (N == 0)
            break ;
        char array[N][20];
        for (i = 0; i < N; i++)
        {
            scanf("%s", array[i]);
            getchar();
        }
        i = 1;
        j = 0;
        while (i < N)
        {
            res = ft_compare(array, res, i, j);
            i++;
        }
        insert(array[res]);
        scanf("%d", &N);
        getchar ();
    }
    print();
    return (0); 
}
