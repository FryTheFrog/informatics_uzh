#!/usr/bin/env python3

def gender_class_rates(dataset):
    male = {
        1: [],
        2: [],
        3: []
    }

    female = {
        1: [],
        2: [],
        3: []
    }
    total = 0.
    for r in dataset[1]:

        total += 1
        is_male = r[3] == 'male'
        if is_male:
            male[r[1]].append(r)
        else:
            female[r[1]].append(r)

    return (
        (rate(male[1], total), rate(male[2], total), rate(male[3], total)),
        (rate(female[1], total), rate(female[2], total), rate(female[3], total))
    )


def rate(vals, total):
    if len(vals) > 0:
        return round(100 * (len(vals) / total), 1)
    else:
        return None


# The following line calls the function and prints the return
# value to the Console. This way you can check what it does.
# However, we encourage you to write tests, because then you
# can easily test many different values on every "Test & Run"!


# Investigate the 'titanic.csv' file before you attempt a submission.
# You might want to download the file to your machine and open it with the functions that you have written in Task 1+2.
# The following example is not complete.
print(gender_class_rates((
    ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
    [
        (True, 1, 'Cumings Mrs. John Bradley (Florence Briggs Thayer)',
         'female', 38, 71.2833),
        (False, 3, 'Heikkinen Miss. Laina', 'female', 26, 7.925)
        # ...
    ]
)))
