#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

struct set {
    int key;
    int data;
};
typedef struct set set;

set *arr;
int capacity = 10;
int size = 0;

int hash_function(int key) {
    return (key % capacity);
}

bool check_prime(int n) {
    int i;
    if (n == 1 || n == 0) {
        return false;
    }
    for (i = 2; i < n / 2; i++) {
        if (n % i == 0) {
            return 0;
        }
    }
    return true;
}

int get_prime(int n) {
    if (n % 2 == 0) {
        n++;
    }
    while (!check_prime(n)) {
        n += 2;
    }
    return n;
}

void init_array() {
    capacity = get_prime(capacity);
    arr = (set *)malloc(capacity * sizeof(set));
    for (int i = 0; i < capacity; i++) {
        arr[i].key = 0;
        arr[i].data = 0;
    }
}

void insert(int key, int data) {
    int idx = hash_function(key);
    if (arr[idx].data == 0) {
        arr[idx].key = key;
        arr[idx].data = data;
        size++;
        printf("key (%d) inserted\n", key);
    } else if (arr[idx].key == key) {
        arr[idx].data = data;
    } else {
        printf("collision!\n");
    }
}

void delete_element(int key) {
    int idx = hash_function(key);
    if (arr[idx].data == 0) {
        printf("key does not exist\n");
    } else if (arr[idx].key == key) {
        arr[idx].key = 0;
        arr[idx].data = 0;
        size--;
        printf("key (%d) deleted\n", key);
    } else {
        printf("collision!\n");
    }
}

void display() {
    for (int i = 0; i < capacity; i++) {
        if (arr[i].data != 0) {
            printf("Key: %d, Data: %d\n", arr[i].key, arr[i].data);
        }
    }
}

int size_of_array() {
    return size;
}

int main() {
    init_array();
    for (int i = 0; i < 10; i++) {
        insert(i, i);
    }
    display();
}
