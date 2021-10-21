import os

def process_data(path_reading, path_writing):
    if not os.path.exists(path_reading):
        return False
    with open(path_reading, 'r') as ugly_file, open(path_writing, 'w') as clean_file:
        for line in ugly_file:
            if line.strip() == 'Name':
                clean_file.write('Firstname,Lastname')
            elif ';' in line:
                shitline = line[line.find(';') + 1:].replace('\n', '') + ',' + line[:line.find(';')]
                clean_file.write('\n' + shitline.strip())
            elif ' ' in line and not ';' in line:    
                clean_file.write('\n' + line.replace(' ', ',').replace('\n', ''))
            elif line == '\n':
                clean_file.write('\n,')
    return 'data processed'
            
print(process_data("data_processing/my_data.txt", "data_processing/my_data_processed.txt"))