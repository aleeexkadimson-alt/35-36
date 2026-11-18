#                                               Инĸапсуляция (Encapsulation)



#PUBLIC

class Video_games:
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"Game: {self.name}")

game = Video_games("Danganronpa")
game.show()

#PROTECTED ._


# class Video_games:
#     def __init__(self,type):
#         self._type = type

#     def show(self):
#         print(f"Game: {self._type}")

# game = Video_games("Detective")
# game.show()






#PRIVATE .__


# class Video_games:
#     def __init__(self,password_for_game):
#         self.__password_for_game = password_for_game

#     def show(self):
#         print(f"Password for game: {self.__password_for_game}")

# game = Video_games("Passwoooooord")
# game.show()