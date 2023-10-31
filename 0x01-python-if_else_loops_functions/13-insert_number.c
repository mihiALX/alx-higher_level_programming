#include "lists.h"

/**
 * insert_node - Inserts a value into a sorted singly-linked list.
 * @pointer: A pointer to the pointer of the linked list.
 * @value: The value to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **pointer, int value)
{
	listint_t *current = *pointer, *new_node, *prev = NULL;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = value;
	new_node->next = NULL;

	if (*pointer == NULL || (*pointer)->n >= value)
	{
		new_node->next = *pointer;
		*pointer = new_node;
		return (new_node);
	}

	while (current && current->n < value)
	{
		prev = current;
		current = current->next;
	}

	new_node->next = current;
	prev->next = new_node;

	return (new_node);
}
