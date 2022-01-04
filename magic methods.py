class Number:

	def __init__(self,number):
		self.number=number

	def __int__(number):
		if isinstance(number, Number)==True:
			return int(number.number) 
		return int(number)     # Used in the "int" method
	def __float__(number):
		if isinstance(number, Number)==True:
			return float(number.number)
		return float(number)   # Used in the "float" method	
	def __str__(number):
		if isinstance(number, Number)==True:
			return str(number.number)
		return str(number)     # Used in the "str" method
	def __repr__(self):
		return str(self.number)
		    # Used in the "repr" method
	def __add__(self,other):
		if isinstance(other,Number)==True:
			return self.number+other.number
		return self.number+other     # Used in the "+" operator function
	def __sub__(self,other):
		if isinstance(other,Number)==True:
			return self.number-other.number
		return self.number-other     # Used in the "-" operator function
	def __mul__(self,other):
		if isinstance(other,Number)==True:
			return self.number*other.number
		return self.number*other     # Used in the `*` operator function
	def __truediv__(self,other):
		if other==0:
			return "ZeroDivisionError"
		if isinstance(other,Number)==True:
			return self.number/other.number
		return self.number/other # Used in the "/" operator function
	def __floordiv__(self,other):
		if isinstance(other,Number)==True:
			return self.number//other.number
		return self.number//other # Used in the "//" operator function
	def	__eq__(self,other):
		if self.number==other:
			return True
		return False
	def __ne__(self,other):
		if self.number!=other:
			return True
		return False
	def __lt__(self,other):
		if self.number<other:
			return True
		return False
	def __le__(self,other):
		if self.number<=other:
			return True
		return False
	def __gt__(self,other):
		if self.number>other:
			return True
		return False
	def __ge__(self,other):
		if self.number>=other:
			return True
		return False
