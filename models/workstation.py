from models.machine import Machine
 
 
class Workstation(Machine):
    def __init__(self, name, model="PC-PT", ip_address=None): # cad par défaut n'a pas d'ip
        super().__init__(name, model) # l'appel au parent 
        self.ip_address = ip_address # le pc a une adresse ip 
