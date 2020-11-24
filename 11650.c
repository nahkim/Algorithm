#include <stdio.h>
#include <stdlib.h>


//typedef struct s_node t_node;
typedef struct	s_node
{
	struct node *next;
	int x;
	int y;
}	t_node;

void	print_node(t_node *cur)
{
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
	t_node	*cur= head->next;
	int index;
	int i = 0;
	int x = 0;
	int y = 0;
	
	if ((head = (t_node *)malloc(sizeof(t_node))) == NULL)
		return (0);
	head->next = NULL;
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
	print_node(head);
	free_node(head);
	return (0);
}
