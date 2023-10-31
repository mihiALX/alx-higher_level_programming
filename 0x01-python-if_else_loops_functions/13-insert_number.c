#include "lists.h"

/**
 * insert_node - Inserts a value into a sorted singly-linked list.
 * @pointer: A pointer the pointer of the linked list.
 * @value: The value to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **pointer, int value)
{
	listint_t *node = *pointer, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = value;

	if (node == NULL || node->n >= value)
	{
		new->next = node;
		*pointer = new;
		return (new);
	}

	while (node && node->next && node->next->n < value)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
