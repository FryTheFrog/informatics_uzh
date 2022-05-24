def read_csv(path):
    list = []
    with open(path) as file:
        for line in file:
            if line == '\n':
                continue
            line = line.split(',')
            for idx in range(len(line)):
                line[idx] = line[idx].replace('\n', '')
            line = tuple(line)
            list.append(line)
    return list

print(read_csv('Ex_6/read_simple/example.csv'))