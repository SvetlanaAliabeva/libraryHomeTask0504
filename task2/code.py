input_line = "apple orange banana banana orange"
# input_line = "a s d f g h j k l"
# input_line = 'aba aba; aba @?"'

def most_often(line=input_line):

    new_list = line.split()
    my_dict = {}
    word_list = []

    for word in new_list:
        if word not in my_dict:
            my_dict[word] = 0
        else:
            my_dict[word] += 1

    for k, v in my_dict.items():
        if v >= max(my_dict.values()):
            word_list.append(k)

    return print(sorted(word_list)[0])

most_often(input_line)
