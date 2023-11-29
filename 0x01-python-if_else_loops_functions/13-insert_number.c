#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: a pointer to the head node
 * @number: the number to insert
 *
 * Return: the address of the new node on success, else NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev, *curr;

	new_node = malloc(sizeof(listint_t));

	if (!new_node)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head)
	{
		*head = new_node;
		return (new_node);
	}

	prev = NULL;
	curr = *head;

	while (curr && curr->n < number)
	{
		prev = curr;
		curr = curr->next;
	}

	if (!prev)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		prev->next = new_node;
		new_node->next = curr;
	}

	return (new_node);
}
