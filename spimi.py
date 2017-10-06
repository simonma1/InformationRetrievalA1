from collections import defaultdict
from file_access import save_dict
import operator
import sys


def spimi_invert(token_stream, block_size, file_number):
    dict = defaultdict(list)
    while sys.getsizeof(dict) < block_size and len(token_stream) > 0:
        token = token_stream.pop(0)
        dict[token.term].append(token.docid)

    sorted_dict = sorted(dict.items(), key=operator.itemgetter(0))

    filename = 'savefile' + str(file_number) + '.txt'
    save_dict(filename, sorted_dict)

    return filename
