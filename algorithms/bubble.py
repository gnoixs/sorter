def bubble(lst, draw_list, GREEN, RED):
	for i in range(len(lst) - 1):
		for j in range(len(lst) - 1 - i):
			num1 = lst[j]
			num2 = lst[j + 1]

			if (num1 > num2):
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				draw_list(lst, {j: GREEN, j + 1: RED}, True)
				yield True

	return lst