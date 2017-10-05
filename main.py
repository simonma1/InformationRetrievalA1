from token_stream import get_token_stream
from spimi import spimi_invert

list = get_token_stream()
block_size = 500000

spimi_invert(list, block_size)


#Could implement block limitation has a limit on terms, but better to use bytes if possible
#Can merge everything in memory, has long as block are saved on disk
#When querying, execute same normalization as before