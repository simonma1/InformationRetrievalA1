from file_access import open_file, save_doc_len
from tokenizer import gettokenlist
from parser_module import create_parsed_text
from token_class import Token
from normalization import normalize
import glob


# Next: normalization which will give a list of terms
# Normalization can include: case folding, number removal, stopword, stemming, Design Decisions(USA vs U-S-A)

def get_token_stream():
    tokenList = list()  # stream of Token objects(term and docId)
    doc_len_arr = []
    for file in glob.glob('Reuters/reut2-0*.sgm'):
        print file
        fileRead = open_file(file)
        documentList = create_parsed_text(fileRead)
        for doc in documentList:
            docTermList, doc_id = parse_doc(doc)
            tokenList.extend(docTermList)

            doc_len_arr.insert(int(doc_id), len(docTermList))

    save_doc_len(doc_len_arr)


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
        return term_list, docId
    else:
        return list(), docId



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
                #To remove duplicates uncomment the following
                #term_dict.append(term)

    return token_list

