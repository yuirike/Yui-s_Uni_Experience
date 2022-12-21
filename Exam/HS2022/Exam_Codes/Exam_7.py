from abc import ABC, abstractmethod

class Razor:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price


class Packaging:
    def __init__(self, packet):
        self.__packet = packet

    def get_price(self):
        price = 0
        for i in self.__packet:
            price += i.get_price()
        
        return round(price,2)

    def get_contents(self):
        return len(self.__packet)

# class Bag(Packaging):
#     ID = 0
#     def __init__(self, packet):
#         Packaging.__init__(self, packet)
#         Bag.ID += 1
#         self.__ID = Bag.ID
    
# #     def get_id(self):
# #         return self.__ID





    






class Bag:
    pass

class Box:
    pass