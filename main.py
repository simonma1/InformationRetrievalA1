from token_stream import get_token_stream
from spimi import spimi_invert
from file_access import read_posting_list
from file_access import merge_postings
import postings_search

# stream = get_token_stream()
# block_size = 500000
# file_name_list = list()
#
# while(len(stream) != 0):
#     file_name = spimi_invert(stream, block_size, len(file_name_list))
#     file_name_list.append(file_name)

# print file_name_list

file_name_list = ['savefile0.txt', 'savefile1.txt', 'savefile2.txt', 'savefile3.txt']

merge_postings(file_name_list)

#reads in the final posting list
#postings = read_posting_list('savefile0.txt')

#result = postings_search.searchAnd(postings, ['will', 'with', 'which'])


#Merge files:
#open buffer to all files
#Find term with highest priority
#Merged all postings list for that term
#Write to disk
#Get next postings from that block





#Could implement block limitation has a limit on terms, but better to use bytes if possible
#Can merge everything in memory, has long as block are saved on disk
#When querying, execute same normalization as before