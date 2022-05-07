// NOT WORKING

#include <stdio.h>
#include <stdlib.h>

struct Node {
    char data;
    struct Node *next;
    };

void displayList(struct Node *head) {
    struct Node *current = head->next;
    while (current != NULL) {
        if (current->next != NULL) {
            printf(" %c ->", current->data);
        } else {
            printf(" %c", current->data);
            printf("\n");
        }
        current = current->next;
    }
}

struct Node *insertList(struct Node *head, char data) {
    struct Node *current = head;
    struct Node *newNode = malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
    return head;
}

void swapNodes(struct Node *prev, struct Node *cur) {
    // before swap: prev−>cur−>ne−>temp
    // after swap: prev−>ne−>cur−>temp
    struct Node * ne = cur->next;
    struct Node * temp = ne->next; prev->next = ne;
    ne->next = cur;
    cur->next = temp;
    return;
}

struct Node *bubbleSort(struct Node *head) {
    struct Node *prev = head;
    struct Node *cur = head->next;
    struct Node *ne = cur->next;
    while (ne != NULL) {
        if (cur->data > ne->data) {
            swapNodes(prev, cur, ne);
        }
        struct Node *ne = ne->next;
        struct Node *cur = cur->next;
        struct Node *prev = prev->next;
    }
    return head;
}

void isAnagram(struct Node *head1, struct Node *head2) {
    struct Node *sorted1 = bubbleSort(head1);
    struct Node *sorted2 = bubbleSort(head2);
    displayList(sorted1);
    displayList(sorted2);
    if (sorted1 == sorted2) {
        printf("\nThe two linked lists are anagrams.\n");
    }
    else {
        printf("\nThe two linked lists are not anagrams.\n");
    }
}

int main() {
    char ch;
    struct Node *head = NULL;
    struct Node *head2 = NULL;

    printf("\nEnter the first string: ");
    while ((ch = getchar()) != '\n') {
        head = insertList(head, ch);
    }
    printf("Enter the second string: ");
    while ((ch = getchar()) != '\n') {
        head2 = insertList(head2, ch);
    }

    displayList(head);
    displayList(head2);
    isAnagram(head, head2);
    displayList(head);
    displayList(head2);
    return 0;
}
