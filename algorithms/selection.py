def selection(lst, draw_list, GREEN, RED):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
            draw_list(lst, {i: GREEN, j: RED, min_idx: RED}, True)
            yield True
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst