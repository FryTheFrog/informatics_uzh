
Numbers are easy to compute, but for human data analysts, a good visualization of the results is a very powerful tool to see and understand data distribution, outlier values, or possible trends, because they are easier to interpret and to compare than plain numerical results.

In this exercise, you are going to implement a function `visualize` that performs a simple analysis and visualization of the Titanic data. It should visualize two things for the different ticket classes: the survival rates of the passengers in the different classes (e.g., "What was the survival rate for people in the third class?") and the percentage of this class in the overall population (e.g., "How many percent of the passengers had tickets in the first class?").

The passenger class is a so called *categorical* data type, as its values come from a fixed set that describes mutualy exclusive, qualitative properties. Bar charts are the common visualization method for such data type. A bar chart is a type of chart that shows the values of different categories of data as rectangular bars with different lengths. You are not expected to generate any graphical output, instead, you will generate text-based bars. Below, you can see an example that illustrates the expected output (the numbers are completely made up):

    == 1st Class ==
    Total |**                  | 10.1%            
    Alive |*****               | 25.7%
    == 2nd Class ==
    Total |*******             | 32.7%
    Alive |*****               | 24.1%
    == 3rd Class ==
    Total |***********         | 57.2%
    Alive |****                | 19.8%

The output should have three parts for the first, second, and third class. For each part, the visualization should show the total percentage of the passengers in this class ("Total"), as well as the survival rate for people that had tickets in this class ("Alive"). The full bar should be 20 characters wide from `|` to `|`, while an empty bar represents 0% and a full bar represents 100%. Add the concrete percentage to the right, rounded to one decimal digit and leave a space to the `|`.

The concrete percentages need to be mapped to 20 characters for the visualization, so every character equals about 5%. Combine a division and a `round` to calculate how many characters need to be drawn, e.g., for `37.6%` the calculation would be `round(37.6/5)`, which is `8`, so `8` characters need to be drawn. Fill the remaining characters with spaces.

You can assume that your function will be provided the same normalized input data as for the previous task. Unlike for the previous task though, you can assume this time that at least one passenger will exist per class to reduce the amount of corner cases that need to be considered in the implementation.

**Note:** The provided script defines the signature of the functions. Do not change this signature or the automated grading will fail.

**Note:** Follow the *exact* same order, formatting, and spacing as illustrated in the example. Make sure that you pay attention to lower/upper-case letters and to symbols. The grading relies on a strict string equality. 

**Note:** While it is not strictly required to work on this task, we would like to encourage you to put all parts of the whole exercise together and use your .csv parser, normalizer, and this analysis/visualizer to investigate the actual distribution in the real dataset.

**Note:** In Python, it is possible to multiply strings, for example, `2*"abc"` is `"abcabc"`.

