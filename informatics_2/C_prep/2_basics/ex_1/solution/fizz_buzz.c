#include <stdio.h>

// "void" functions don't return anything (like return None)
void fizzBuzz(int num) {
    if (num % 3 == 0 && num % 5 == 0) { // "&&" = "and"; "||" = or
        printf("FizzBuzz\n");
    }
    else if (num % 3 == 0) {
        printf("Fizz\n");
    }
    else if (num % 5 == 0) {
        printf("Buzz\n");
    }
    else {
        printf("%d\n", num);    // close to python old-style
    }
}

// calling the function in a for loop
// the "main" function should NOT be a "void" function, instead just return 0
int main() {                    // type of the functions return val is set to integer
    int i;                      // declare var used in the loop
    for (i = 1; i <= 20; ++i) { // (start; stop; incrementation)
        fizzBuzz(i);            // -> (python) for i in range(20 + 1): ...
    }
    return 0;
}
