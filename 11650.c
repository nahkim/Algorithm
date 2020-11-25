#include <stdio.h>
#include <stdlib.h>


typedef struct	s_node
{
	struct s_node *next;
	int x;
	int y;
}	t_node;

void	Ascending_array(t_node *head)
{
	t_node *cur;
	t_node *tmp;
	int	check = 1;

	//cur = head->next;
	while (check > 0)
	{
		check = 0;
		cur = head->next;
		printf("kkkkkk\n");
		printf("check %d\n", check);
		printf("cur x : %d, cur->next x: %d\n", cur->x, cur->next->x);
		while (cur->next != NULL)
		{
			printf("eeeeee\n");
			printf("cur x : %d, cur->next x: %d\n", cur->x, cur->next->x);
			if (cur->x > cur->next->x)
			{
				//
				tmp = cur->next;
				cur = cur->next->next;
				tmp->next = head->next;
				head->next = tmp;
				check += 1;
			}
			else if (cur->x == cur->next->x)
			{
				if (cur->y > cur->next->y)
				{
					//
					check += 1;
				}
				else
				{
					cur = cur->next;
					check += 0;
				}
			}
			else
			{
				cur = cur->next;
				check += 0;
			}
			printf("check %d\n", check);
			printf("cur %p\n", cur);
		}
	}
}

void	print_node(t_node *cur)
{
	cur = cur->next;
	while (cur != NULL)
	{
		printf("%d %d\n", cur->x, cur->y);
		cur = cur->next;
	}
}

void	add_node(t_node *target, int x, int y)
{
	t_node	*newnode;
	if ((newnode = (t_node *)malloc(sizeof(t_node))) == NULL)
		return ;
	newnode->x = x;
	newnode->y = y;
	newnode->next = target->next;
	target->next = newnode;
	//return (newnode);
}

void	free_node(t_node *target)
{
	t_node *next;
	while (target != NULL)
	{
		next = target->next;
		free(target);
		target = next;
	}
}

int	main(void)
{
	t_node	*head;
	//t_node	*cur;
	int index;
	int i = 0;
	int x = 0;
	int y = 0;
	
	if ((head = (t_node *)malloc(sizeof(t_node))) == NULL)
		return (0);
	head->next = NULL;
	//if ((cur = (t_node *)malloc(sizeof(t_node))) == NULL)
	//	return (0);
	//cur = head->next;
	scanf("%d", &index);
	getchar();
	while (i < index)
	{
		scanf("%d %d", &x, &y);
		getchar();
		add_node(head, x, y);
		i++;
	}
	Ascending_array(head);
	print_node(head);
	free_node(head);
	/*
	while(1)
	{
		;
	}
	*/
	return (0);
}
