import csv

#'Ex_6/data_processing/titac.csv'


def data_fucker(in_path, out_path):
    key_list = []
    with open(in_path) as data:
        for key in data.readline().split(","):
            key = key.replace("\n", "")
            key_list.append(key)
    for key in key_list:
        with open(in_path, "r") as data, open(out_path, "a") as fucked:
            data = csv.DictReader(data)
            poss_list = []
            for line in data:
                if line[key] not in poss_list:
                    poss_list.append(line[key])
            fucked.write(f"\n\n{key}\n" + str(poss_list))
    print(key_list)


data_fucker("Ex_6/data_processing/titanic.csv", "Ex_6/data_processing/inconsist.txt")
