distance = 3

list_of_x_dimension = [2, 23, 34, 54, 12, 54, 2, 55, 67, 84, 112, 125, 64, 12]

cumsum = 0
list_of_positions = [0]
for i in range(len(list_of_x_dimension)):
	cumsum = cumsum + list_of_x_dimension[i] + distance
	list_of_positions.append(cumsum)


print(list_of_positions)