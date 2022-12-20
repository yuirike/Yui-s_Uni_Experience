class Brewery:
    def __init__(self, name):
        self.__name = name
        self.__stock = {}

    @staticmethod
    def to_gram(amount, unit):
        if unit == 't':
            return amount*(10**6)
        if unit == "kg":
            return amount*(10**3)
        if unit == "g":
            return amount

    def add_stock(self, resource, amount, unit):
        if not resource in self.__stock.keys():
            add = {resource: 0}
            self.__stock.update(add)
        self.__stock[resource] = self.__stock[resource] + \
            self.to_gram(amount, unit)

    def show_stock(self, resource):
        if not resource in self.__stock.keys():
            return 0
        return self.__stock[resource]

    def brew(self, recipe):
        for key in recipe.keys():
            if not key in self.__stock.keys():
                raise LookupError

        recipe_items = [x for x in recipe.items()]
        stock_items = [x for x in self.__stock if x in recipe_items]
        recipe_items = sorted(recipe_items)
        stock_items = sorted(stock_items)
        for a, b in zip(recipe_items, stock_items):
            if a[1] > b[1]:
                raise LookupError

        for a, b in recipe_items:
            self.__stock[a] = self.__stock[a]-b


#Assertions
assert Brewery.to_gram(1, "t") == 1000000
assert Brewery.to_gram(1, "kg") == 1000
assert Brewery.to_gram(1, "g") == 1
b = Brewery("KegOverflow")
assert b.show_stock("Syrup") == 0
b.add_stock("Malt", 5, "kg")
b.add_stock("Malt", 5, "kg")
b.add_stock("Water", 50, "kg")
b.add_stock("Hops", 30, "g")
assert b.show_stock("Malt") == 10000
b.brew({"Malt": 8000, "Water": 40000, "Hops": 20})
assert b.show_stock("Malt") == 2000
b.brew({"Water": 10000})
assert b.show_stock("Water") == 0
