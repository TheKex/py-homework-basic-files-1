import os
if __name__ == '__main__':
    files = ['1.txt', '2.txt', '3.txt']
    files_metadata = {}
    for file_name in files:
        with open(os.path.join('src', 'files', file_name), encoding="utf-8") as file:
            files_metadata[file_name] = len(file.readlines())
    files.sort(key=lambda x: files_metadata[x])

    with open(os.path.join('src', 'files', 'result.txt'), 'w', encoding="utf-8") as res_file:
        for file in files:
            res_file.write(file + '\n' + str(files_metadata[file]) + '\n')
            with open(os.path.join('src', 'files', file), encoding="utf-8") as read_file:
                res_file.writelines(read_file.readlines() + ['\n'])

