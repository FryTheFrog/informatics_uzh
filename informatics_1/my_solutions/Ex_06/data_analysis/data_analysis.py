def gender_class_rates(dataset):
    first_class_male = 0
    second_class_male = 0
    third_class_male = 0

    first_class_female = 0
    second_class_female = 0
    third_class_female = 0

    for orig_tuple in dataset[1]:

        temp_list = []
        for part in orig_tuple:
            temp_list.append(part)
        temp_list.append(temp_list)

        if temp_list[1] == 1:
            if temp_list[3] == "male":
                first_class_male += 1
            elif temp_list[3] == "female":
                first_class_female += 1
        if temp_list[1] == 2:
            if temp_list[3] == "male":
                second_class_male += 1
            elif temp_list[3] == "female":
                second_class_female += 1
        if temp_list[1] == 3:
            if temp_list[3] == "male":
                third_class_male += 1
            elif temp_list[3] == "female":
                third_class_female += 1

    total = (
        first_class_male
        + first_class_female
        + second_class_male
        + second_class_female
        + third_class_male
        + third_class_female
    )
    print(total)
    first_class_male = round(first_class_male / total * 100, 1)
    second_class_male = round(second_class_male / total * 100, 1)
    third_class_male = round(third_class_male / total * 100, 1)
    first_class_female = round(first_class_female / total * 100, 1)
    second_class_female = round(second_class_female / total * 100, 1)
    third_class_female = round(third_class_female / total * 100, 1)

    return (
        (
            first_class_male if first_class_male > 0 else None,
            second_class_male if second_class_male > 0 else None,
            third_class_male if third_class_male > 0 else None,
        ),
        (
            first_class_female if first_class_female > 0 else None,
            second_class_female if second_class_female > 0 else None,
            third_class_female if third_class_female > 0 else None,
        ),
    )


data = (
    ("Survived", "Pclass", "Name", "Gender", "Age", "Fare"),
    [
        (False, 3, "Braund Mr. Owen Harris", "male", 22.0, 7.25),
        (False, 3, "Braund Ms. Maria", "female", 21.0, 25.0),
        (
            True,
            1,
            "Cumings Mrs. John Bradley (Florence Briggs Thayer)",
            "female",
            38.0,
            71.28,
        ),
    ],
)

print(gender_class_rates(data))
