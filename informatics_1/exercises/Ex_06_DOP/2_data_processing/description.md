Data collection is a challenging task and it is very prone to error, because some parts of the data can get lost or recorded incorrectly. Also, data might contain inconsistencies when it is the result of integrating different sources. Therefore every data analyst typically starts with *cleaning* the dataset, before actually analyzing it. The main purpose of this task is to exercise this step by cleaning a concrete dataset.

You will be working on real data that describes passengers of the infamous Titanic accident. In 1912, Titanic has been the largest passenger liner of its time, but unfortunately, sank on its first journey, after a collision with an iceberg. During this tragedy 1,502 out of 2,224 passengers and crew died. Please find the dataset in the `public/titanic.csv` file. The data is provided in the comma-separated values (CSV) format that has been discussed in Task 1. Each row represents one passenger with the following attributes.

| Attribute | Description|
|----------|-------------|
| Survived  |Whether the passenger survived or not|
| Pclass    |Ticket class of the passenger|
| Name      |Name of the passenger|
| Gender    |Gender of the passenger|
| Age       |Age of the passenger|
| Fare      |Fare paid by the passenger|

In this exercise, your task is to implement a function `preprocess` that ensures that the data is cleaned so it can be analyzed more easily. The normalization should filter incomplete data, fix inconsistent values, and replace all strings with values in their most appropriate data type. If a missing or corrupted data point can be identified, the fixing strategy depends on the attribute. Please consider the following description of the intended data format:
 
| Attribute |Type   |Expected schema                            | Fix Action
|-----------|-------|-------------------------------------------|-------
| Survived  |boolean| `True` for survived, `False` otherwise    | Discard
| Pclass    |int    | only values `1`, `2`, and `3` are allowed | Discard
| Name      |string | the name                                  | Discard
| Gender    |string | only `"male"` and `"female"` are allowed  | Discard
| Age       |float  | Age in the range \]0.0, 100.0]            | Discard
| Fare      |float  | The ticket fare is a positive float       | Replace with 25.0


You can assume that the function `preprocess` will receive a result from Task 1 as input, i.e., a list of string tuples. Based on this input, the function should (1) convert each attribute to its intended data type, (2) normalize the values by making sure the values for every attribute are consistent with the expected schema, and (3) handle missing and corrupt values with the corresponding fix action. Remember that the first line of a .csv file is typically the header. This tuple should remain unchanged.

When called, the function should return a tuple of 1) the tuple that contains all header keys and 2) a list of normalized value tuples that are consistent with the schema. For example, consider the following example as an illustration:
    
    preprocess([
    	("Survived", "Pclass", "Name", "Gender", "Age", "Fare"),
        ("survived", "1", "Bukater Ms. Rose", "f", "17", "200"),
    	("No", "3", "Dawson Mr. Jack", "male", "", "")
    ])
    # should result in 
    (
    	('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
	    [
	    	(True, 1, "Bukater Ms. Rose", "female", 17.0, 200.0)
	    ]
    )

**Note:** The provided script defines the signature of the functions. Do not change this signature or the automated grading will fail.

**Note:** Use `int("..")` and `float("..")` to convert strings to the correct data type. You can assume that this conversion will always succeed if the attribute is set. Be careful with boolean values though, as `bool("False")` is `True`.

**Note:** Understanding the data is an important step in every data analysis task, so download and investigate the provided file `titanic.csv` to understand what you are working with. Most importantly, do not confuse invalid data with inconsistent data. For instance, the column *Gender* contains mixed values such as 'Female', 'female', or 'f'. These values are inconsistent with our expected schema, but they are valid. Treat such cases differently than invalid data to preserve as much of the data as possible.

**Note:** The solution requires you to explore the existing dataset and it is highly recommended that you download this task to your local machine and explore the data before attempting a submission. A particularly challenging part of the task is to normalize inconsistent values, e.g., for gender. One approch to achieve this would be to collect all possible values from the large dataset, and to manually assign them, e.g., `male_values = [...]`. To classify a new value, all that is required is to check whether this new value exists in this particular list.

**Note:** It is allowed to reuse the solution in exericse 01.
  

