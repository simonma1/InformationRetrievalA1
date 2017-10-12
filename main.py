from token_stream import get_token_stream
from spimi import spimi_invert
from file_access import read_posting_list
from file_access import merge_postings
import postings_search

memory_size = None
escape_layout = "----------------------------"

while (not(isinstance(memory_size, (int, long, float)))):
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
while(len(stream) != 0):
    file_name = spimi_invert(stream, memory_size, len(file_name_list))
    file_name_list.append(file_name)

print "SPIMI Completed"
print escape_layout

print "Merging Postings"
merge_postings(file_name_list)
print "Postings Merged"
print escape_layout

#reads in the final posting list
invertedIndex = read_posting_list('results.txt')

continue_queries = True

while (continue_queries):
    word_query = []
    word = raw_input("Enter the word you are looking for: ")
    if(word != ""):
        word_query.append(word)
        while (word != ""):
            word = raw_input("Enter another word or leave it blank to stop: ")
            if(word != ""):
                word_query.append(word)
            else:
                if(len(word_query) == 1):
                    result = postings_search.search(invertedIndex, word_query[0])
                    print result
                else:
                    query_type = None
                    while(query_type != 1 and query_type != 2):
                        try:
                            query_type = input("For an AND query enter 1, for an OR query enter 2: \n")
                        except:
                            print "Please enter a number\n"

                    if(query_type == 1):
                        result = postings_search.searchAnd(invertedIndex, word_query)
                        print result
                    elif(query_type == 2):
                        result = postings_search.searchOr(invertedIndex, word_query)
                        print result
        print escape_layout
    else:
        continue_queries = False



#When querying, execute same normalization as before