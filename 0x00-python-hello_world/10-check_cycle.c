#include "lists.h"
/**
 * check_cycle - check if there is any cycle in the list
 * @list: head of the list
 * Return: 1 if there is a cycle 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *cur = list, *n = list;

	if (!list)
		return (0);
	while (cur && n && cur->next)
	{
		cur = cur->next;
		n = n->next->next;
		if (cur == n)
			return (1);
	}
	return (0);
}
