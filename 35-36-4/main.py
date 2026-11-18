#                                     Полиморфизм (Polymorphism)

class Detective_game:
    def game(self):
        print("Danganronpa")

class Horror_game:
    def game(self):
        print("Until Dawn")

game1 = Detective_game()
game2 = Horror_game()

for obj in [game1,game2]:
    obj.game()