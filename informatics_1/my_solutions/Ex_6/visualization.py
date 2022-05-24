def visualize(records):
    first_class_alive = 0
    second_class_alive = 0
    third_class_alive = 0

    first_class_total = 0
    second_class_total = 0
    third_class_total = 0

    for orig_tuple in records[1]:

        temp_list = []
        for part in orig_tuple:
            temp_list.append(part)
        temp_list.append(temp_list)

        if temp_list[1] == 1:
            first_class_total += 1
            if temp_list[0] == True:
                first_class_alive += 1
        if temp_list[1] == 2:
            second_class_total += 1
            if temp_list[0] == True:
                second_class_alive += 1
        if temp_list[1] == 3:
            third_class_total += 1
            if temp_list[0] == True:
                third_class_alive += 1

    total = first_class_total + second_class_total + third_class_total

    first_class_alive = round(first_class_alive / first_class_total * 100, 1)
    second_class_alive = round(second_class_alive / second_class_total * 100, 1)
    third_class_alive = round(third_class_alive / third_class_total * 100, 1)
    first_class_total = round(first_class_total / total * 100, 1)
    second_class_total = round(second_class_total / total * 100, 1)
    third_class_total = round(third_class_total / total * 100, 1)

    return f"""== 1st Class ==
Total |{round(first_class_total/5) * '*' + round(20 - first_class_total/5) * ' '}| {first_class_total}%
Alive |{round(first_class_alive/5) * '*' + round(20 - first_class_alive/5) * ' '}| {first_class_alive}%
== 2nd Class ==
Total |{round(second_class_total/5) * '*' + round(20 - second_class_total/5) * ' '}| {second_class_total}%
Alive |{round(second_class_alive/5) * '*' + round(20 - second_class_alive/5) * ' '}| {second_class_alive}%
== 3rd Class ==
Total |{round(third_class_total/5) * '*' + round(20 - third_class_total/5) * ' '}| {third_class_total}%
Alive |{round(third_class_alive/5) * '*' + round(20 - third_class_alive/5) * ' '}| {third_class_alive}%"""


print(
    visualize(
        (
            ("Survived", "Pclass", "Name", "Gender", "Age", "Fare"),
            [
                (
                    True,
                    1,
                    "Cumings Mrs. John Bradley (Florence Briggs Thayer)",
                    "female",
                    38,
                    71.2833,
                ),
                (
                    False,
                    1,
                    "Cumings Mrs. John Bradley (Florence Briggs Thayer)",
                    "female",
                    38,
                    71.2833,
                ),
                (True, 2, "Flunky Mr Hazelnut", "female", 18, 51.2),
                (False, 3, "Heikkinen Miss. Laina", "female", 26, 7.925),
            ],
        )
    )
)
