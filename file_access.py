from collections import defaultdict
import ast

def open_file(filename):
    fileOpen = open(filename, 'r')
    return fileOpen.read()


def save_dict(filename, sorted_dict):
    f = open(filename, 'w')

    for k, v in sorted_dict:
        f.write(k + ' ' + str(v) + '\n')


def read_posting_list(filename):
    opened_file = open(filename, 'r')
    dict = defaultdict(list)

    for line in opened_file:

        line = line.split(' ', 1)
        term = line[0]
        postings = map(int,ast.literal_eval(line[1]))

        dict[term].extend(postings)

    return dict
