class Machine:
    def __init__(self, name, model, cpu=1, ram=1):
        self.name = name
        self.model = model
        self.cpu = cpu
        self.ram = ram
        self.links = []
 
    def is_full(self):
        return False
 
    def connect(self, other):
        for device in (self, other):
            if device.is_full():
                raise ValueError(f"{device.name} : plus de port libre")
        self.links.append(other)
        other.links.append(self)
 
    def __str__(self):
        return f"{self.name} [{self.model}]"
