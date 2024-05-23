
surfaces = [1.5, 12, 45, 56, 72, 90, 78, 100, 340, 400, 30]  # test values. in real program this dataset need to be extract form the list

def find_quadrant_dimensions(surface):
	best_pair = (1, surface)
	closest_difference = abs(1-surface)

	for i in range(2, int(surface ** 0.5) + 1):
		if surface % i == 0:
			j = surface // i
			difference = abs(i - j)
			if difference < closest_difference:
				closest_difference = difference
				best_pair = (i, j)
	return best_pair



y_dimensions = []
x_dimensions = []
for surface in surfaces:
	x,y = find_quadrant_dimensions(surface)
	x_dimensions.append(x)
	y_dimensions.append(y)


print(x_dimensions, y_dimensions)
