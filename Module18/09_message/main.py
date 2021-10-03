import string

def back (word):

    word_list = word.split("!" or '"' or "#" or "$" or "%" or "&" or
                           "'" or "(" or ")" or "*" or "+" or "," or
                           "-" or "." or "/" or ":" or ";" or "<" or
                           "=" or ">" or "?" or "@" or "[" or '\ ' or
                           "]" or "^"or "_" or "`" or "{" or "|" or "}" or "~")

    #for simble in

    return word

message_string = input("Input string: ")
message_list = message_string.split(" ")

for word in message_list:
    word = back(word)