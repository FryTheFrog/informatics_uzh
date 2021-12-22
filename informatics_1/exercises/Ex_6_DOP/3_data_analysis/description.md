
Once a dataset is normalized, analyzing it is a breeze. In this task, you will perform a basic data analysis task on the Titanic data that you have worked on in the previous tasks. You can assume that you will be provided with valid data according to the following schema:

| Attribute |Type   |Expected schema                            | Fix Action
|-----------|-------|-------------------------------------------|-------
| Survived  |boolean| `True` for survived, `False` otherwise    | Discard
| Pclass    |int    | only values `1`, `2`, and `3` are allowed | Discard
| Name      |string | the name                                  | Discard
| Gender    |string | only `"male"` and `"female"` are allowed  | Discard
| Age       |float  | Age in the range \]0.0, 100.0]            | Discard
| Fare      |float  | The ticket fare is a positive float       | Replace with 25.0

As defined before, the data is provided in a tuple, in which the first element is a tuple with all keys and the second element is a list that contains all records as normalized tuples. On this data, you can now carry out different analyses and investigate interesting questions.


For this task, we are interested in the *gender distribution* among different classes. Based on provided dataset, partition the data according two dimensions: 1) Passengers' class, 2) Passengers' gender. For each combination among these two dimensions (6 in total), you need to calculate the ratio w.r.t all passengers, for example, the ratio of first class female passengers. 



Implement a function `gender_class_rates` that takes the dataset as input and that calculates the passengers distribution according to their gender and class. The results should be arranged in two nested tuples like the ones illustrated in the following example. More specifically, `t[0][1]` should contain the rate of passengers that were holding second class ticket and were male:

    (
    	("First class and male", "Second class and male", "Third class and male"),
    	("First class and female", "Second class and female", "Third class and female")
    )

Calculate the percentages in the range of [0, 100] with a precision of one number of decimal. For example, in a population of 123 passengers, a group of 45 passengers represent 45/123=0.3658...~36.6% of the population. The results should be stored as `float` numbers and you can use the built-in Python function `round` to achieve the cut-off.


**Note:** The provided script defines the signature of the functions. Do not change this signature or the automated grading will fail.

**Note**: You can assume that the provided dataset is valid and always contains at least one entry. It might be the case though that the dataset does not contain data for all six values. The implementation should return `None` in these cases.
