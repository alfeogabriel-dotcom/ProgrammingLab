#Modificate l’oggetto CSVFile della lezione precedente in modo che stampi a
#schermo un messaggio di errore* se si cerca di aprire un file non esistente.
#Potete fare questo controllo:
#a) nella funzione get_data(), oppure
#b) nell’ __init__() (basta che leggiate la prima riga per vedere se il file esiste)
'''
class CSVFile:

    def __init__(self, name):
    # Verifichiamo se 'name' NON è una stringa
        if not isinstance(name, str):
            raise TypeError(f'Il nome del file deve essere una stringa, non {type(name).__name__}')
        self.name = name

class CSVFile:

    def __init__(self, name):
        # Controllo se il nome è una stringa
        if not isinstance(name, str):
            raise TypeError('Il nome del file deve essere una stringa, ricevuto: "{}"'.format(type(name).__name__))
        
        self.name = name

    def get_data(self, start=None, end=None):
        self.dati = []
        
        try:
            with open(self.name, 'r') as file:
                # Usiamo enumerate per tenere traccia del numero di riga (partendo da 1)
                for i, line in enumerate(file, start=1):
                    
                    # Logica di filtraggio:
                    # Se start è definito e la riga attuale è minore di start, salta
                    if start is not None and i < start:
                        continue
                    
                    # Se end è definito e la riga attuale è maggiore di end, interrompi la lettura
                    if end is not None and i > end:
                        break
                    
                    elementi = line.strip().split(',')
                    
                    # Evitiamo di aggiungere righe vuote
                    if elementi:
                        self.dati.append(elementi)
                        
        except FileNotFoundError:
            print(f"Errore: il file '{self.name}' non esiste.")
            return None
            
        return self.dati

class NumericalCSVFile(CSVFile):
    
    def __init__(self,name):
        super().__init__(name)

    def get_data(self, *args, **kwargs):
        lista_righe = super().get_data(*args, **kwargs)
        dati_numerici=[]
        for riga in lista_righe:
            new_riga=[riga[0]]
            
            for valore in riga[1:]:
                try:
                    new_riga.append(float(valore))
                except ValueError:
                    print('Impossibile convertire valore "{}" in riga "{}" '.format(valore,riga))
                    continue
                except Exception as e:
                    print(f"Errore imprevisto: {e}")
                    continue
            if len(new_riga) > 1:
                dati_numerici.append(new_riga)
                
        return dati_numerici
'''
#Scrivete un programma che riceva una data di nascita come input e visualizzi
#l’età dell’utente e il numero di giorni, ore, minuti e secondi che mancano al
#prossimo compleanno.
'''
from datetime import datetime

def calcola_prossimo_compleanno():
    try:
        # 1. Richiesta input all'utente
        data_input = input("Inserisci la tua data di nascita (GG/MM/AAAA): ")
        data_nascita = datetime.strptime(data_input, "%d/%m/%Y")
        
        # 2. Otteniamo il momento attuale
        adesso = datetime.now()
        
        # 3. Calcolo dell'età
        eta = adesso.year - data_nascita.year
        # Sottraiamo 1 se il compleanno non è ancora avvenuto quest'anno
        if (adesso.month, adesso.day) < (data_nascita.month, data_nascita.day):
            eta -= 1
        
        print(f"\nHai {eta} anni.")

        # 4. Calcolo del prossimo compleanno
        prossimo_compleanno = datetime(adesso.year, data_nascita.month, data_nascita.day)
        
        # Se il compleanno è già passato quest'anno, calcoliamo quello dell'anno prossimo
        if prossimo_compleanno < adesso:
            prossimo_compleanno = datetime(adesso.year + 1, data_nascita.month, data_nascita.day)
        
        # 5. Differenza temporale (timedelta)
        differenza = prossimo_compleanno - adesso
        
        giorni = differenza.days
        ore, resto = divmod(differenza.seconds, 3600)
        minuti, secondi = divmod(resto, 60)

        print(f"Mancano al tuo prossimo compleanno:")
        print(f"{giorni} giorni, {ore} ore, {minuti} minuti e {secondi} secondi.")

    except ValueError:
        print("Errore: Assicurati di inserire la data nel formato corretto (GG/MM/AAAA).")

if __name__ == "__main__":
    calcola_prossimo_compleanno()
'''
#Scrivete un programma che chieda all'utente di inserire un numero intero. Se
#l'utente inserisce un valore valido, il programma deve stampare il quadrato del
#numero. Se l'utente inserisce un valore non valido, il programma deve
#visualizzare un messaggio di errore e richiedere nuovamente l'input
'''
while True:
    n = input("Inserire un numero intero: ")
    
    try:
        # Tentiamo di convertire l'input in un intero
        numero = int(n)
        
        # Se la conversione riesce, calcoliamo il quadrato e usciamo dal ciclo
        quadrato = numero ** 2
        print(f"Il quadrato di {numero} è {quadrato}")
        break 
        
    except ValueError:
        # Se int(n) genera un errore, viene eseguito questo blocco
        print("Errore: il valore inserito non è un numero intero valido. Riprova.")
'''

#Create un programma che mostri un menù all'utente con tre opzioni:
#1. Calcolare la somma di due numeri.
#2. Calcolare la differenza tra due numeri.
#3. Uscire.
#Il programma deve:
#1. Chiedere all'utente di scegliere un'opzione (1, 2 o 3).
#2. Eseguire l'operazione corrispondente se l'input è valido.
#3. Gestire input non validi mostrando un messaggio di errore.
#4. Continuare a mostrare il menù fino a quando l'utente sceglie di uscire (opzione 3

while True:
    n=input('_______MENU:_______\n Scegliere un opzione (1, 2, 3)\n 1 Somma di due numeri\n ' \
'2 Differenza di due numeri \n 3 Uscita\n')
    try:
        int(n)
    except ValueError:
        print("Errore: devi inserire un numero intero!")

    if (n=='1'):
        a=input('Inserire primo numero\n')
        b=input('Inserire secondo numero\n')
        print(f"La somma è {int(a)+int(b)}")
    elif (n=='2'):
        a=input('Inserire primo numero\n')
        b=input('Inserire secondo numero\n')
        print(f"La differenza è {int(a)-int(b)}")
    elif (n=='3'):
        break
    else:
        print('Inserisci un numero valido tra le tre opzioni')