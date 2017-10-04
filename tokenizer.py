import nltk

#Download the necessary library
#nltk.download('punkt')

from nltk.tokenize import word_tokenize


def gettokenlist(list):
    tokenList = []

    for text in list:
        titleToken = nltk.word_tokenize(text.string)
        #print text.string
        tokenList += titleToken

    return tokenList


#example
# s1 = "hello my name is gipsy"
# s2 = nltk.word_tokenize(s1)
