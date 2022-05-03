#include <stdio.h>
#include <stdlib.h>

// create node
struct node {
    int value;
    struct node *next;
};

// print linked list value
void printLinkedList (struct node *p) {
    while (p != NULL) {
        printf("%d ", p->value);
        p = p->next;
    }
}

int main() {
    // init nodes
    struct node *head;
    struct node *one = NULL;
    struct node *two = NULL;
    struct node *three = NULL;

    // allocate memory
    one = malloc(sizeof(struct node));
    two = malloc(sizeof(struct node));
    three = malloc(sizeof(struct node));

    // assign value values
    one->value = 1;
    two->value = 2;
    three->value = 3;

    // connect nodes
    one->next = two;
    two->next = three;
    three->next = NULL;

    // printing node-value
    head = one;
    printLinkedList(head);
}
