#include <stdio.h>

int main() {
    int num = 23;
    if (num == 1) {
        return 0;
    }
    int i;
    for (i = 2; i <= num / 2; ++i) {
        if (num % i == 0) {
            return 0;
        }
    }
    return 1;
}
