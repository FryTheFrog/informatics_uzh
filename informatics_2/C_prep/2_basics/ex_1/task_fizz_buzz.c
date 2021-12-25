#include <stdio.h>

// Task: implement a fizzBuzz function
// - takes an integer
// - prints "Fizz", "Buzz" or "FizzBuzz"
// - Fizz: number divisible by 3
// - Buzz: divisible by 5
// - FizzBuzz: divisible by 3 and 5

// "void" functions don't return anything (like return None)
void fizzBuzz(int num) {        // the type of the argument also has to be declared
    // TODO: implement me
}

// calls the function in a for loop
// the "main" function should NOT be a "void" function, instead just return 0
int main() {                    // type of the functions return value is set to integer
    int i;                      // declare var used in the loop
    for (i = 1; i <= 20; ++i){  // (start; stop; incrementation)
        fizzBuzz(i);            // -> (python) for i in range(20 + 1): ...
    }
    return 0;
}
