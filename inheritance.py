class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")


animal_instance = Animal()
dog_instance = Dog()


animal_instance.speak()  
dog_instance.speak()     



