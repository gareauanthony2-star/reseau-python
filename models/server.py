from models.machine import Machine
 
 
class Server(Machine):
    def __init__(self, name, service=None): # cad par défaut = none pas de service
        super().__init__(name, "Server-PT") # l'appel au parent classe machine 
        self.service = service # les serveur fournit un service
