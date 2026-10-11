
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()

obj = Dog()
obj.speak()
