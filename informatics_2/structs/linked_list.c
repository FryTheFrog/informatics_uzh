#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct node {
    int value;
    struct node *next;
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
    return new_node;
}

node *insert_at_end(node *head, int value) {
    if (head == NULL) {
        head = malloc(sizeof(node));
        head->value = value;
        head->next = NULL;
        return head;
    }
    node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = malloc(sizeof(node));
    current->next->value = value;
    current->next->next = NULL;
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
    current->next = new_node;
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
    return head;
}

node *reverse(node *head) {
    node *previous = NULL;
    node *current = head;
    node *next = NULL;
    while (current != NULL) {
        next = current->next;
        current->next = previous;
        previous = current;
        current = next;
    }
    return previous;
}

void swap_nodes(node *prev, node *cur) {
    node *temp = cur->next->next;
    prev->next = cur->next;
    cur->next->next = cur;
    cur->next = temp;
}

node *bubble_sort(node *head) {
    if (head == NULL || head->next == NULL) return head;
    node *temp = malloc(sizeof(node));
    temp->next = head;
    node *last = NULL;
    while (temp->next != last) {
        node *prev = temp;
        node *cur = prev->next;
        while (cur->next != last) {
            if (cur->value > cur->next->value) {
                swap_nodes(prev, cur);
            }
            else {
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

void print_list (node *head) {
    struct node *current = head;
    while (current != NULL) {
        if (current->next != NULL) {
            printf(" %d -", current->value);
        } else {
            printf(" %d", current->value);
            printf("\n");
        }
        current = current->next;
    }
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
    printf("length; %d\n", length(head));
    printf("find '3': %d\n", find(head, 3));
    head = bubble_sort(head);
    print_list(head);
    return 0;
}
