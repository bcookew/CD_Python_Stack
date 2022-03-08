class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def updatePrice(self, percentage, isIncreased):
        change = self.price * percentage
        if isIncreased:
            self.price += change
        else:
            self.price -= change
        return self

    def printInfo(self):
        print(f"Product Name: {self.name}\nCategory: {self.category}\nPrice: {self.price}\n")
        return self