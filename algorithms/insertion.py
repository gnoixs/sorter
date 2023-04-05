def insertion(lst, draw_list, GREEN, RED):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
            draw_list(lst, {j + 1: GREEN, j + 2: RED}, True)
            yield True
        lst[j + 1] = key
    return lst