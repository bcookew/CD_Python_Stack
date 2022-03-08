from store_class import Store
from product_class import Product

new_world = Store("New World")

shampoo = Product("Shampoo", 5.99, "toiletries")
conditioner = Product("Conditioner", 9.99, "toiletries")
beer = Product("Beer", 4.99, "Alcohol")

new_world.addProduct(shampoo).addProduct(conditioner).addProduct(beer)
print("*"*25,"\nInitail Prices\n", "*"*25)
new_world.listAvail()

print("*"*25,"\nInflation Prices\n", "*"*25)
new_world.inflation(1)
new_world.listAvail()

print("*"*25,"\nClearance Prices\n", "*"*25)
new_world.setClearance("toiletries",0.5)
new_world.listAvail()