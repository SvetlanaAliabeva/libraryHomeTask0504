input_line = "one two one two three"


def count_reps(line=input_line):
    new_list = line.split()

    my_dict = {}
    word_list = []

    for word in new_list:
        if word not in my_dict:
            my_dict[word] = 0
        else:  # в противном случае
            my_dict[word] += 1
            
        word_list.append(my_dict[word])

    return print(*word_list)

count_reps(input_line)
