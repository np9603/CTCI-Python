"""

"""

string = "Mr John Smith    "
true_length = 13

def urlify1(string,length):

    return string.strip().replace(" ","%20")

print(urlify1(string,true_length))

def urlify2(string,length):
    char_list = list(string)
    string = ""
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":
            # Replace spaces
            char_list[new_index - 3: new_index] = "%20"
            new_index -= 3
        else:
            # Move characters
            char_list[new_index - 1] = char_list[i]
            new_index -= 1
    # convert back to string
    return string.join(char_list)

print(urlify2(string,true_length))