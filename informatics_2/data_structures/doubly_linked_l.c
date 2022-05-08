#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *next;
    struct node *prev;
};
typedef struct node node;

bool is_empty(node *head) {
    return head == NULL;
}

int length(node *head) {
    int length = 0;
    node *current = head;
    while (current != NULL) {
        length++;
        current = current->next;
    }
    return length;
}

int find(node *head, int value) {
    int i = 0;
    node *current = head;
    while (current->value != value) {
        if (current->next == NULL) {
            return -1;
        }
        i++;
        current = current->next;
    }
    return i;
}

node *insert_at_head(node *head, int value) {
    node *new_node = malloc(sizeof(node));
    new_node->value = value;
    new_node->next = head;
    new_node->prev = NULL;
    if (head != NULL) {
        head->prev = new_node;
    }
    return new_node;
}

node *insert_at_end(node *head, int value) {
    if (head == NULL) {
        head = malloc(sizeof(node));
        head->value = value;
        head->next = NULL;
        head->prev = NULL;
        return head;
    }
    node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = malloc(sizeof(node));
    current->next->value = value;
    current->next->next = NULL;
    current->next->prev = current;
    return head;
}

node *insert_at_position(node *head, int value, int position) {
    if (position == 0) {
        return insert_at_head(head, value);
    }
    node *current = head;
    for (int i = 0; i < position - 1; i++) {
        current = current->next;
    }
    node *new_node = malloc(sizeof(node));
    new_node->value = value;
    new_node->next = current->next;
    new_node->prev = current;
    current->next = new_node;
    if (new_node->next != NULL) {
        new_node->next->prev = new_node;
    }
    return head;
}

node *delete_at_position(node *head, int position) {
    if (position == 0) {
        head = head->next;
    }
    node *current = head;
    for (int i = 0; i < position - 1; i++) {
        current = current->next;
    }
    current->next = current->next->next;
    if (current->next != NULL) {
        current->next->prev = current;
    }
    return head;
}

node *reverse(node *head) {
    node *previous = NULL;
    node *current = head;
    node *next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = previous;
        current->prev = next;
        previous = current;
        current = next;
    }
    return previous;
}

void swap_nodes(node *prev, node *cur) { // swap by value
    int temp = prev->value;
    prev->value = cur->value;
    cur->value = temp;
}

node *bubble_sort(node *head) {
    node *current = head;
    while (current != NULL) {
        node *next = current->next;
        while (next != NULL) {
            if (current->value > next->value) {
                swap_nodes(current, next);
            }
            next = next->next;
        }
        current = current->next;
    }
    return head;
}

void print_list(node *head) {
    node *current = head;
    while (current != NULL) {
        printf("%d ", current->value);
        current = current->next;
    }
    printf("\n");
}

int main() {
    node *head = malloc(sizeof(node));
    head = NULL;

    for (int i = 0; i < 10; i++) {
        head = insert_at_head(head, i);
    }

    head = reverse(head);
    print_list(head);
    delete_at_position(head, 3);
    insert_at_position(head, 3, 8);
    print_list(head);
    printf("is_empty: %d\n", is_empty(head));
    printf("length: %d\n", length(head));
    printf("find '3': %d\n", find(head, 3));
    head = bubble_sort(head);
    print_list(head);

    return 0;
}
