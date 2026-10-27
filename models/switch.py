from models.machine import Machine
 
 
class Switch(Machine):
    def __init__(self, name, model, nb_ports=24):
        super().__init__(name, model)
        self.nb_ports = nb_ports # mémorise le nombre de ports 
 
    def is_full(self):
        return len(self.links) >= self.nb_ports # tous les ports sont bloqués = nouveau câble refusé
 
 
class L3Switch(Switch): # hérite de switch sous entendu de machine aussi 
    def __init__(self, name, model, nb_ports=24):
        super().__init__(name, model, nb_ports)
        self.ip_routing = True # ce switch route 
