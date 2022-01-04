"""In this challenge, you have to build a class that will store and manipulate the data of a simplified clone of Battleship, the popular strategy game.

The game is played on a 5x5 square board, with rows indexed by uppercase letters from A to E (from top to bottom), and columns indexed by numbers from 1 to 5 (from left to right).

Rules of the Game
There are two types of ship: the Patrol and the Cruiser. The Patrol occupies a single cell, the Cruiser occupies two cells, horizontally or vertically.
Three Patrols and three Cruisers will be placed randomly in the grid, without ships adjacent in rows and columns (in particular, two adjacent cells can only both be ship cells if they belong to the same Cruiser).
The player calls six different cells, trying to guess if there's a Patrol or a Cruiser in it.
Hits and misses are recorded on the board. For every hit Patrol or Cruiser, a point is gained, and if a Cruiser is sunk, two additional points are gained.
Class "Battleship"
Each instance of the Battleship class in the Tests tab will be declared with two parameters:

scheme is a list containing 9 strings which are the coordinates indicating where the ships are placed on the board.
guesses is a list containing 6 strings which are the coordinates of the guesses made by the player.
What do you have to implement?
The Tests will expect each instance of the Battleship class to possess four methods:

board() will return the final state of the board, based on the placement of the ships and the results of the player guesses, as a matrix of size 5x5. To vizually represent the state of the game, you will use four different characters:

' ' = a blank space on the board.
's' = a space occupied by a ship.
'.' = a miss (wrong guess).
'X' = a hit (a correct guess).
hits() will return the total number of hits made by the player (correct guesses), either on Patrols or on Cruisers.

sunk() will return the total number of sunk Cruisers (two adjacent correct guesses, either horizontally or vertically).
points() will return the total number of points gained by the player (1 for every hit, plus 2 for every sunk Cruiser)."""


# CHARACTER SET
# " " -> empty
# "s" -> ship
# "." -> miss
# "X" -> hit

class Battleship:
	#Le board est donné en format 'A1', 'C2' donc on va d'abord le traduire en chiffre pour pouvoir ittérer dessus
	translation_board={ "A1":"00","A2":"01","A3":"02","A4":"03","A5":"04",
						"B1":"10","B2":"11","B3":"12","B4":"13","B5":"14",
						"C1":"20","C2":"21","C3":"22","C4":"23","C5":"24",
						"D1":"30","D2":"31","D3":"32","D4":"33","D5":"34",
						"E1":"40","E2":"41","E3":"42","E4":"43","E5":"44",}

	def __init__(self, scheme, guesses):
		self.scheme=scheme
		self.guesses=guesses
		self.hit=0
		self.sink=0
		self.result=[[ ' ', ' ', ' ', ' ', ' ' ],
  					 [ ' ', ' ', ' ', ' ', ' ' ],
  					 [ ' ', ' ', ' ', ' ', ' ' ],
  					 [ ' ', ' ', ' ', ' ', ' ' ],
  					 [ ' ', ' ', ' ', ' ', ' ' ]]

	def board(self):
		x=0
		y=0
		for key in Battleship.translation_board:
			holder=Battleship.translation_board[key]
			x=int(holder[0])
			y=int(holder[1])
			if (key in self.scheme) and (key in self.guesses): #Si key est dans les emplacements des bateaux ET dans la réponse ça touche
				self.result[x][y]="X"
				self.hit+=1
			elif key in self.scheme:
				self.result[x][y]="s"
			elif key in self.guesses: #Si elle est dans les guesses mais pas dans le scheme, c'est manqué
				self.result[x][y]="."
		return self.result
	def hits(self):
		return self.hit

	def sunk(self):
		holder=""
		x=0
		y=0
		while x<=4:
			while y<=4:
				if self.result[x][y]=='X' and self.result[x][y]==holder: #Dans le cas ou un battleship est détruit horizontalement
					self.sink+=1
				else:
					holder=self.result[x][y]
				if x<4: #Dans le cas ou un battleship est détruit verticalement (haut vers bas)
					if self.result[x][y]=='X' and self.result[x+1][y]=="X":
						self.sink+=1
				elif x>0 and x>4:   #Dans le cas ou un battleship est détruit verticalement (bas vers haut) la deuxième condition c'est pour éviter la répétition
					if self.result[x][y]=='X' and self.result[x-1][y]=="X":
						self.sink+=1
				y+=1
			y=0
			x+=1
		return self.sink

	def points(self):
		return (self.sink*2)+self.hit

scheme1 = ["A1", "C1", "B2", "B3", "D2", "E2", "E4", "E5", "A5"]
scheme2 = ["A1", "B1", "D1", "E1", "A3", "A4", "D3", "E4", "D5"]
scheme3 = ["A2", "A4", "C1", "C2", "E3", "C4", "C5", "D3", "E5"]
guesses1 = ["A1", "B2", "C3", "D4", "E5", "E4"]
guesses2 = ["A2", "B4", "C1", "D3", "E5", "A5"]
guesses3 = ["A1", "B1", "D1", "E1", "A3", "A4"]



battleship1=Battleship(scheme2, guesses3);
print(battleship1.board())
x=battleship1.hits()
print(x)
print(battleship1.sunk())
print(battleship1.points())






"""Notes
If two cruisers are in the same row or the same column, there will be a blank cell between them, so that it will be possible to distinguish them as different ships.
The board is not given, you have to build it.
In the Examples above, the symbols in the board are not between quotation marks for readability, but they are strings.


"""
