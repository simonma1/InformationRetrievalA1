from collections import defaultdict

def search(dict, term):
    if(len(dict[term]) == 0):
        return "Sorry no results were found"
    return dict[term]


def searchAnd(dict, terms):
    tempDict = defaultdict(list)
    result = []
    for term in terms:
        tempDict[term].extend(dict[term])#will get the postings list for each term
        if (len(tempDict[term])==0):
            return "The word you are looking for could not be found."

    # find the smallest index
    smallest_term = findSmallestList(tempDict)
    result.extend(tempDict[smallest_term])
    del(tempDict[smallest_term])

    while (len(tempDict) > 0):
        smallest_term = findSmallestList(tempDict)
        result = intersect(result, tempDict[smallest_term])
        del (tempDict[smallest_term])

    return result



def findSmallestList(dict):
    termOfSmallest = ""
    for term, postings in dict.items():
        if(termOfSmallest == ""):
            termOfSmallest = term
        else:
            if(len(postings) < len(dict[termOfSmallest])):
                termOfSmallest = term

    return termOfSmallest

def intersect(result, otherList):
    result_next = result.pop(0)
    other_next = otherList.pop(0)
    answer = []

    while(result_next != None and other_next != None):

        if(result_next == other_next):
            answer.insert(len(answer),result_next)
            result_next = check_if_list_empty(result)
            other_next = check_if_list_empty(otherList)
        elif(result_next > other_next):
            other_next = check_if_list_empty(otherList)
        else:
            result_next = check_if_list_empty(result)

    return answer


def check_if_list_empty(listing):
    if (len(listing) == 0):
        return None
    else:
        return  listing.pop(0)
