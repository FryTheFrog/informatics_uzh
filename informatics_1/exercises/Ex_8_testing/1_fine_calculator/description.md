
In this task you are going to practice *black-box testing*, thereby testing the program's ability to comply with its specification, in terms of expected output to specific inputs, with no knowledge about its implementation.


## Function Specification
The function you will be testing, called `fine_calculator` calculates the cost of a traffic fine caused by speeding.
The function takes 2 parameters: `Area` and `Speed`.
`Area` indicates the area where the speed control is made.
`Speed` indicates the measured speed during the speed control.
A fine is calculated depending on the area's type and the speed recorded.

There are 3 `Area` types: Urban, Expressway and Motorway.
Each area has its own speed limit and a fine coefficient:
* The speed limit for Urban areas is 50 km/h, and the fine coefficient is 1
* The speed limit for Expressway areas is 100 km/h, and the fine coefficient is 0.8
* The speed limit for Motorway areas is 120 km/h, and the fine coefficient is 0.5

A correct implementation of `fine_calculator` must comply with the following requirements:
* For the speed parameter it expects a non-negative (float or int) number
* For the area parameter it expects a lowercase string 'urban', 'expressway' or 'motorway'
* The function returns the string `Invalid Area Type` if it receives an area parameter with the type other than string
* The function returns the string `Invalid Area Value` if it receives an string parameter other than the 3 areas defined above
* The function returns the string `Invalid Speed Type` if it receives a speed parameter with the type other than the defined above
* The function returns the string `Invalid Speed Value` if it receives an out of range speed parameter
* The function returns `0` if the speed provided to the function is less than the speed limit.
* If the measured speed exceeds the speed limit and the parameters are valid, the amount of the fine is calculated by multiplying the area fine coefficient by the square of the overspeed percentage, ie: `fine_coefficient` * `overspeed_percentage`²; see a concrete example below
* If the parameters are valid, the function returns the total fine amount to the closest integer value

For example, if the `area` parameter is given as _motorway_ and the `speed` parameter is _180 km/h_, the percentage of overspeed is 50% since Motorways' speed limit is 120 km/h.
The amount of the fine is 0.5 x 50² = 1250, hence:

```Python
fine_calculator("motorway", 180) == 1250
```

## Task details

Your task is to provide a good test suite in `public/tests.py` that can decide whether a given `fine_calculator` implementation follows the specification given above.
Your test suite will be run with a variety of correct and incorrect implementations.
The resulting grade depends on its ability to detect faulty implementations of `fine_calculator`.
More specifically, the test suite should pass for a correct implementation and fail for an incorrect one.

Your task is to make sure that any implementation of `fine_calculator` does indeed always comply with _all_ of specified requirements.
For this purpose, you need to test the function with multiple test cases that you will write.

**Note:** You do not need to implement `fine_calculator` in `public/script.py`. You can simply start writing your tests against unknown implementations. This is called "test-driven development": you provide the test suite _first_ to specify the requirements for a given implementation by identifying interesting test cases. You then implement `fine_calculator` in `script.py` to run your test suite again using "Test & Run". However, your implementation of the function is irrelevant for the grading.

**Note:** You do not need to come up with good error messages, it is enough to fail a test if a problem can be detected (e.g., `self.assertEquals(expected, actual)`).

**Note:** Define your test suite as a subclass of `TestCase`.
Do not use utility functions for the assertions, instead, include calls like `self.assertEqual` directly in the body of the test functions or the automated grading will mark the solution as incorrect.

**Note:** The provided files define the signatures of various classes and functions.
Do not change these signatures or the automated grading will fail.
