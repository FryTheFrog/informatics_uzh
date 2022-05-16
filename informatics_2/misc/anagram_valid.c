#include <stdio.h>
#include <stdlib.h>

struct node {
    char value;
    struct node *next;
};
typedef struct node node;

void display_list(node *head) {
    node *current = head;
    while (current != NULL) {
        if (current->next != NULL) {
            printf(" %c ->", current->value);
        } else {
            printf(" %c", current->value);
            printf("\n");
        }
        current = current->next;
    }
}

node *insert_at_end(node *head, char data) {
    if (head == NULL) {
        head = malloc(sizeof(node));
        head->value = data;
        head->next = NULL;
        return head;
    }
    node *current = head;
    node *newNode = malloc(sizeof(node));
    newNode->value = data;
    newNode->next = NULL;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    return head;
}

void swap_nodes(node *prev, node *cur) {
    node *ne = cur->next;
    node *temp = ne->next;
    prev->next = ne;
    ne->next = cur;
    cur->next = temp;
}

node *bubble_sort(node *head) {
    if (head == NULL || head->next == NULL)
        return head;

    node *temp = malloc(sizeof(node));
    temp->next = head;
    node *last = NULL;

    while (temp->next != last) {
        node *prev = temp;
        node *cur = prev->next;
        while (cur->next != last) {
            if (cur->value > cur->next->value) {
                swap_nodes(prev, cur);
            } else {
                cur = cur->next;
            }
            prev = prev->next;
        }
        last = cur;
    }
    head = temp->next;
    free(temp);
    return head;
}

void is_anagram(node *head1, node *head2) {
    node *current1 = head1;
    node *current2 = head2;
    while (current1 != NULL && current2 != NULL) {
        if (current1->value != current2->value) {
            printf("Not anagrams\n");
            return;
        }
        current1 = current1->next;
        current2 = current2->next;
    }
    printf("Anagrams\n");
}

int main() {
    char ch;
    node *head = NULL;
    node *head2 = NULL;

    printf("\nEnter the first string: ");
    while ((ch = getchar()) != '\n') {
        head = insert_at_end(head, ch);
    }
    printf("Enter the second string: ");
    while ((ch = getchar()) != '\n') {
        head2 = insert_at_end(head2, ch);
    }
    head = bubble_sort(head);
    head2 = bubble_sort(head2);
    is_anagram(head, head2);
    display_list(head);
    display_list(head2);
    return 0;
}
