#include "lists.h"

/**
 * reverse_listint - ths reverses a linked list
 * @head: pointer to the first node on the list
 * Return: pointer to the first node on the new list
 */
void reverse_listint(listint_t **head)
{
	listint_t *previous = NULL;
	listint_t *current = *head;
	listint_t *new;

	while (current)
	{
		new = current->next;
		current->next = previous;
		previous = current;
		current = new;
	}

	*head = previous;
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if true, 0 if false
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *temp = *head, *prev = NULL;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	while (1)
	{
		fast = fast->next->next;
		if (!fast)
		{
			prev = slow->next;
			break;
		}
		if (!fast->next)
		{
			prev = slow->next->next;
			break;
		}
		slow = slow->next;
	}

	reverse_listint(&prev);

	while (prev && temp)
	{
		if (temp->n == prev->n)
		{
			prev = prev->next;
			temp = temp->next;
		}
		else
			return (0);
	}

	if (!prev)
		return (1);

	return (0);
}
