#                                           Наследование (Inheritance)
print()
class Video_games:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def show(self):
        print(f"Game:{self.name}")
        print(f"Type: {self.type}")

class Detective_game(Video_games):
    def __init__(self,name,type,cast,quality,sound,my_opinion):
        super().__init__(name,type)
        self.cast = cast
        self.quality = quality
        self.sound = sound
        self.my_opinion = my_opinion

    def show(self):
        super().show()
        print(f"Cast: {self.cast}")
        print(f"Quality: {self.quality}")
        print(f"Sound: {self.sound}")
        print(f"My opinion: {self.my_opinion}")
        print()
        print()

class Horror_game(Video_games):
    def __init__(self,name,type,cast,quality,sound,my_opinion):
        super().__init__(name,type)
        self.cast = cast
        self.quality = quality
        self.sound = sound
        self.my_opinion = my_opinion

    def show(self):
        super().show()
        print(f"Cast: {self.cast}")
        print(f"Quality: {self.quality}")
        print(f"Sound: {self.sound}")
        print(f"My opinion: {self.my_opinion}")
        

Danganronpa = Detective_game("Danganronpa","Detective","10/10","9.5/10","10/10","10/10")
Until_dawn = Horror_game("Until_dawn","Horror","9/10","10/10","10/10","10/10")

Danganronpa.show()
Until_dawn.show()
