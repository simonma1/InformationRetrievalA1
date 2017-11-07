"""
1. Find all the docs that 1 of the terms occurs in, than add it to a dict. DONE
2. For all doc in the list:
    a. Find the RSV for that doc by summing the following for each term in the query:
        I. log of [number of doc in the collection]/ # of doc that term occurs in
        II. the rest of the function where tftd = term frequency in doc d, Ld = length of doc d, and Lavg = avg length of all doc

"""
from collections import defaultdict

import math


def bm_25(doc_len_arr, inverted_index, words, l_avg):
    print "BMMM25"
    result_list = defaultdict(int)
    num_doc_collection = len(doc_len_arr)
    doc_unranked = get_docs_containing_word(inverted_index, words)
    print doc_unranked

    words_freq_dict = get_frequencies(inverted_index, words)

    for doc in doc_unranked:
        d_length = doc_len_arr[doc]
        res = calculate_rsv(num_doc_collection, words_freq_dict, words, doc, d_length, l_avg)
        print res
        result_list[res] = doc
        #add return value to list
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
    k1 = 1.5
    b = 0.75
    for word in words:
        print "------------"
        dft = len(words_freq_dict[word])
        #print words_freq_dict[word]
        if doc in words_freq_dict[word]:
            tf_td = words_freq_dict[word][doc]
        else:
            #If check not done like this would add it to the dict breaking the logic
            tf_td = 0

        log_part = math.log(num_doc_collection/dft)

        numerator = (k1 + 1) * tf_td
        denum = (k1 * ((1 - b) + (b * (d_length/l_avg)))) + tf_td

        word_score = (log_part * numerator)/denum
        score += word_score # does the summation of all the word score for that doc
        # print "NUM: " + str(numerator)
        # print "DENUM: " + str(denum)
        # print "LOOG : " + str(log_part)
        # print "dft: " + str(dft) + " total docs: " + str(num_doc_collection)
        print "------------"


    return score

