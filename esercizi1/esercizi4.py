#Esercizio canguro
'''
class Canguro:

    def __init__(self):
        self.contenuto_tasca=[]

    def intasca(self,oggetto):
        self.contenuto_tasca.append(oggetto)
    
    def __str__(self):
        return 'Contenuto tasca canguro: "{}"'.format(self.contenuto_tasca)

can=Canguro()
can.intasca(1)
guro=Canguro()
guro.intasca((2,3))
print(can,guro)
'''
#● Si vogliono modificare le classi Studente e Docente precedentemente definite in modo che esse possano:
#○ memorizzare una lista di corsi frequentata da uno studente
#○ memorizzare una lista di corsi insegnati da un Docente
#● Per semplicità le liste in questione non sono vuote. Si vuole quindi definire
#saluta per stampare a schermo la lista completa dei corsi.
#● In pratica, si vuole permettere di scrivere il seguente codice:
#○ corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]
#○ obj_Irene = Studente("Irene", "Rossi", corsi)
#● cosicché obj_Irene.saluta() stampi tutti i corsi frequentati da obj_Irene
#(variabile corsi, passata al costruttore).

#○ un algoritmo che calcoli se un docente insegna tutti i corsi frequentati da uno studente.
#○ un algoritmo che verifichi che, per ogni studente iscritto ad un certo numero di corsi, esistano
#docenti che effettivamente insegnino quei corsi.
#● Per risolvere il secondo punto si usi la soluzione del primo.

class Persona:
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print('Ciao sono', self.ruolo + ",", self.nome, self.cognome)

class Studente(Persona):

    # costruttore sotto-classe
    def __init__(self, nome, cognome, corso):
        super().__init__("Studente UNITS", nome, cognome)
        self.corso = corso

    # ridefinizione del metodo bonjour di persona
    def saluta(self):
        Persona.saluta(self) # uso esplicitamente metodo di Persona
        print("> Frequento i corsi: ", self.corso)

class Docente(Persona):
    def __init__(self, nome, cognome, corso):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = corso

    def saluta(self):
        Persona.saluta(self)
        print("> Docente dei corsi: ", self.corso)

    def contacorsi(Docente,Studente):
        return set(Studente.corsi).issubset(set(Docente.corsi))
    
    def verifica_copertura_studenti(lista_studenti, lista_docenti):
        for studente in lista_studenti:
        # any() restituisce True se almeno un elemento nell'iterazione è True
            studente_coperto = any(contacorsi(docente, studente) for docente in lista_docenti)
        
            if not studente_coperto:
                print(f"Attenzione: Lo studente {studente.nome} {studente.cognome} non ha un singolo docente che copra tutti i suoi corsi.")
                return False
            
        print("Verifica superata: Tutti gli studenti hanno i loro corsi interamente coperti da almeno un docente.")
        return True

corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]
obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Irene.saluta()
obj_Paolo = Docente("Paolo","Rossi",corsi)
obj_Paolo.saluta()


#Crea una sottoclasse auto di veicolo che ha in aggiunta l'attributo
#numero_porte e cambia il metodo _str__ di conseguenza
#● Crea una sottoclasse moto che ha in aggiunta l'attributo tipo (ad esempio,
#"Sportiva" o "Touring") e cambia il metodo _str__ di conseguenza
'''
class Veicolo:
    
    def __init__(self, modello, marca, anno, numero_porte):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
        self.numero_porte = numero_porte
    
    def __str__(self):
        return 'Veicolo : "{}, {}, {}, {}, {}"'.format(self.modello,self.marca,self.anno,self.speed)
    
    def acc(self):
        self.speed += 5

    def fren(self):
        self.speed -= 5
    
    def get_speed(self):
        print(self.speed)

def Auto(Veicolo):

    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte

    def __str__(self):
        return 'Veicolo : "{}, {}, {}, {}, {}"'.format(self.modello,self.marca,self.anno,self.speed, self.numero_porte)
    
def Moto(Veicolo):
    def __init__(self,modello,marca,anno,tipo):
        super().__init__(modello, marca, anno)
        self.tipo=tipo

    def __str__(self):
        return 'Veicolo : "{}, {}, {}, {}, {}"'.format(self.modello,self.marca,self.anno,self.speed, self.tipo)
'''
#Si crei la classe Poligono:
#○ Il costruttore deve prendere solo il numero di lati
#○ Deve fornire una descrizione del tipo: "Sono un poligono con X lati"
#● Definire una sottoclasse Quadrilatero, modificare il costruttore in modo
#opportuno e sovrascrivere la descrizione per essere: "Sono un quadrilatero"
#● Definire una sottoclasse Rettangolo di Quadrilatero, la cui
#inizializzazione necessità di base ed altezza, modificare la descrizione per
#includere questa informazione e definire i metodi perimetro ed area
#● Definire la classe Triangolo, la cui inizializzazione necessità di 3 lati.
#Modificare la descrizione per includere la lunghezza dei lati. Fornire un
#metodo perimetro e uno is_equilatero (restituisce True se il triangolo è equilatero)
'''
class Poligono:
    
    def __init__(self, lati):
        self.lati=lati
    
    def __str__(self):
        return 'Sono un poligono di "{}" lati'.format(self.lati)

class Quadrilatero(Poligono):

    def __init__(self):
        super().__init__(4)

    def __str__(self):
        return 'Sono un quadrilatero'

class Rettangolo(Quadrilatero):

    def __init__(self,base,altezza):
        super().__init__()
        self.base=base
        self.altezza=altezza
    
    def __str__(self):
        return 'Sono un rettangolo di base "{}" e altezza "{}"'.format(self.base,self.altezza)

    def perimetro(self):
        return 2*self.base+2*self.altezza
    
    def area(self):
        return self.altezza*self.base

class Triangolo(Poligono):
    
    def __init__(self,a,b,c):
        super().__init__(3)
        self.a=a
        self.b=b
        self.c=c
    
    def __str__(self):
        return 'Sono un triangolo'
    
    def perimetro(self):
        return self.a+self.b+self.c
    
    def is_equilatero(self):
        if (self.a == self.b == self.c):
            return True
        else:
            return False

    


trig=Triangolo(2,2,2)
print (trig)
print (trig.perimetro())
print (trig.is_equilatero())
'''