
class Bicycle(object): 
	def __init__(self, modelname, weight, cost):
		self.modelname = modelname
		self.weight = weight
		self.cost = cost 

	def margin(self, cost): 
		self.cost = cost 
		return cost * 1.2

class BikeShop(object): 
	def __init__(self, shopname, inventory, margin, profit):
		self.shopname = shopname
		self.inventory = inventory 
		self.margin = margin 
		self.profit = profit 

class Customer(object): 
	def __init__(self, name, funds, owner):
		self.name = name
		self.funds = funds
		self.owner = owner 

bike1 = Bicycle("Trek1", "2.5", "100")
bike2 = Bicycle("Trek2", "5", "150")
bike3 = Bicycle("Trek3", "7", "300")
bike4 = Bicycle("Felt1", "8", "450")
bike5 = Bicycle("Felt2", "10", "600")
bike6 = Bicycle("Felt3", "8", "800")

bikecost = [bike1.cost, bike2.cost, bike3.cost, bike4.cost, bike5.cost, bike6.cost]

#bikeshop1 = BikeShop("ABC Bikes", [bike1, bike2, bike3, bike4, bike5, bike6], .2, 500)

#print bikecost

for i in bikecost:
	if i < "200":  
		print 


customer1 = Customer("Bob", "200", True)
customer2 = Customer("George", "500", True)
customer3 = Customer("Max", "1000", True)

