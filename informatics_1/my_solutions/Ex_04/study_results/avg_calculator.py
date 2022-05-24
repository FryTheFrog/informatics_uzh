import os

def get_average_grade(path):
    if not os.path.exists(path):
        return None

    def line_finder(file):
        for line in file:
            if ':' in line and not '#' in line:
                yield line
        file.close()
    significant_lines = line_finder(open(path, 'r'))

    def crap_remover(gen_obj):
        for line in gen_obj:
            yield line[line.find(':') + 1:]
    filtered = crap_remover(significant_lines)
    grade_list = list(map(float, filtered))

    if len(grade_list) > 0:
        return sum(grade_list) / len(grade_list)
    else: return 0.0

print(get_average_grade("study_results/my_grades.txt"))