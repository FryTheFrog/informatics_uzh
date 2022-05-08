#include <stdio.h>
#include <stdlib.h>

struct Node {
    char data;
    struct Node *next;
    };

void displayList(struct Node *head) {
    struct Node *current = head;
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

struct Node *insertAtEnd(struct Node *head, char data) {
    if (head == NULL) {
        head = malloc(sizeof(struct Node));
        head->data = data;
        head->next = NULL;
        return head;
    }
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
    struct Node *ne = cur->next;
    struct Node *temp = ne->next;
    prev->next = ne;
    ne->next = cur;
    cur->next = temp;
}

struct Node *bubbleSort(struct Node *head) {
    if (head == NULL || head->next == NULL) return head;

    struct Node *temp = malloc(sizeof(struct Node));
    temp->next = head;
    struct Node *last = NULL;

    while(temp->next != last) {
        struct Node *prev = temp;
        struct Node *cur = prev->next;
        while (cur->next != last) {
            if (cur->data > cur->next->data) {
                swapNodes(prev, cur);
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

void isAnagram(struct Node *head1, struct Node *head2) {
    struct Node *sorted1 = bubbleSort(head1);
    struct Node *sorted2 = bubbleSort(head2);
    while (sorted1 != NULL && sorted2 != NULL) {
        if (sorted1->data != sorted2->data) {
            printf("Not anagrams\n");
            return;
        }
        sorted1 = sorted1->next;
        sorted2 = sorted2->next;
    }
    printf("Anagrams\n");
}

int main() {
    char ch;
    struct Node *head = NULL;
    struct Node *head2 = NULL;

    printf("\nEnter the first string: ");
    while ((ch = getchar()) != '\n') {
        head = insertAtEnd(head, ch);
    }
    printf("Enter the second string: ");
    while ((ch = getchar()) != '\n') {
        head2 = insertAtEnd(head2, ch);
    }

    isAnagram(head, head2);
    displayList(head);
    displayList(head2);
    return 0;
}
