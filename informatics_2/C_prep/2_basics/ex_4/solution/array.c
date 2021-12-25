#include <stdio.h>

int main() {
    int array[5];                   // declare type of elems and size of array
    int i;
    for (i = 0; i < 5; i++) {
        array[i] = i;               // assign values in the array
    }
    for (i = 4; i >= 0; i--) {      // iterate in reverse
        printf("%d\n", array[i]);   // print the elems
    }                               // it is NOT possible to just print the whole array
    return 0;
}
