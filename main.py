from token_stream import get_token_stream
from spimi import spimi_invert

stream = get_token_stream()
block_size = 500000
file_name_list = list()

while(len(stream) != 0):
    file_name = spimi_invert(stream, block_size, len(file_name_list))
    file_name_list.append(file_name)

print file_name_list

#Merge files:
#open buffer to all files
#Find term with highest priority
#Merged all postings list for that term
#Write to disk
#Get next postings from that block





#Could implement block limitation has a limit on terms, but better to use bytes if possible
#Can merge everything in memory, has long as block are saved on disk
#When querying, execute same normalization as before