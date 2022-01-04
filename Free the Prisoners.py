#A prison can be represented as a list of cells. Each cell contains exactly one prisoner. 
#A 1 represents an unlocked cell and a 0 represents a locked cell.

#Starting inside the leftmost cell, you are tasked with seeing how many prisoners you can set free, with a catch.
# You are the prisoner in the first cell. If the first cell is locked, you cannot free anyone. 
#Each time you free a prisoner, the locked cells become unlocked, and the unlocked cells become locked again.


#You are the prisoner in the first cell. You must be freed to free anyone else.

#You must free a prisoner in order for the locks to switch. 
#So in the second example where the input is [1, 1, 1] after you release the first prisoner, the locks change to [0, 0, 0].
# Since all cells are locked, you can release no more prisoners.

#You always start within the leftmost element in the list (the first prison cell). 
#If all the prison cells to your right are zeroes, you cannot free any more prisoners.

def freed_prisoners(prison):
	def switch(jail):
		i=0
		while i<len(jail):
			if jail[i] == 0:
				jail[i]= 1
			else:
				jail[i]= 0
			i=i+1
		return jail
	free=0
	x=0
	if prison[0]==0:
		return free
	while x<len(prison):
		if prison[x]==1:
			free=free+1
			prison=switch(prison)
			print(prison)
		x=x+1
	return free

r=freed_prisoners([1, 0, 0, 0, 0, 0, 0])
print(r)
