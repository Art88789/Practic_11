def sort_string(s):
    char_list = list(s)
    char_list.sort()
    return ''.join(char_list)

input_str = input()
result = sort_string(input_str)
print(result)
