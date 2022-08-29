#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome_r - checks if a singly linked list is a palindrome.
 * @left: The list fromm left
 * @right: The List from right
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome_r(listint_t **left, listint_t *right)
{
    int palindrome = 0;

    if (right == NULL)
        return 1;
    palindrome = is_palindrome_r(left, right->next);
    if (palindrome == 0)
        return 0;
    palindrome = (*left)->n == right->n;
    *left = (*left)->next;
    return palindrome;
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: The list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    if (head == NULL)
        return 0;
    if (((*head) == NULL) || ((*head)->next == NULL))
        return 1;

    return is_palindrome_r(head, *head);
}
