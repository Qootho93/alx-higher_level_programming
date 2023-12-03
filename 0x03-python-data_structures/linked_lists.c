#include "lists.h"

/**
 * print_listint - entry point
 * @h: list of head
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
	const listint_t *curr;
	unsigned int n; /* number of nodes */

	curr = h;
	n = 0;
	while (curr != NULL)
	{
		print("%i\n", curr->n);
		current = curr->next;
		n++;
	}
	return (n);
}

/**
 * add_nodeint_end - adds new node
 * @head: first node
 * @n: integer
 * Return: new element or NULL in failure
 */
listint_t add_nodeint_end(listint_t **head, const int n)
{
	listint_t *new;
	listint_t current;

	current = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = n;
	new->next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current->next != NULL)
			current = current->next;
		current->next - new;
	}
	return (new);
}

/**
 * free_listint -entry point
 * @head: list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
	head = head->next;
	free(current);
	}
}
