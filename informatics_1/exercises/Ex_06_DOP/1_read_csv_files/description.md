To store and exchange data between different programs, data is often stored in files using well-defined and reusable formats. For tabular data, a simple yet powerful format is to store the data as comma-seperated-values (CSV). Every line in such a file represents a *record* (a "row") in the tabular data. Every *attribute* of such a record (a "column") is separated by comma.

For instance, consider the following table that contains biometric data of humans:

|Age|Gender| Weight (kg)|Height (cm)|
|---|------|-------|------|
|28 |Female|58|168|
|33|Male||188|
| ... | ...   |...  | ...  |

This data could be represented in a .csv file like this:

    Age,Gender,Weight (kg),Height (cm)
    28,Female,58,168
    33,Male,,188
    ...


In this exercise, your task is to implement a function, `read_csv`, which can open arbitrary .csv files and parse the contents. The function will get the path to a file as a parameter. The function should open the file, read the contents and convert the lines into a list of string tuples. The different tuple indices represent the various attributes of the record.

Several alternatives exist for encoding the .csv data, e.g., quoting attributes ("), adding spaces after each commas("..., ..."). For this task, you can assume that the provided .csv file always exists and that it is well-formated, i.e., that every line has the same number of columns. You can further assume that attributes do not contain any quotes and you can assume that the different attributes do not contain commas. A .csv file can have "gaps" though, such as empty lines or missing attributes. These should be handled as well: the implementation should ignore empty lines and empty attributes should be interpreted as an empty string, e.g.,  a line `a,,c` should be encoded as `("a","","c")`. 

When invoced on the previous .csv file, your function should return the following list:

    [
        ("Age", "Gender", "Weight (kg)", "Height (cm)"),
        ("28", "Female", "58", "168"),
        ("33", "Male", "", "188")
    ]


**Note:** The provided script defines the signature of the functions. Do not change this signature or the automated grading will fail.

**Note:** You are not allowed to use any library for this task.

**Note:** The .csv files often contain the headers as the first line. Make sure that this line is preserved.

**Note:** You can assume that provided files always exist. The implementation should be able to read empy files though, for which the result is simply an empty list.

