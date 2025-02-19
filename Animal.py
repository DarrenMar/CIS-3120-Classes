class Animal:
    def __init__(self, name):
        self.__name = name 
        print("hello, I am", self.__name)

    def talk(self):
        print(self.__name, "is talking.")

    def walk(self):
        print(self.__name, "is walking.")

    def run(self):
        print(self.__name, "is running.")

    def jump(self):
        print(self.__name, "is jumping.")

    def eat(self):
        print(self.__name, "is eating.")

    def sleep(self):
        print(self.__name, "is sleeping.")

