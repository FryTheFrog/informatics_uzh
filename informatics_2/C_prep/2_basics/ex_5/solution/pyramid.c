#include <stdio.h>

int main() {
    const int rows = 5;     // constant -> var can't be changed
    int i, space, k = 0, count = 0;    // it's possible to create multiple vars
    for (i = 1; i <= rows; ++i) {                   // of the same type like this
        for (space = 1; space <= rows - i; ++space) {
            printf("  ");
        }
        while (k < 2 * i - 1) {
            if (k <= i - 1) {
                printf("%d ", (i + k));
            }
            else {
                ++count;
                printf("%d ", (i + k - 2 * count));
            }
            ++k;
        }
        count = k = 0;
        printf("\n");
    }
    return 0;
}
