arr = [-1,2,0,3,-2]

def attack(arr_data):
	d = {}
	for i in range(len(arr_data)):
		for j in range(i+1, len(arr_data)+1):
			val = arr_data[i:j]
			if 0 in val:
				d[sum(val)] = val
	return d[sorted(d.keys())[-1]]

print(attack(arr))
