from collections import defaultdict
from copy import deepcopy
from normalization import normalize

def search(dict, term):
    term = normalize(term)
    if(len(dict[term]) == 0):
        return "Sorry no results were found"
    return dict[term]

def searchOr(dict, terms):
    result = []
    for term in terms:
        term = normalize(term)
        result = union(result, deepcopy(dict[term]))
    return result



def searchAnd(dict, terms):
    tempDict = defaultdict(list)
    result = []
    for term in terms:
        term = normalize(term)
        if(term != ""):
            tempDict[term].extend(dict[term])#will get the postings list for each term
            if (len(tempDict[term])==0):
                return "The word you are looking for could not be found."

    # find the smallest index
    smallest_term = findSmallestList(tempDict)
    result.extend(tempDict[smallest_term])
    del(tempDict[smallest_term])

    while (len(tempDict) > 0):
        smallest_term = findSmallestList(tempDict)
        result = intersect(result, deepcopy(tempDict[smallest_term]))
        del (tempDict[smallest_term])

    return result

def union(result, other_list):
    result_next = check_if_list_empty(result)
    other_next = check_if_list_empty(other_list)
    answer = []

    while (result_next != None or other_next != None):
        if(result_next == None):
            answer.insert(len(answer), other_next)
            answer.extend(other_list)
            other_next = None
        elif(other_next == None):
            answer.insert(len(answer), result_next)
            answer.extend(result)
            result_next = None
        else:
            if(other_next < result_next):
                answer.insert(len(answer), other_next)
                other_next = check_if_list_empty(other_list)
            elif(result_next < other_next):
                answer.insert(len(answer), result_next)
                result_next = check_if_list_empty(result)
            else:
                answer.insert(len(answer), result_next)
                result_next = check_if_list_empty(result)
                other_next = check_if_list_empty(other_list)

    return answer

def findSmallestList(dict):
    termOfSmallest = ""
    for term, postings in dict.items():
        if(termOfSmallest == ""):
            termOfSmallest = term
        else:
            if(len(postings) < len(dict[termOfSmallest])):
                termOfSmallest = term

    return termOfSmallest

def intersect(result, other_list):
    result_next = result.pop(0)
    other_next = other_list.pop(0)
    answer = []

    while(result_next != None and other_next != None):

        if(result_next == other_next):
            answer.insert(len(answer),result_next)
            result_next = check_if_list_empty(result)
            other_next = check_if_list_empty(other_list)
        elif(result_next > other_next):
            other_next = check_if_list_empty(other_list)
        else:
            result_next = check_if_list_empty(result)

    return answer


def check_if_list_empty(listing):
    if (len(listing) == 0):
        return None
    else:
        return  listing.pop(0)
