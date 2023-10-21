def list_to_set_with_delimiter(current_list, delimiter):
    current_str = str(current_list)
    current_str_slipt = current_str.split(delimiter)
    current_set = set(current_str_slipt)
    return current_set


def find_common_participants(first_list, second_list, delimiter=","):
    first_set = list_to_set_with_delimiter(first_list, delimiter)
    second_set = list_to_set_with_delimiter(second_list, delimiter)
    coincidence_set = first_set.intersection(second_set)
    coincidence_list = list(coincidence_set)
    coincidence_list.sort()
    return coincidence_list


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))

