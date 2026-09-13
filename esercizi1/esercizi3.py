#Creare una classe coin che ha come attributo il valore della faccia
#● E ha due metodi:
#○ uno che simula il lancio della moneta e che salva il valore sull'attributo faccia.
#○ uno che ritorna il valore dell'attributo faccia
'''
import random

class coin:

    def __init__(self): #inizializzo la faccia
        self.faccia = 0

    def lancio(self): # creo il metodo lancio
        self.faccia = random.randint(0,1)
    
    def risultato(self): # creo il metodo che ritorna il risultato
        print(self.faccia)

moneta=coin()
moneta.lancio()
moneta.risultato()
'''
#Scrivete una classe denominata Veicolo che disponga di questi attributi dati:
#● modello (per il modello del veicolo);
#● marca (per la marca del veicolo);
#● anno (per l'anno del veicolo).
#● speed (per la velocità del veicolo)
#E di questi metodi:
#● __init__ che accetti come argomenti l’anno, il modello, e la marca. Il metodo dovrebbe inoltre
#assegnare 0 all’attributo dati speed.
#● __str__ che restituisce una stringa con i dettagli del veicolo (marca, modello, anno e velocità)
#● accellerare che aggiunge 5 all’attributo dati speed ogni volta che viene chiamato.
#● frenare che sottrae 5 dall’attributo dati speed ogni volta che viene chiamato.
#● get_speed che restituisce la velocità corrente.
'''
class Veicolo:
    
    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
    
    def __str__(self):
        return 'Veicolo : "{}, {}, {}, {}"'.format(self.modello,self.marca,self.anno,self.speed)
    
    def acc(self):
        self.speed += 5

    def fren(self):
        self.speed -= 5
    
    def get_speed(self):
        print(self.speed)

auto = Veicolo('fiat','126','1978')
print(auto)
auto.acc()
auto.get_speed()
auto.fren()
auto.get_speed()
'''
#Create un oggetto CSVFile che rappresenti un file CSV, e che:
#1) venga inizializzato sul nome del file csv, e
#2) abbia un attributo “name” che ne contenga il nome
#3) abbia un metodo“get_data()” che torni i dati dal file CSV come lista di liste,
#ad es: [ ['01-01-2012', '266.0'], ['01-02-2012', '145.9'], ... ]
'''
class CSVFile:

    def __init__(self,name):
        self.name = name

    def get_data(self):
        self.dati = []
        with open(self.name, 'r') as file:
            for line in file:
                elementi = line.strip().split(',')
                if elementi[0] != 'Date':  # Salta l'intestazione se presente, nel caso di shampoo sales
                    self.dati.append(elementi)
        return self.dati

file=CSVFile('shampoo_sales.csv')
print(file.get_data())
'''