#include <stdlib.h>
#include <unistd.h>
#include "lists.h"
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted list
 * @head: a pointer to the head of a listed list
 * @num: number to be inserted
 *
 * Return: pointer to the new head
 */

listint_t *insert_node(listint_t **head, int num)
{
	listint_t *current = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = num;
	new->next = NULL;

	if (!*head || (*head)->n > num)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (current && current->n < num)
		{
			temp = current;
			current = current->next;
		}

		temp->next = new;
		new->next = current;
	}

	return (new);
}
