from token_stream import get_token_stream

list = get_token_stream()

print len(list)
print list.pop(0)
print list.pop(len(list) - 7)