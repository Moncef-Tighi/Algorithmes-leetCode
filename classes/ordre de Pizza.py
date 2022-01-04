
#Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
# Only the ingredients will be given as input.

#You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually!
# As well as creating this Pizza class, hard-code the following pizza flavours.



class Pizza:
	order_number=0
	def __init__(self,ingredients):
		Pizza.order_number+=1
		self.order_number=Pizza.order_number
		self.ingredients=ingredients
	def hawaiian():
		obj= Pizza(["ham", "pineapple"])
		return obj
	def meat_festival():
		obj= Pizza(["beef", "meatball", "bacon"])
		return obj
	def garden_feast():
		obj= Pizza(["spinach", "olives", "mushroom"])
		return obj