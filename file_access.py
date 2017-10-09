from collections import defaultdict
import ast
import operator

def open_file(filename):
    fileOpen = open(filename, 'r')
    return fileOpen.read()


def save_dict(filename, sorted_dict):
    f = open(filename, 'w')

    for k, v in sorted_dict:
        f.write(k + ' ' + str(v) + '\n')


def read_posting_list(filename):
    opened_file = open(filename, 'r')
    dict = defaultdict(list)

    for line in opened_file:

        line = line.split(' ', 1)
        term = line[0]
        postings = map(int,ast.literal_eval(line[1]))

        dict[term].extend(postings)

    return dict


def merge_postings(postings_list):
    fs = {}
    postings_next_value = {}
    result = defaultdict(list)

    #Open all the postings list file in an array and gives them an id to act as the key
    for index in range(len(postings_list)):
        fs[index] = open(postings_list[index], 'r')

    #gets the first the first line of each files and puts it in the postings_next_value list
    for index in range(len(fs)):
        postings_next_value[index] = fs[index].readline()
        postings_next_value[index] =postings_next_value[index].split(' ', 1)
        postings_next_value[index][1] = map(int, ast.literal_eval(postings_next_value[index][1]))

    #while there is still files opened
    while(len(fs) > 0):
        #finds the first element by alphabetical order
        indexOfEarliestElement = -1
        for posting, value in postings_next_value.items():
            if(indexOfEarliestElement == -1):#if no index has been set, use the first one
                indexOfEarliestElement = posting
            elif(value[0] < postings_next_value[indexOfEarliestElement][0]):#compares the 2 values by alphabetical order
                indexOfEarliestElement = posting

        #adds the result to a result dictionary
        result[postings_next_value[indexOfEarliestElement][0]].extend(postings_next_value[indexOfEarliestElement][1])

        postings_next_value[indexOfEarliestElement] = fs[indexOfEarliestElement].readline()#reads the next line from the file whose value was used
        if(postings_next_value[indexOfEarliestElement] == ''):#if no more data in the file delete its reference
            fs[indexOfEarliestElement].close()
            del fs[indexOfEarliestElement]
            del postings_next_value[indexOfEarliestElement]
        else:
            postings_next_value[indexOfEarliestElement] = postings_next_value[indexOfEarliestElement].split(' ', 1)
            postings_next_value[indexOfEarliestElement][1] = map(int, ast.literal_eval(postings_next_value[indexOfEarliestElement][1]))

    sorted_dict = sorted(result.items(), key=operator.itemgetter(0))
    savefilename = 'results.txt'
    save_dict(savefilename, sorted_dict)

    return savefilename
