#include <stdio.h>

int main() {
    const int rows = 5;     // constant -> var can't be changed
    int i, space, k = 0, count1 = 0, count2 = 0;    // it's possible to create multiple vars
    for (i = 1; i <= rows; ++i) {                   // of the same type like this
        for (space = 1; space <= rows - i; ++space) {
            printf("  ");
            ++count1;
        }
        while (k < 2 * i - 1) {
            if (count1 <= rows - 1) {
                printf("%d ", (i + k));
                ++count1;
            }
            else {
                ++count2;
                printf("%d ", (i + k - 2 * count2));
            }
            ++k;
        }
        count1 = count2 = k = 0;
        printf("\n");
    }
    return 0;
}
