
#In the class Employee, implement the instance attributes as firstname, lastname and salary.

#Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. 
#Properties will be separated by a dash.

#The salary is an integer.



class Employee:

	def __init__(self, prenom, nom, salaire):
		self.prenom=prenom
		self.nom=nom
		self.salaire=int(salaire)
	
	@classmethod
	def from_string(cls, full):
		prenom,nom,salaire=full.split('-')
		return cls(prenom,nom,salaire)
		
emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp1.salaire)
print(emp2.salaire)