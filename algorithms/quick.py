def quick(lst, draw_list, GREEN, RED):
    def partition(lst, low, high):
        pivot = lst[high]
        i = low - 1
        for j in range(low, high):
            if lst[j] <= pivot:
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                draw_list(lst, {i: GREEN, j: RED, high: RED}, False)
                yield False
        lst[i+1], lst[high] = lst[high], lst[i+1]
        draw_list(lst, {i+1: GREEN, high: RED}, False)
        yield False
        return i+1

    def quick_helper(lst, low, high):
        if low < high:
            pivot_idx = yield from partition(lst, low, high)
            yield from quick_helper(lst, low, pivot_idx - 1)
            yield from quick_helper(lst, pivot_idx + 1, high)

    yield from quick_helper(lst, 0, len(lst) - 1)
    draw_list(lst, {}, True)
    return lst
