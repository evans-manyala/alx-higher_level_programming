#include "lists.h"

/**
 * is_palindrome - Checks if a linked list is a palindrome.
 * @head: Pointer to the head of the list.
 * Return: 1 if palindrome, 0 otherwise.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *next_second_half = *head;
	listint_t *second_half_head = *head, *reversed_current = NULL;
	int is_palindrome = 0, is_odd_length = 0, length = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	for (length = 0; second_half_head->next; second_half_head =
						     second_half_head->next,
	    length++)
		is_odd_length = length % 2 != 0;
	reversed_current = NULL;
	next_second_half = *head;
	second_half_head = *head;

	for (int x = 0; x < length; x++)
	{
		if (is_palindrome)
			break;
		if (x == length / 2)
		{
			if (is_odd_length)
				second_half_head = second_half_head->next;
			reversed_current = next_second_half;
			next_second_half = next_second_half->next;
			second_half_head->next = NULL;
		}
		else if (x > length / 2)
		{
			next_second_half = next_second_half->next;
			second_half_head->next = reversed_current;
			reversed_current = second_half_head;
			second_half_head = next_second_half;
		}
	}
	next_second_half->next = reversed_current;
	while (next_second_half)
	{
		if (current->n != next_second_half->n)
		{
			is_palindrome = 0;
			break;
		}
		current = current->next;
		next_second_half = next_second_half->next;
	}
	next_second_half->next = reversed_current;
	return (is_palindrome);
}
