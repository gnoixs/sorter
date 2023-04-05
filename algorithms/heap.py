def heapify(lst, n, i, draw_list, GREEN, RED):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and lst[i] < lst[l]:
        largest = l

    if r < n and lst[largest] < lst[r]:
        largest = r

    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        draw_list(lst, {i: RED, largest: GREEN}, True)
        yield True

        yield from heapify(lst, n, largest, draw_list, GREEN, RED)


def heap(lst, draw_list, GREEN, RED):
    n = len(lst)

    for i in range(n, -1, -1):
        yield from heapify(lst, n, i, draw_list, GREEN, RED)

    for i in range(n-1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_list(lst, {i: GREEN, 0: RED}, True)
        yield True

        yield from heapify(lst, i, 0, draw_list, GREEN, RED)

    return lst
