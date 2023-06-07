#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * insert_node - insert node in a sorted way
 * @head: head of the list
 * @number: data of the list
 * Return: pointer to the new node or NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tempo = malloc(sizeof(listint_t));
	listint_t *current;

	if (tempo == NULL)
		return (NULL);
	current = *head;
	tempo->n = number;
	if (current == NULL)
	{
		*head = tempo;
		return (tempo);
	}
	if (current->n > number)
	{
		tempo->next = *head;
		*head = tempo;
		return (tempo);
	}
	while (current->next)
	{
		if (current->next->n > number)
		{
			tempo->next = current->next;
			current->next = tempo;
			return (tempo);
		}
		current = current->next;
	}
	current->next = tempo;
	tempo->next = NULL;
	return (tempo);
}
