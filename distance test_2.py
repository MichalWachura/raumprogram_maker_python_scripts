def cumulative_sum_with_constant(input_list, constant):
	if not input_list:
		return []

	result = [input_list[0] + constant]
	for i in range(1, len(input_list)):
		result.append(result[-1] + input_list[i] + constant)

	return result


# Przykład użycia
input_list = [1, 2, 3, 4, 5]
constant = 2
new_list = cumulative_sum_with_constant(input_list, constant)
print(new_list)