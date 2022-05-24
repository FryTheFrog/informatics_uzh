
This task consists of two separate parts. The first part is about **fuzz testing** and
includes the implementation of three functions. The second part is about
**white-box testing** and contains the writing of unit tests of the implemented
functions.

### Fuzz testing
[Fuzzing][fuzz] is the process of generating _random_ inputs to feed into a
program with the goal of hopefully uncovering unexpected behavior
without having to guess corner cases. Many bugs
stem from errors of the input processing, so by supplying many random inputs, these bugs
may be uncovered automatically.

This task shows a simple application of a fuzzer and runner which are
both represented as
functions named `fuzzer` and `run`. The runner tests the program `calculate_factorial`
with random input from the `fuzzer` function.

Your task is to implement these three functions:

1. The function `fuzzer` takes four input parameters (all integers) and
returns a string of random length containing random characters. The first two
parameters `min_length` and `max_length` determine how
long the returned random string can be. The two parameters
`char_start` and `char_end` determine which character from the ASCII table
should be included in the returned random string. So for example, calling the function `fuzzer(5, 10, 43, 57)` will return a string that is between 5 and 10 (including) characters long and contains randomly selected characters corresponding to decimal numbers between 43 (`+`) and 57 (`9`) from the ASCII table. For this example, one such random string might be `.5728//`.

2. The function `calculate_factorial` takes one input parameter `inp` (an
integer or a string) and returns the factorial of the input `inp` as an
integer. The factorial function should return `None` if the
input is `None`. If the input is a string, the function should try to convert the
input string into an integer and if this is not possible, the function should
throw a `TypeError` with the message `"TypeError: string"`.
If the converted number or integer input is negative, the function should throw a
`ValueError` with the message `"ValueError: number negative"`. If the converted
number or integer input is larger than 10, the function should also throw a
`ValueError` but with the message `"ValueError: number too large"`. This is for
example a simulation of a buffer overflow.

3. The function `run` has one input parameter `trials` (an integer)
and returns a list of tuples, containing feedback on executing the
`calculate_factorial` function with random inputs.
 The function `run` should run your function `calculate_factorial`
as many times as specified in `trials`. Each time `calculate_factorial`
is run, it should be provided with a new random input obtained by calling the
`fuzzer` function. **For the parameter input for the function `fuzzer` 
use the provided global variables instead of passing values directly to the function.**
For each run, a new tuple should be appended to the return value, where each tuple
consists of two elements. The first
element is an integer which can be `0` (success) or `1` (failure) and the second element contains a string.
When `calculate_factorial` throws a `ValueError`,
the error should be caught and a tuple with the elements `1` and the error
message should be added to the list which will be returned. For example if 
`calculate_factorial` raises an `ValueError` with the message `"ValueError: number too large"`,
the following tuple should be added to the list: (`1`, `"ValueError: number too large"`).
Any other thrown error should be caught and a tuple with
the elements `1` and the string `"Other error"` should be added to the list.
If no error is thrown, a tuple
with the elements `0` and an empty string should be added to the list. If no element
is added to the resulting list, an empty list should be returned.

**Note**: For the building a string of random range and with random characters
these functions can help: [randrange][random], [chr][character]

**Note**: Check out the lecture slides for raising and catching Errors/Exceptions.

### White-box testing
White-box testing is about implementing tests by studying the implementation of
a program. In this part of the task you should write text cases for the
function `calculate_factorial` only.

You should test whether the function `calculate_factorial` throws the correct
exceptions when supplied with invalid inputs and you should also test whether it
works normally with valid input. To check whether a function throws an exception,
have a look at [`self.assertRaises`][raises]. You do not have to test the error
messages themselves. As your function also should accept integers, test
these cases as well. And remember to also test edge cases!

**Note:** With [`self.fail()`][fail] you can make a test case fail.

[random]:https://docs.python.org/3/library/random.html#random.randrange
[character]:https://docs.python.org/3/library/functions.html#chr
[fuzz]:https://en.wikipedia.org/wiki/Fuzzing
[fail]:https://docs.python.org/3/library/unittest.html#unittest.TestCase.fail
[raises]:https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises
