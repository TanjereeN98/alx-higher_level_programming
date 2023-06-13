#include "lists.h"
/**
 * listint_len - length of linked list
 * @h: head of the list
 * Return: length of a list
 */
size_t list_len(const listint_t *h)
{
	const listint_t *p;
	int counter = 0;

	p = h;
	while (p)
	{
		counter++;
		p = p->next;
	}
	return (counter);
}

/**
 * is_palindrome -  checks if a singly linked list is a palindrome
 * @head: head of the list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	int x, y, len, sig = 1
	listint_t *current = *head;
	int ints[1024] = {0};

	if (*head == NULL)
		return (sig);
	len = list_len(*head);
	for (x = 0 ; x < len ; x++)
	{
		ints[x] = current->n;
		current = current->next;
	}
	for (x = 0, y = len - 1 ; y > x && x < len ; x++, y--)
	{
		if (arr[x] != arr[y])
			sig = 0;
	}
	return (sig);
}
