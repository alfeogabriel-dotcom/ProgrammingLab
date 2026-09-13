'''
def sumfile():
    somma=0
    with open('shampoo_sales.csv', 'r') as mio_file:
            for linea in mio_file:
                linea_p = linea.strip()
                if not linea_p:
                    continue
                elementi = linea_p.split(',')

                if (elementi[0]!= 'Date'):
                    try:
                        somma = somma + float(elementi[1])
                    except ValueError:
                        print(f"Salto la riga non valida: {linea_p}")
                        continue
    return somma

print(sumfile())

'''
'''
class Veicolo:
    
    def __init__(self, modello, velocita, km, anno_rev, posti):
        self.modello = modello
        self.velocita = velocita
        self.km = km
        self.anno_rev = int(anno_rev)
        self.posti = int(posti)

    def info(self):
        print(f"Sono un {self.modello}, vado a {self.velocita} km/h e ho {self.km} km")
    
    def revisionata(self, anno):
        if anno == self.anno_rev or anno == self.anno_rev +1:
            print(f'L\' {self.modello} è coperta\o per l\' anno {anno}')
        else: print(f'L\'{self.modello} NON è coperta\o dalla revisione per l\' anno {anno}')

    def fare(self):
        return self.posti * 100
    
class Autobus(Veicolo):
    
    def __init__(self, velocita, km, capienza, rotta, anno_rev, posti):
        super().__init__("Autobus",velocita, km, anno_rev, posti)
        self.capienza = capienza
        self.rotta = rotta
        
    def info(self):
        Veicolo.info(self)
        print(f"Ho capienza massima di {self.capienza} persone, e seguo la rotta: {self.rotta}")

    def revisionata(self,anno):
        super().revisionata(anno)

class Bus(Veicolo):

    def __init__(self,modello,velocita, km, anno_rev, posti):
        super().__init__(modello,velocita, km, anno_rev, posti)

    def fare(self):
        return self.posti * 100 + self.posti/10 *100


class Auto(Veicolo):
    
    def __init__(self, velocita, km, anno_rev):
        super().__init__("Auto", velocita, km, anno_rev, 4)
    
    def revisionata(self,anno):
        super().revisionata(anno)


percorso = ['trieste', 'opicina','prosecco','sistiana','duino']

a = Veicolo('Berlina', 20, 100000, 2024, 5)
b= Autobus(15, 50000, 35, percorso, 2023, 40)
c= Auto(30, 450000, 2025)
scuolabus = Bus("volvo",15,12,2023,50)


a.info()
b.info()
b.revisionata(2024)
c.revisionata(2028)

print(scuolabus.fare())
print(b.fare())
'''
while True:
    a=input("inserire numero \n")
    try:
        a=int(a)
        print(a*2)
        break
    except ValueError:
        print("\nValore non valido immettere altro valore")
        continue