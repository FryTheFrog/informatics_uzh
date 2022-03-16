#include <stdio.h>

int main() {
    int n = 5;                  // num of elems
    int array[5] = {3,2,5,4,2}; // array
    int v = 2;                  // desired num
    int p;
    int i;
    for (i = 0; i < n; i++) {
        if (array[i] = v) {
            p = i;
        }
    }
    printf("%d", p);
    return 0;
}

/* This will return the last occurance
of the desired number */
