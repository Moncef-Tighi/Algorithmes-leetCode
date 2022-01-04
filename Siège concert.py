#Create a function that determines whether each seat can "see" the front-stage. A number can "see" the front-stage if it is strictly greater than the number before it.

def can_see_stage(seats):
	y=0
	while y<len(seats):
		Holder=0
		x=0
		while x<=len(seats):
			if Holder<seats[x][y]:
				Holder=seats[x][y]
			elif Holder>=seats[x][y]:
				return False
			x=x+1
		y=y+1
	return True







Test= [[1, 2, 2], 
[1, 2, 3], 
[4, 4, 4]]
print(can_see_stage(Test))