def remove_min (lst):
    min_val = list[0]
    min_idx = 0
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
            min_idx = i

    new_lst = lst[:min_idx] + lst[min_idx+1:]

    return new_lst