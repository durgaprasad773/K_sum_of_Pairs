def convert_str_to_int(int_list):
    new_list=[]
    for num in int_list:
        int_num = int(num)
        new_list.append(int_num)
    return new_list


def get_unique_pairs(int_list, pair_sum):
    stop_index = len(int_list) - 1
    unique_pairs_set = set()
    
    for cur_index in range(stop_index):
        num_1 = int_list[cur_index]
        num_2 = pair_sum - num_1
        remining_list = int_list[cur_index+1:]
        if num_2 in remining_list:
            pair = (num_1, num_2)
            sorted_pair = tuple(sorted(pair))
            unique_pairs_set.add(sorted_pair)
    return unique_pairs_set


str_num_list = input().split(",")
pair_sum = int(input())

int_list = convert_str_to_int(str_num_list)

unique_pairs = get_unique_pairs(int_list , pair_sum )

for pair in unique_pairs:
    print(pair)