from abc import ABC, abstractmethod
import unittest

class Product(ABC):
    def __init__(self, price):
        self.__price = price

    @abstractmethod
    def get_price():
        pass

class Bottle(Product):
    def __init__(self, price, name):
        self.name = name
        self.price = price

    def get_price(self):
        return self.price
        

class Crate(Product):
    def __init__(self):
        self.__storage = []

    def add(self, bottle):
        if len(self.__storage) == 20:
            raise RuntimeError
        self.__storage.append(bottle)

    def get_price(self):
        total = 0
        for i in self.__storage:
            total += i.get_price()
        return total

    def get_size(self):
        return len(self.__storage)

    
class DiscountCrate(Crate):
    def __init__(self):
        Crate.__init__(self)

    def get_price(self):
        discounted_price = Crate.get_price(self)*(1-(0.02*Crate.get_size(self)))
        if discounted_price > Crate.get_price(self)*0.75:
            return round(discounted_price,2)
        else:
            return round(Crate.get_price(self)*0.75, 2)


class FixedPriceCrate(Crate):
    def __init__(self, price):
        Crate.__init__(self)
        self.__price = price

    def get_price(self):
        return self.__price




import unittest
class ShopTestSuite(unittest.TestCase):

    def test_crate_add(self):
        c = Crate()
        c.add(Bottle(4.50, "Light Beer"))
        self.assertEqual(c.get_size(), 1)

    def test_crate_max_size(self):
        B = Bottle(5, "Corona")
        Bottles = [B, B, B, B, B, 
                    B, B, B, B, B,
                    B, B, B, B, B,
                    B, B, B, B, B]
        C = Crate()
        for Bot in Bottles: C.add(Bot)
        with self.assertRaises(RuntimeError):
            C.add(B)


    def test_crate_price(self):
        B = Bottle(5, "Corona")
        A = Bottle(10, "Beer")
        C = Crate()
        C.add(B)
        C.add(A)
        self.assertEqual(15, C.get_price())

    def test_discount_crate_price(self):
        B = Bottle(4, "Corona")
        D = DiscountCrate()
        Bottles = [B, B, B, B, B]
        for Bot in Bottles: D.add(B)
        self.assertAlmostEqual(18, D.get_price())