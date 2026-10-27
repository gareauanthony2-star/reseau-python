from models.machine import Machine
 
 
class Router(Machine):
    def __init__(self, name, model="ISR4331"):
        super().__init__(name, model) # on appelle le parent avec super donc machine / sans ça le routeur est vide pas d'infos
        self.routes = []
 
    def add_route(self, network, next_hop): # 2 infos par route : rzo de dest. + @ du voisin
        self.routes.append((network, next_hop)) # on stocke la route
