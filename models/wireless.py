from models.machine import Machine
 
 
class WirelessController(Machine):
    def __init__(self, name):
        super().__init__(name, "WLC-PT")
 
 
class AccessPoint(Machine):
    def __init__(self, name, model="3702i"):
        super().__init__(name, model)
        self.wireless_clients = [] # c'est la liste des clients wi-fi 
 
    def associate(self, client):
        self.wireless_clients.append(client) # on ajoute le client dans la liste d'access point 
