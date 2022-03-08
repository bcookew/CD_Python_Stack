import product_class

class Store:
    def __init__(self, name, products=[]):
        self.name = name
        self.products = products

    def addProduct(self, newProduct):
        self.products.append(newProduct)
        return self

    def sellProduct(self, id):
        self.products.pop(id)
        return self

    def inflation(self, percentage):
        for product in self.products:
            product.updatePrice(percentage, True)

    def setClearance(self, category, percentage):
        for product in self.products:
            if product.category == category:
                product.updatePrice(percentage, False)
    
    def listAvail(self):
        for product in self.products:
            product.printInfo()

