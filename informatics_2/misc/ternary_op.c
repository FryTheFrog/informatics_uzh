#include <stdio.h>
#include <stdlib.h>

int main() {
    int a = 1;
    int b = 2;
    int x;

    if (a<b) {
        x = a;
    } else {
        x = 0;
    }
    printf("%d\n", x);

    x = a < b ? a : 0;
    printf("%d\n", x);

    return 0;
}
