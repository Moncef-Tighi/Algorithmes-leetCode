"""Given a dictionary containing quarterly sales values for a year, return a string representing a bar chart of the sales by quarter.

Quarter names (Q1, Q2, Q3, Q4) should appear on the left.
Quarters should be sorted in descending order by value.
Quarters with the same value should be shown in their yearly order (Q1 - Q4).
Bars should begin with a " | ".
Repeat the character # to fill the bar, with each character having a value of 50.
A single space comes after the bar, then the sales for that quarter.
If the value is 0, there should be no space after .
Use the newline character (n) to separate each bar in the chart."""


def bar_chart(results):

	def sorting(diction):
		sorted_values=sorted(diction.values(), reverse=True)
		sorted_dict={}
		for value in sorted_values:  #Here, we sort based on values
			for key in diction.keys():
				if diction[key]==value:
					sorted_dict[key]=diction[key]
		#If there is two equal values, we need to sort based on Quarter
		order=["Q1","Q2","Q3","Q4"]
		hold=0
		result={}
		for key in sorted_dict:
			if hold==sorted_dict[key]: #What this does : If there is a repeat value, go in the loop and lookup the order of quarters,
				for key in order:
					if sorted_dict[key]==hold:
						result[key]=sorted_dict[key]
			else: # Else just keep it normal.
				result[key]=sorted_dict[key]
			hold=value

		return result
	
	diction={}
	diction=sorting(results)
	print(diction)
	result=""
	for key in diction:
		result=result + key + "|"
		number_of_bar=diction[key]/50
		if number_of_bar==0:
			result=result + "0" + "\n"
		else :
			while number_of_bar>0:
				result=result + "#"
				number_of_bar-=1
			result=result+ " " + str(diction[key]) + "\n"

	return result





print(bar_chart({'Q4': 0, 'Q3': 100, 'Q2': 0, 'Q1': 600}))
print(bar_chart({'Q4': 100, 'Q1': 500, 'Q2': 50, 'Q3': 200}))
print(bar_chart({'Q4': 150, 'Q3': 0, 'Q2': 0, 'Q1': 450}))