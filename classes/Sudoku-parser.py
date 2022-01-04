"""Create a class Sudoku that takes a string as an argument.
 The string will contain the numbers of a regular 9x9 sudoku board left to right and top to bottom, with zeros filling up the empty cells.

Attributes :
	
	An instance of the class Sudoku will have one attribute:

	board: a list representing the board, with sublits for each row, with the numbers as integers. Empty cell represented with 0.
		Methods
	

An instance of the class Sudoku wil have three methods:

	get_row(n): will return the row in position n.
	get_col(n): will return the column in position n.
	get_sqr([n, m]): will return the square in position n if only one argument is given, 
		and the square to which the cell in position (n, m) belongs to if two arguments are given."""



class Sudoku:
	
	def __init__(self,bor):
		self.bor=bor
		board=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0],
			   [0, 0, 0, 0, 0, 0, 0, 0, 0]]
		i,y,z=0,0,0
		while i<len(board):
			while y<len(board):
				board[i][y]=int(bor[z])
				y+=1
				z+=1
			i+=1
			y=0
		self.board=board
	def get_row(self,n):
		i=0
		result=[]
		for i in range(0,len(self.board)):
			result.append(self.board[n][i])
		return result
	def get_col(self,n):
		i=0
		result=[]
		for i in range(0,len(self.board)):
			result.append(self.board[i][n])
		return result
	def get_sqr(self,*args):
		if len(args)==1: #Not the best implementation, mais c'est dans le cas où on a qu'un argument faut le convertir en n, m. Flem de recoder juste pour ce cas
			n,m=1,1
			i=args[0]
			while i>0:
				m=3+1
				i-=1
				if i>0:
					m=m+3
					i-=1
				if i>0:
					m=1
					if n>1:
						n=n+3
					else:	
						n=3+1
					i-=1
		else:
			n,m=args[0],args[1]
		#First, we find the middle of the square		
		if n%3!=1:
			if n%3>1:
				n-=1
			if n%3<1:
				n+=1
		if m%3!=1:
			if m%3>1:
				m-=1
			if m%3<1:
				m+=1
		result=[]
		x=-1
		y=-1
		while x<2:
			while y<2:
				result.append(self.board[n+x][m+y])
				y+=1
			y=-1
			x+=1
		return result

g1 = Sudoku("005001000287369100416520000000700692000000000000806453843000000000930000950074200")
print(g1.board)
print(g1.get_sqr(2))

""" [[0, 0, 5, 0, 0, 1, 0, 0, 0],
 	 [2, 8, 7, 3, 6, 9, 1, 0, 0],
 	 [4, 1, 6, 5, 2, 0, 0, 0, 0], 
  	 [0, 0, 0, 7, 0, 0, 6, 9, 2], 
  	 [0, 0, 0, 0, 0, 0, 0, 0, 0], 
  	 [0, 0, 0, 8, 0, 6, 4, 5, 3], 
  	 [8, 4, 3, 0, 0, 0, 0, 0, 0], 
  	 [0, 0, 0, 9, 3, 0, 0, 0, 0], 
  	 [9, 5, 0, 0, 7, 4, 2, 0, 0]]


	  1,1  1,4 1,7
	  4,1  4,4 4,7
	  7,1  7,4 7,7"""
