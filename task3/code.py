# input_line = "one two one tho three"
input_line = "She sells sea shells on the sea shore; The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore, I'm sure that the shells are sea shore shells."
# input_line = 'aba aba; aba @?"'

def previous_index(line=input_line):
    new_list = line.split()

    result = [-1 for i in range(len(new_list))]

    my_dict = {}

    for i in range(len(new_list)):
        if new_list[i] in my_dict:
            result[i] = my_dict[new_list[i]]
            my_dict[new_list[i]] = i
        else:
            my_dict[new_list[i]] = i

    return print(*result)

previous_index(input_line)
