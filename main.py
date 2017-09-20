from file_access import open_file
from tokenizer import gettokenlist
from parser_module import create_parsed_text


fileRead = open_file("Reuters/reut2-000.sgm")

soup = create_parsed_text(fileRead)


titleList = soup('title')

print gettokenlist(titleList)






