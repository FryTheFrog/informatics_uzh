#include <stdio.h>

float abundancyIndex(int num) {
    int sum = 0;
    int i;
    for (i = 1; i < num; ++i) {
        if (num % i == 0) {
            sum += i;
        }
    }
    return sum / num;
}

// after running the code the terminal prints something like:
// "exited with code=0" -> which shows the return val of main

// in C there is no "True" or "False"
// instead 0 (=false) and 1 (=true) are used
int main() {
    int a = 6;
    int b = 28;
    if (a == b) {
        return 0;   // ~ return False
    }
    if (abundancyIndex(a) == abundancyIndex(b)) {
        return 1;   // ~ return True
    }
    return 0;       // ~ return False
}
