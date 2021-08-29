def sort_anagrams(list_of_strings):
    new_list = []
    for item in list_of_strings:
        tmp_list = [item]
        for comp in list_of_strings:
            if comp not in tmp_list:
                if sorted(comp) == sorted(item):
                    tmp_list.append(comp)
                    tmp_list.sort()
        if not sorted(tmp_list) in sorted(new_list):
            new_list.append(tmp_list)
    return new_list        