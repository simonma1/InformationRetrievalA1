from token_stream import get_token_stream
from spimi import spimi_invert
from file_access import read_posting_list, merge_postings, get_doc_len
from scoring_module import bm_25
import postings_search


escape_layout = "----------------------------"

def indexation():

    memory_size = None
    while (not (isinstance(memory_size, (int, long, float)))):
        try:
            memory_size = input("Enter the desired memory size: \n")
        except:
            print "Please enter a number\n"
    print escape_layout
    print "Tokenizing"
    stream = get_token_stream()
    print "Documents Tokenized"
    print escape_layout
    file_name_list = list()
    print "Executing SPIMI "
    while (len(stream) != 0):
        file_name = spimi_invert(stream, memory_size, len(file_name_list))
        file_name_list.append(file_name)
        print "Remaining: " + str(len(stream))
    print "SPIMI Completed"
    print escape_layout
    print "Merging Postings"
    merge_postings(file_name_list)
    print "Postings Merged"
    print escape_layout

#Comment out this part to only execute queries on the result file
#indexation()

#Get number of words per doc
doc_len_arr = get_doc_len()
l_avg = 0

for doc in doc_len_arr:
    l_avg += doc

l_avg /= (float)(len(doc_len_arr))

#reads in the final posting list
invertedIndex = read_posting_list('results.txt')

continue_queries = True

while continue_queries:
    query = raw_input("Enter the word or words you are looking for. Leave the field blank to stop: ")
    if(query != ""):
        words = query.split()
        result_list = bm_25(doc_len_arr, invertedIndex, words, l_avg)
        print result_list

        for key, value in sorted(result_list.items(), reverse=True):
            print(key, value)
    else:
        print 'Thank you. Have a nice day'
        continue_queries = False

#Unranked search through the postings
# while continue_queries:
#     query = raw_input("Enter the word or words you are looking for. Type 'or' at the end for a conjunctive query. Leave the field blank to stop: ")
#     if(query != ""):
#         words = query.split()
#         if (len(words) == 1):
#             result = postings_search.search(invertedIndex, words[0])
#             print result
#         else:
#             if(words[-1].lower() == 'or'):
#                 del words[-1]
#                 result = postings_search.searchOr(invertedIndex, words)
#                 print result
#             else:
#                 result = postings_search.searchAnd(invertedIndex, words)
#                 print result
#     else:
#         print 'Thank you. Have a nice day'
#         continue_queries = False
