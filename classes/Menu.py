#Create a class that imitates a select screen. For simplicity, the cursor can only move right!

#In the display method, return a string representation of the list, but with square brackets around the currently selected element.
# Also, create the method to_the_right, which moves the cursor one element to the right.

#The cursor should start at index 0.





class Menu:
	def __init__(self, liste):
		self.liste=liste
		self.index=0
	
	def to_the_right(self):
		self.index+=1
		if self.index>=len(self.liste):
			self.index=0	

	def display(self):
		x=0
		text="["
		while x<len(self.liste):
			if x==self.index:
				if type(self.liste[x])==str:
					text=text + "['" + str(self.liste[x]) + "'], "
				else:
					text=text + "[" + str(self.liste[x]) + "], "
			else:
				if type(self.liste[x])==str:
					text=text + "'" + str(self.liste[x]) + "', "
				else:
					text=text + str(self.liste[x]) + ", "
			x+=1
		text= text[:-1]
		text=text[:-1]
		return text + "]"

menu = Menu(["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
menu.to_the_right()
menu.to_the_right()
menu.to_the_right()

print(menu.display())