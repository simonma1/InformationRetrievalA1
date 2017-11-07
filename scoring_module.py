from collections import defaultdict
from normalization import normalize

import math

K1 = 1.5
K3 = 1.5
B = 0.75


def bm_25(doc_len_arr, inverted_index, words, l_avg):
    print "EXECUTING BM25"
    result_list = defaultdict(int)
    num_doc_collection = len(doc_len_arr)
    doc_unranked = get_docs_containing_word(inverted_index, words)

    print words
    for w in words:
        term = normalize(w)
        if term == "":
            words.remove(w)
    print words


    words_freq_dict = get_frequencies(inverted_index, words)

    for doc in doc_unranked:
        d_length = doc_len_arr[doc]
        res = calculate_rsv(num_doc_collection, words_freq_dict, words, doc, d_length, l_avg)
        result_list[res] = doc
        #adds return value to list where the score is the key and the doc the value
    return result_list

def get_docs_containing_word(inverted_index, words):
    result = []
    for word in words:
        word_indexes = inverted_index[word]
        for idx in word_indexes:
            if idx not in result:
                result.append(idx)

    return result

def get_frequencies(inverted_index, words):
    # A list dictionary with the word as the key to a dictionary of doc as key and frequency in that doc as value
    words_freq_dict = defaultdict(dict)
    for word in words:
        word_freq_dict = defaultdict(int) # doc-frequency dictionary
        word_occurence_list = inverted_index[word]#the list of all occurences as docId of the term
        #for every index in the postings, counts the frequency of the term in that doc
        for idx in word_occurence_list:
            if idx not in word_occurence_list:
                word_freq_dict[idx] = 1
            else:
                word_freq_dict[idx] += 1
        words_freq_dict[word] = word_freq_dict
    return words_freq_dict


def calculate_rsv(num_doc_collection, words_freq_dict, words, doc, d_length, l_avg):
    score = 0
    for word in words:
        dft = len(words_freq_dict[word])
        #print words_freq_dict[word]
        if doc in words_freq_dict[word]:
            tf_td = words_freq_dict[word][doc]
        else:
            #If check not done like this would add it to the dict breaking the logic
            tf_td = 0

        if(dft != 0):#To prevent division by 0 errors
            log_part = math.log(num_doc_collection/dft)
        else:
            log_part = 0

        numerator = (K1 + 1) * tf_td
        denum = (K1 * ((1 - B) + (B * (d_length/l_avg)))) + tf_td

        word_score = (log_part * numerator)/denum
        score += word_score # does the summation of all the word score for that doc

        tf_tq = 0
        if len(words) > 3: # For long queries only
            #Takes into account how often the word was in the query
            for w in words:
                if word == word:
                    tf_tq += 1
            long_query_score = (((K3 + 1)*tf_tq))/(K3 + tf_tq)

    return score

