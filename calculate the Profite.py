#You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
#You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory.
# Return the total profit made, rounded to the nearest dollar.

def profit(info):
	x=info["cost_price"]
	y=info["sell_price"]
	z=info["inventory"]
	result=(y-x)*z
	return round(result)

