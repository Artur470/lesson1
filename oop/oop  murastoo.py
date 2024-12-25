



##############################  Murastoo ###########################




class Animals:
    def init(self, name , weight, color, country):

        self.name = name
        self.weight = weight
        self.color = color
        self.country = country




    def golos(self):
        print("Animals голос")

    def spat(self, name):
        print(f" {name} спать")

    def food(self):
        print("Animals кушать")


class Dog(Animals):
    def __init__(self, name, weight , color , country, poroda, pol):

        self.name = name
        self.weight = weight
        self.color = color
        self.country = country
        self.poroda = poroda
        self.pol = pol

    def fas(self):
        print(f" {self.name}   fas")
    def ohrana(self):
        print(f"{self.name}   protect the house")



atak = Animals()
animals =Dog('Reks' , 20, 'black', 'Kyrgyzstan', 'Taygan', 'mun')

atak.spat("Reks")
animals.fas()





