




############################## canstructor ################################

class Car:
    def __init__(self, model, marka, color):
        self.__model = model
        self.__marka = marka
        self.__color = color



    def get_model(self):
        return self.__model

    def get_marka(self):
        return self.__marka



    def set_model(self, new_model):
        self.__model = new_model

    def set_color(self, new_color):
        self.__color = new_color

    def start(self):
        print(f'{self.__model}  Car is startig')
    def move(self):
        print(f"{self.__model}  Car is moving")
    def stop(self):
        print(f"{self.__model}  Car is stoping")

    def display_info(self):
        print(f"model: {self.__model}\n"
              f'marka: {self.__marka}\n'
              f'color:  {self.__color}\n'
              )


mers = Car('Mers','SLS AMG', 'black')
mers.set_color('red')
mers.set_model('Mazda')
print(mers.get_model())

mers.display_info()






