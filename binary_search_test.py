"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def bin_search(input_array, value):
	"""Your code goes here."""
	index=0
	index=int(round(len(input_array)/2))
	list_size= int(round(len(input_array)/2))
	while (index<=len(input_array)) or (index>0) or (list_size==0):
		print(index)
		if value == input_array[index]:
			return index
		if value > input_array[index]:
			index = index + int(round(list_size/2))
			list_size= int(round(list_size/2))
		if value < input_array[index]:
			index = index- int(round(index/2))
	return -1

test_list = [1,2,3,9,11,15,19,25,29]
test_val2 = 15
test_val3 = 2
print(bin_search(test_list, test_val2))
print(bin_search(test_list, test_val3))
