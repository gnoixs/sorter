def merge(lst, draw_list, GREEN, RED):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]

        yield from merge(left, draw_list, GREEN, RED)
        yield from merge(right, draw_list, GREEN, RED)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1

            k += 1

            draw_list(lst, {i+j-1: GREEN}, True)
            yield True

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

            draw_list(lst, {i+j-1: GREEN}, True)
            yield True

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1

            draw_list(lst, {i+j-1: GREEN}, True)
            yield True

    return lst
