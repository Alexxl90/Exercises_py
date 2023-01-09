from unittest.util import sorted_list_difference


class Vehicul:
  

    def __init__(self , nume, viteza , capacitate_cilindrica , capacitate_portbagaj , caroserie):
        self.nume = nume
        self.viteza = viteza
        self.capaciatate_cilindrica = capacitate_cilindrica
        self.capacitate_portbagaj = capacitate_portbagaj
        self.caroserie = caroserie

    

        print(f"Masina este ->  {nume} | {viteza} km/h | cilindree {capacitate_cilindrica} cm³ | portbagaj - {capacitate_portbagaj} litri | tip caroserie -  {caroserie}")
    
  


dacia = Vehicul("Dacia", 220 , 1400 , 300 , "sedan")
volvo = Vehicul("Volvo", 260 , 2000 , 400 , "SUV")
bmw = Vehicul("BMW  ",300 , 3000 , 500 , "sedan")
ford = Vehicul("Ford ", 280 , 1600, 550 , "SUV")

lista1 = [dacia.viteza ,  volvo.viteza , bmw.viteza , ford.viteza]
lista2 = [dacia.capacitate_portbagaj , volvo.capacitate_portbagaj, bmw.capacitate_portbagaj , ford.capacitate_portbagaj] 

top_speed = sorted(lista1)
top_spatiu = sorted (lista2)


print (f"cele mai rapide masini  sunt --> " , top_speed[0] , "si -->" , top_speed[1])