#A group of n prisoners stand in a circle awaiting execution.
 #Starting from an arbitrary position(0), the executioner kills every kth person until one person remains standing, who is then granted freedom 

#Create a function that takes 2 arguments — the number of people to be executed n, and the step size k, and returns the original position (index)
 #of the person who survives.

def who_goes_free(n, k):
	i=0
	prisoners=[]
	while i<n:
		prisoners.append(i)
		i=i+1
	N=k
	while len(prisoners)>1:
		Death-liste=[]
		for prisoner in prisoners:
			N=N-1
			if (N==0) and (len(prisoners)>1):
				#print(number)
				Death-liste.append(prisoner)
				N=k
		for death in Death-liste:
			if len(prisoners)>1:
				prisoners.remove(death)
	free=prisoners[0]
	return free

x= who_goes_free(9,3)
print(x)
















# [0, 1, 2, 3, 4, 5, 6, 7, 8]
# [0, 1, -, 3, 4, -, 6, 7, -] -> [0, 1, 3, 4, 6, 7]
# [0, 1, -, 4, 6, -] -> [0, 1, 4, 6]
# [0, 1, -, 6] -> [0, 1, 6]
# [0, -, 6] -> [0, 6]
# [0, -] -> [0]
