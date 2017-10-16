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
