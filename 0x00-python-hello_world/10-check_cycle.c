#include "lists.h"
/**
 * check_cycle - check if there is any cycle in the list
 * @list: head of the list
 * Return: 1 if there is a cycle 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *cur = list, *n = list;

	if (!list || !list->next || !list->next->next)
		return (0);
	do
	{
		cur = cur->next;
		n = n->next->next;
		if (cur == n)
			return (1);
	} while (cur && n && cur != n);
	return cur == n;
}
