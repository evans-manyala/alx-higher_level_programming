#include "lists.h"

/**
 * find_middle_node - Finds the middle node of a linked list
 * @head: Pointer to the head of the list
 * Return: Pointer to the middle node
 */
listint_t *find_middle_node(listint_t *head)
{
	listint_t *slow = head, *fast = head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	return (slow);
}

/**
 * free_list - Frees a linked list
 * @head: Pointer to the head of the list
 */
void free_list(listint_t *head)
{
	while (head)
	{
		listint_t *next_node = head->next;

		free(head);
		head = next_node;
	}
}

int is_palindrome(listint_t **head)
{
	if (*head == NULL || (*head)->next == NULL)
		return (1);
	listint_t *slow = *head, *fast = *head;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
	}
	listint_t *prev = NULL, *current = slow, *next_node;

	while (current)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	listint_t *first_half = *head;
	listint_t *second_half = prev;

	while (second_half)
	{
		if (first_half->n != second_half->n)
		{
			current = prev;
			prev = NULL;
			while (current)
			{
				next_node = current->next;
				current->next = prev;
				prev = current;
				current = next_node;
			}
			return (0);
		}
		first_half = first_half->next;
		second_half = second_half->next;
	}
	current = prev;
	prev = NULL;
	while (current)
	{
		next_node = current->next;
		current->next = prev;
		prev = current;
		current = next_node;
	}
	return (1);
}
