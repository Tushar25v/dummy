class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Bird(Animal):
    def make_sound(self):
        print("Chirp")

class Mammal(Animal):
    def make_sound(self):
        print("Roar")

class Parrot(Bird):
    def make_sound(self):
        print("Squawk")

class Lion(Mammal):
    def make_sound(self):
        print("Growl")

# Creating instances of Parrot and Lion classes
parrot_instance = Parrot(name="Polly", sound="Squawk")
lion_instance = Lion(name="Simba", sound="Growl")


print("Parrot makes the sound:")
parrot_instance.make_sound()

print("\nLion makes the sound:")
lion_instance.make_sound()
