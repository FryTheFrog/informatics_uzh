Hiding complexity behind simple class interfaces facilitates the life of developers tremendously.

For example, imagine the hassle if you had to build a correct matrix representation and always calculate multiplications
and additions manually by multiplying or adding up individual values. Instead, what you would do normally,
is to just use a calculator that allows to fill in the matrix values without ever worrying about the internal
calculation steps performed or the checks done to ensure correctness.

Thus, in this task you will build a class `Matrix` with basic capabilities of multiplication and addition to illustrate
these steps usually just abstracted away by a calculator.

## Specification
- Constructor: An instance of `Matrix` should be created via a nested list, ie. `M = Matrix([[1,1], [1,1]])`
- Each list embedded in the larger list corresponds to one row in the matrix
- The indices within the embedded lists correspond to the columns.
- If the constructor input satisfies the following properties it should be stored as a private instance variable:
    1. It contains exactly 2 dimensions, the input to the constructor is a list of lists of either integers or floats.
    2. The nested lists passed to the constructor form an exact rectangle, meaning all rows are of the exact same length.
    3. The nested lists passed to the constructor may not be empty `[[]]`.
- If the above conditions are not satisfied, an `AssertionError` should be thrown
(you may use the `assert x == y, "error message in case of assertion failure"` syntax).
- make sure that two instances`A` and `B` of class `Matrix` can be added via the `+` operator, i.e. `C = A + B` should work
To do this, implement `__add__(self, other)` and return a new `Matrix` instance.
- make sure that two instances`A` and `B` of class `Matrix` can be multiplied via the `*` operator, i.e. `C = A * B` should work
To do this, implement `__mul__(self, other)` and return a new `Matrix` instance.


**Note:** In case you do not know how to add/multiply matrices, check this [Link](https://en.wikipedia.org/wiki/Matrix_(mathematics)#Matrix_multiplication)

**Note:** We encourage you to play around with your data structure to understand the effect that providing the various methods has on the way in which you can use your data structure.

**Note:** All state must be contained within the class. Do not store information in global variables or in class variables. It has to be possible to use multiple instances of the classes in parallel without suffering from side effects.

**Note:** The provided files define the signatures of various classes and functions. Do not change these signatures or the automated grading will fail.

**Note:** We strongly encourage you to add more tests to the public test suite.
