from collections import defaultdict
import sys


def spimi_invert(token_stream, block_size):
    dict = defaultdict(list)
    while sys.getsizeof(dict) < block_size:
        token = token_stream.pop(0)
        dict[token.term].append(token.docid)

    print dict.items()