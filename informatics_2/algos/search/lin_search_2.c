#include <stdio.h>

int main() {
    int n = 5;                  // num of elems
    int array[5] = {3,2,5,4,2}; // array
    int v = 2;                  // desired num
    int i = 0;
    do {
        i++;
        }
    while (i < 5 && array[i] != v);
    if (i < 5) {
        printf("%d", i);
    }
    return 0;
}

/* This will return the first occurance
of the desired number */
