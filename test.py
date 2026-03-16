doors = []

for i in range(100):
	doors.append(False)
	
for i in range(100):
	for j in range(100):
		if (j+1) % (i+1) == 0:
			doors[j] = not doors[j]

open = []
for i in range(100):
	if doors[i]:
		open.append(i+1)
		
print(open)	