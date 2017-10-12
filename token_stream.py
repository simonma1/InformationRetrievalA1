from file_access import open_file
from tokenizer import gettokenlist
from parser_module import create_parsed_text
from token_class import Token


# Next: normalization which will give a list of terms
# Normalization can include: case folding, number removal, stopword, stemming, Design Decisions(USA vs U-S-A)

def get_token_stream():
    fileRead = open_file("Reuters/reut2-000.sgm")
    documentList = create_parsed_text(fileRead)
    tokenList = list()  # stream of Token objects(term and docId)
    for doc in documentList:
        docTermList = parse_doc(doc)
        tokenList.extend(docTermList)


    return tokenList


def parse_doc(doc):
    docId = doc.get('newid')  # gets the id for the document
    # print val('title')
    parsedText = doc.find('body')  # parses the file by body tag
    parsedTitle = doc.find('title') #parses the title tag
    if (parsedText != None):
        parsedText = parsedText.contents  # gets only the content between the tags

        #Adds the term from the title tag
        if(parsedTitle != None):
            parsedText.extend(parsedTitle.contents)#adds the titlt tag to the list of terms to be tokenized

        tokenizedTermList = gettokenlist(parsedText)  # tokenizes the content

        term_list = get_list_of_terms(tokenizedTermList, docId)
        return term_list
    else:
        return list()



def get_list_of_terms(tokenizedTermList, docId):
    token_list = list()
    term_dict = list()
    # Loops through all the terms in the document and adds them to the list with their associated docId
    for term in tokenizedTermList:
        term = normalize(term)
        if term != '':
            if(not(term in term_dict)):
                tokenObj = Token(term.encode('UTF8'), docId.encode('UTF8'))
                token_list.append(tokenObj)
                term_dict.append(term)
                # print tokenObj

    return token_list

def normalize(term):
    term = removePunctuation(term)
    term = removeStopwords(term)
    term = term.lower()
    return term

def removePunctuation(term):
    symbols = ['.', ',', '!', '?', '\'s', ';', '>', '(', ')', '#', '\'']
    for sym in symbols:
        term = term.replace(sym, '')

    return term

def removeStopwords(term):
    stop_words = ['a', 'the', 'is', 'and', '&']
    for word in stop_words:
        if word == term:
            return ''

    return term


'''
1. get id from newid \\\
2. create function to parse title and text
3. associate the id to each token in inverted index\\\
4. Repeat for all document in the folder 
'''



# Minimum to tokenize is title and text
# Take docId from reteurs element newid
