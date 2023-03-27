//연결리스트 시간 초과

#include <stdio.h>
#include <stdlib.h>

typedef struct	s_node
{
	struct s_node *next;
	int x;
	int y;
}	t_node;

void	print_node(t_node *cur)
{
	cur = cur->next;
	while (cur != NULL)
	{
		printf("%d %d\n", cur->x, cur->y);
		cur = cur->next;
	}
}

void	insert_node(t_node *target, int x, int y)
{
	t_node *cur;
	t_node *pre;
	t_node	*newnode;
	if ((newnode = (t_node *)malloc(sizeof(t_node))) == NULL)
		return ;
	newnode->x = x;
	newnode->y = y;
	cur = target;
	pre = cur;
	cur = cur->next;
	while (cur != NULL && cur->x < x)
	{
		pre = cur;
		cur = cur->next;
	}
	if (cur == NULL)	// min num, max num
	{
		pre->next = newnode;
		newnode->next = cur;
		return ;
	}
	else if (cur->x > x)		// current node'x > x
	{
		pre->next = newnode;
		newnode->next = cur;
		return ;
	}
	else if (cur->x == x)		// current node'x == x
	{
		if (cur->y > y)			// current node'y > y
		{
			pre->next = newnode;
			newnode->next = cur;
		}
		else if (cur->y < y)	// current node'y < y
		{
			newnode->next = cur->next;
			cur->next = newnode;
		}
		return ;
	}
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
	int index;
	int i = 0;
	int x = 0;
	int y = 0;
	if ((head = (t_node *)malloc(sizeof(t_node))) == NULL)
		return (0);
	head->next = NULL;
	scanf("%d", &index);
	getchar();
	while (i < index)
	{
		scanf("%d %d", &x, &y);
		getchar();
		insert_node(head, x, y);
		i++;
	}
	print_node(head);
	free_node(head);
	return (0);
}
