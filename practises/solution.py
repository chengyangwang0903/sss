class Animal:
    species = 'animal'

    # write a class method show_species to print the species of the class
    # like this "It's dog". so that every subclass could call the same method
    # to print their own species
    # -- write your code here --
    @classmethod
    def show_species(c):
        print(f"It's {c.species}!")

    # @classmethod
    # def show_species(c):
    #     print(f"It's {c.species}!")

# Make Class Dog inherit from Class Animal
# -- write your code here --
class Dog(Animal):
    species = 'dog'

    def __init__(self, breed):
        self.__breed = breed
        self.__color = 'undefined'

    def barking(self):
        # print something like `Black Alaskan is barking!`
        # -- write your code here --
        print(f"{self.__color} {self.__breed} is barking!")

    # write a property function to return the color of the Dog that stores
    # at self.__color
    # -- write your code here --
    @property
    def color(self):
        return self.__color

    # write a setter function to change the dog's color which stores at
    # self.__color
    # -- write your code here --
    @color.setter
    def color(self,one_color):
        self.__color=one_color
import sys


color = "Brown"
breed = "Pug"

print(f'Dog is subclass of Animal: {issubclass(Dog, Animal)}')
dog = Dog(breed)
dog.color = color
dog.barking()
Dog.show_species()
