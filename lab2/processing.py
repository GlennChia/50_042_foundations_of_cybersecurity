character_counter = {45: 230, 62: 280, 46: 559, 79: 750, 50: 1292, 12: 357, 
        124: 315, 117: 36, 89: 115, 73: 466, 88: 91, 9: 167, 
        99: 454, 75: 347, 70: 142, 95: 105, 116: 448, 59: 178, 
        69: 271, 32: 149, 115: 48, 60: 67, 39: 102, 86: 51, 
        112: 146, 101: 95, 87: 76, 123: 4, 118: 7, 82: 7, 51: 48, 
        102: 4, 10: 1}

def sort_counts_into_list(char_counter):
    sorted_x = sorted(char_counter.items(), key=lambda kv: kv[1], reverse=True)
    print('The Sorted Character Counts is: \n{}'.format(sorted_x))
    len_sorted_x = len(sorted_x)
    print('The number of unique characters is: {}\n'.format(len_sorted_x))
    return sorted_x

'''
[(50, 1292), (79, 750), (46, 559), (73, 466), (99, 454), (116, 448), 
(12, 357), (75, 347), (124, 315), (62, 280), (69, 271), (45, 230), 
(59, 178), (9, 167), (32, 149), (112, 146), (70, 142), (89, 115), 
(95, 105), (39, 102), (101, 95), (88, 91), (87, 76), (60, 67), 
(86, 51), (115, 48), (51, 48), (117, 36), (118, 7), (82, 7), 
(123, 4), (102, 4), (10, 1)]
'''

def format_sorted_list_into_sorted_dict(sorted_list):
    formatted_str = '{ '
    for index_outer, individual_tuple in enumerate(sorted_list):
        for index_inner, individual_element in enumerate(individual_tuple):
            if index_inner == 1:
                formatted_str += ': '
                formatted_str += str(individual_element)
            else:
                formatted_str += str(individual_element)
        if index_outer < len(sorted_list)  -1:
            formatted_str += ', '
        else:
            formatted_str += ' }'
    print('The formatted mapping is: \n{}'.format(formatted_str))
    return formatted_str


sorted_list = sort_counts_into_list(character_counter)
formatted_mapping = format_sorted_list_into_sorted_dict(sorted_list)

