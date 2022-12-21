import random

class Coinflips:
    def __init__(self):
        self.__check = []
        self.__options = ["tails", "heads"]
        self.__choice = 0

    def play(self, choice):
        if not choice in self.__options:
            raise Warning
        self.__check.append(choice)
        self.__choice = choice
        
        option = random.choice(self.__options)
        return option

    def winner(self):
        if self.__choice == self.play(self.__choice):
            return True
        else:
            return False

    def __str__(self):
        return "\n".join(self.__check)





        
        


    
