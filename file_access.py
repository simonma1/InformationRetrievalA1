def open_file(filename):
    fileOpen = open(filename, 'r')
    return fileOpen.read()


def save_dict(filename, sorted_dict):
    f = open(filename, 'w')

    for k, v in sorted_dict:
        f.write(k + ' ' + str(v) + '\n')
