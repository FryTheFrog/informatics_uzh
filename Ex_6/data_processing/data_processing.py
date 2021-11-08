def preprocess(records):

    datalist = []
    reslist = []
    res_tuple = []
    for orig_tuple in records:
        if orig_tuple == ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'):
            res_tuple.append(orig_tuple)
            continue
        temp_list = []

        for part in orig_tuple:
            temp_list.append(part)
        datalist.append(temp_list)

        temp_tuple = []
        for idx in range(len(temp_list)):
            if idx == 0:
                if temp_list[idx] in ['', 'undefined', 'Undefined', 'unknown', 'Unknown']:
                    temp_tuple = (); break
                elif temp_list[idx] in ['yes', 'Yes', 'survived', 'Survived', 'true', 'True', 't', 'T', 'Alive']:
                    temp_tuple.append(True)
                elif temp_list[idx] in ['no', 'No', 'dead', 'Dead', 'false', 'False', 'f', 'F', 'Survived=dead']:
                    temp_tuple.append(False)

            elif idx == 1: #Pclass
                if temp_list[idx] in ['1', '2', '3'] and temp_list[idx] != '':
                    temp_list[idx] = int(temp_list[idx])
                    temp_tuple.append(temp_list[idx])
                else: temp_tuple = (); break

            elif idx == 2: #Name
                if temp_list[idx] in ['', 'undefined', 'Undefined', 'unknown', 'Unknown']:
                    temp_tuple = (); break
                else: temp_tuple.append(temp_list[idx])

            elif idx == 3: #Gender
                if temp_list[idx] in ['', 'undefined', 'Undefined', 'unknown', 'Unknown']:
                    temp_tuple = (); break
                elif temp_list[idx] in ['male', 'Male', 'm', 'M']:
                    temp_tuple.append('male')
                elif temp_list[idx] in ['female', 'Female', 'f', 'F']:
                    temp_tuple.append('female')

            elif idx == 4: #Age
                if temp_list[idx] in ['', 'undefined', 'Undefined', 'unknown', 'Unknown']:
                    temp_tuple = (); break
                temp_list[idx] = float(temp_list[idx])
                if temp_list[idx] > 0 and temp_list[idx] <= 100:
                    temp_tuple.append(temp_list[idx])
                else: temp_tuple = (); break

            elif idx == 5: #Fare
                if temp_list[idx] in ['', 'undefined', 'Undefined', 'unknown', 'Unknown']:
                    temp_tuple.append(25.0)
                else:
                    temp_list[idx] = float(temp_list[idx])
                    temp_tuple.append(temp_list[idx])

        if temp_tuple != ():
            reslist.append(tuple(temp_tuple))

    res_tuple.append(reslist)
    res_tuple = tuple(res_tuple)

    return res_tuple

records = [
                ('Survived', 'Pclass', 'Name', 'Gender', 'Age', 'Fare'),
                ('no', '3', 'Braund Mr. Owen Harris', 'male', '22', '7.25'),
                ('Dead', '3', 'Braund Ms. Maria', 'Female', '21', ''),
                ('Yes', '1', 'Cumings Mrs. John Bradley (Florence Briggs Thayer)', 'F', '38', '71.28'),
                ('', '3', 'Vander Planke Miss. Augusta', 'female', '', ''),
                ('Dead', '3', 'Lennon Mr. Denis', 'male', '0', '15.5')
            ]

print(preprocess(records))