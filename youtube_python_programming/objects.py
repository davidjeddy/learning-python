import random
import sys
import os

class Animal:
    # Private properties start with `__`, changing value must use a methods call (getters/setters)
    __name = None
    __height = 0
    __weight = 0
    __sound = 0

    # init he obj
    def __init__(self, name, height, weight, sound):
        """
        :param name:
        :param height:
        :param weight:
        :param sound:
        """
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, param: str):
        """
        set obj name property
        :param param:
        :return:
        """
        self.__name = param

    def get_name(self) -> str:
        """
        get object name property
        :return:
        """
        return self.__name

    def set_height(self, param: str):
        """
        set obj height property
        :param param:
        :return:
        """
        self.__height = param

    def get_height(self) -> str:
        """
        get object height property
        :return:
        """
        return self.__height

    def set_weight(self, param: str):
        """
        set obj weight property
        :param param:
        :return:
        """
        self.__weight = param

    def get_weight(self) -> str:
        """
        get object weight property
        :return:
        """
        return self.__weight

    def set_sound(self, param: str):
        """
        set obj sound property
        :param param:
        :return:
        """
        self.__sound = param

    def get_sound(self) -> str:
        """
        get object sound property
        :return:
        """
        return self.__sound

    def get_type(self):
        print("Animal")

    def toString(self) -> str:
        return "{} is {} cm tall, weights {} kg, and says {}.".format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)

cat = Animal('Whiskers', 33, 10,' Meow')
print(cat.toString())

# class inheritance
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        """
        :param name:
        :param height:
        :param weight:
        :param sound:
        :param owner:
        """
        # calling a method from a parent / super class and passing parameters to it
        super(Dog, self).__init__(name, height, weight, sound)

        self.__owner = owner

    def set_owner(self, param: str):
        """
        set obj owner property
        :param param:
        :return:
        """
        self.__owner = param

    def get_owner(self) -> str:
        """
        get object owner property
        :return:
        """
        return self.__owner

    def get_type(self):
        print("Dog")

    # over ride parent / super class method
    def toString(self) -> str:
        """
        :return:
        """
        return "{} is {} cm tall, weights {} kg, and says {}. It's owner is {}.".format(self.__name,
                                                                                        self.__height,
                                                                                        self.__weight,
                                                                                        self.__sound,
                                                                                        self.__owner)

    # method overloading
    def multiple_sounds(self, how_many_time = None):
        """
        :param how_many_time:
        :return:
        """
        if how_many_time is None:
            print(self.get_sound())
        else:
            print(self.get_sound() * how_many_time)

dog = Dog('Max', 50, 25, 'Woof', 'you')