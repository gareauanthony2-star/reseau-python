# from models.machine import Machine # « Va dans le dossier models, ouvre le fichier machine.py, et récupère la classe Machine. »
 
# a = Machine("A", "Test")
# b = Machine("B", "Test")
# a.connect(b) # on connecte les 2 machines 
# print(a, "->", [d.name for d in a.links]) # d = device, affiche le nom des voisins de a

# from models.machine import Machine
# from models.switch import Switch
 
# sw = Switch("SW-test", "2960-24TT", nb_ports=2)
# sw.connect(Machine("PC-A", "PC-PT"))
# sw.connect(Machine("PC-B", "PC-PT"))
# print(sw, "->", [d.name for d in sw.links])

from models.switch import Switch, L3Switch
from models.router import Router
from models.workstation import Workstation
from models.server import Server
from models.wireless import WirelessController, AccessPoint
 
# 1. Les équipements
core = L3Switch("CORE", "3650-24PS")
core2 = L3Switch("CORE-2", "3650-24PS")
core3 = L3Switch("CORE-3", "3650-24PS")
sw1 = Switch("Switch-1", "2960-24TT")
sw2 = Switch("Switch-2", "2960-24TT")
router0 = Router("Router0")
wlc = WirelessController("WLC0")
ap = AccessPoint("AP0")
 
dhcp = Server("DHCP", service="DHCP")
dns = Server("DNS", service="DNS")
server0 = Server("Server0")
server2 = Server("Server2")
server3 = Server("Server3")
 
pc0, pc1, pc2, pc3, pc4, pc5 = (Workstation(f"PC{i}") for i in range(6))
laptop0 = Workstation("Laptop0", model="Laptop-PT")
 
# 2. Les câbles
core.connect(core2)
core.connect(core3)
core.connect(sw1)
core.connect(sw2)
core.connect(dhcp)
core.connect(dns)
core.connect(wlc)
core.connect(ap)
core.connect(router0)
 
core2.connect(sw1)
core2.connect(sw2)
 
core3.connect(pc4)
core3.connect(pc5)
 
sw1.connect(server0)
sw1.connect(pc0)
sw1.connect(pc1)
 
sw2.connect(pc2)
sw2.connect(pc3)
sw2.connect(server2)
 
router0.connect(server3)
 
ap.associate(laptop0)
 
# 3. Affichage
devices = [core, core2, core3, sw1, sw2, router0, wlc, ap,
           dhcp, dns, server0, server2, server3,
           pc0, pc1, pc2, pc3, pc4, pc5, laptop0]
 
for d in devices:
    print(d, "->", ", ".join(n.name for n in d.links) or "(aucun câble)")
