# # from models.machine import Machine # « Va dans le dossier models, ouvre le fichier machine.py, et récupère la classe Machine. »
 
# # a = Machine("A", "Test")
# # b = Machine("B", "Test")
# # a.connect(b) # on connecte les 2 machines 
# # print(a, "->", [d.name for d in a.links]) # d = device, affiche le nom des voisins de a

# # from models.machine import Machine
# # from models.switch import Switch
 
# # sw = Switch("SW-test", "2960-24TT", nb_ports=2)
# # sw.connect(Machine("PC-A", "PC-PT"))
# # sw.connect(Machine("PC-B", "PC-PT"))
# # print(sw, "->", [d.name for d in sw.links])




# # La liste des imports
# from models.switch import Switch, L3Switch
# from models.router import Router
# from models.workstation import Workstation
# from models.server import Server
# from models.wireless import WirelessController, AccessPoint
 
# # 1. Liste des équipements
# core = L3Switch("CORE", "3650-24PS")
# core2 = L3Switch("CORE-2", "3650-24PS")
# core3 = L3Switch("CORE-3", "3650-24PS")
# sw1 = Switch("Switch-1", "2960-24TT")
# sw2 = Switch("Switch-2", "2960-24TT")
# router0 = Router("Router0")
# wlc = WirelessController("WLC0")
# ap = AccessPoint("AP0")
 
# dhcp = Server("DHCP", service="DHCP")
# dns = Server("DNS", service="DNS")
# server0 = Server("Server0")
# server2 = Server("Server2")
# server3 = Server("Server3")
 
# pc0, pc1, pc2, pc3, pc4, pc5 = (Workstation(f"PC{i}") for i in range(6)) # veut dire= fait 6 Workstation nommées PC0 à PC5, et range-les dans les variables pc0 à pc5, dans l'ordre. »
# laptop0 = Workstation("Laptop0", model="Laptop-PT") # = fait un objet de type Workstation, donne-lui le nom Laptop0 et le modèle Laptop-PT, puis range-le dans la variable laptop0. »
 
# # 2. Liste des câbles
# core.connect(core2) # core relié à core2
# core.connect(core3)
# core.connect(sw1)
# core.connect(sw2)
# core.connect(dhcp)
# core.connect(dns)
# core.connect(wlc)
# core.connect(ap)
# core.connect(router0)
 
# core2.connect(sw1)
# core2.connect(sw2)
 
# core3.connect(pc4)
# core3.connect(pc5)
 
# sw1.connect(server0)
# sw1.connect(pc0)
# sw1.connect(pc1)
 
# sw2.connect(pc2)
# sw2.connect(pc3)
# sw2.connect(server2)
 
# router0.connect(server3)
 
# ap.associate(laptop0) # ici c'est access point, pour la wifi !!! c'est pas 1 câble 
 
# # 3. Affichage (on met tous les équipements dans une liste "device")
# devices = [core, core2, core3, sw1, sw2, router0, wlc, ap,
#            dhcp, dns, server0, server2, server3,
#            pc0, pc1, pc2, pc3, pc4, pc5, laptop0]
 
# for d in devices:
#     print(d, "->", ", ".join(n.name for n in d.links) or "(aucun câble)") # parcourt tt équipement et affiche la liste de ses voisins, donne un "rapport de câblage" pour vérifier que tout est co

echo '$krb5pa$18$william.dupond$CATCORP.LOCAL$fc8bbe22b2c967b222ed73dd7616ea71b2ae0c1b0c3688bfff7fecffdebd4054471350cb6e36d3b55ba3420be6c0210b2d978d3f51d1eb4f' > hash.txt