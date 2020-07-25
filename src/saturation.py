def saturation(value, high, low):
	if (value <= low):
		return low
	elif (value < high):
		return value
	else:
		return high
