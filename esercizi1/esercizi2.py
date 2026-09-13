#Esercizi liste ---------------------------------
#Scrivete una funzione che sommi tutti gli elementi di una lista
"""
def suml(l):
    somma=0
    for i in l:
        somma=somma+i
    return somma

l = [1,2,3,4,5,6,7,8,9,10]
print (suml(l))

"""
#Scrivere una funzione che prende in input una stringa e ritorna True se è un palindromo, False altrimenti.
"""
def pal(parola):
    i=0
    for i in range(len(parola)):
        if parola[i]!=parola[-(i+1)]:
            return False
    return True

print("inserire parola")
p=input()
print(pal(p))

#def pal(parola): #opzione più elegante
#    return parola == parola[::-1]
"""
#Definire una funzione che prende in input una lista A, indici i, j, e scambia il valore di A[i] con A[j].
"""
def scamb(A,i,j):
    temp=A[i]
    A[i]=A[j]
    A[j]=temp

A=[1,2,3,4,5,6,7,8,9]
print(A)
scamb(A,3,4)
print(A)
"""
#Scrivere una funzione che prende in input due liste e ritorna True se le due liste hanno almeno un elemento in comune
"""
def check_prop(A,B):
    for i in A:
        for j in B:
            if i==j:
                return True
    return False

A=[1,2,3,4,5]
B=[6,7,8,9,10,2]

print(check_prop(A,B))
"""
#Definire una funzione che prende in input una lista di numeri interi in [0, 9] e ritorna una 
# lista di stringhe, corrispondenti ai numeri scritti in Italiano, es. [1,0,7,9,8] - >["uno","zero","sette","nove","otto"]
"""
def trans(A):
    j=0
    C=[None]*len(A)
    for i in A:
        C[j]=diz_num[i]
        j=j+1
    return C

A=[2,4,7,3,9]

diz_num={1:"uno",2:"due",3:"tre",4:"quattro",5:"cinque",6:"sei",7:"sette",8:"otto",9:"nove"}

print(trans(A))
"""
#Esercizi Dizionari e File ------------------------------------

# Scrivere una funzione che prende una lista di parole e restituisce un dizionario
# con il conteggio delle occorrenze.
"""

def occ(l):
    dict = {} # inizializzo il dizionario
    for item in l: # faccio un ciclo for
        if item in dict:
            dict[item] += 1 # se l'item è nel dizionario aggiungo uno al contatore, in questo caso accediamo
            # alle chiavi 
        else:
            dict[item] = 1 # se l'item non è nel dizionario, lo inizializzo
    return dict

l=["rosso","rosso","rosso","banana","rosso","albatros"]
print(occ(l))

"""
# Definire una funzione che sommi tutti i valori delle vendite degli shampoo del file passato come argomento
"""
def vendtot(filename):
    with open(filename, 'r') as file:
        total = 0.0
        for line in file:
            elementi = line.strip().split(',')
            if elementi[0] != 'Date' and len(elementi) > 1:
                    value = float(elementi[1])
                    total += value
    return total

print(vendtot('shampoo_sales.csv'))
"""
# Definire una funzione che prende in input un file ed una parola ˜
# e conta quante volte quella parola è presente sul file
"""
def cont(filename, l):
    sum = 0
    with open(filename, 'r') as file:
        for line in file:
            words = line.strip().split(',')
            for w in words:
                if w.lower() == l.lower():
                    sum += 1
    return sum

print(cont('shampoo_sales.csv', 'date'))
"""
# Definire una funzione conteggio che prende come input un file 
# e ritorna un dizionario con chiave le parole e valore il numero di volte che la parola è presente nel file.
"""
def dizcont(filename):
    dict = {}
    with open(filename, 'r') as file:
        for line in file:
            words = line.split()
            for w in words:
                if w in dict:
                    dict[w] += 1
                else:
                    dict[w] = 1
    return dict

print(dizcont('es2.txt'))
"""

# Definire una funzione che prende come input un file, rimuove tutte le righe duplicate, 
# scrive il risultato in un nuovo file chiamato unique.txt.
#GEMINI
def clean(filename):
    # Inizializziamo un insieme vuoto per memorizzare le righe uniche
    righe_viste = set()
    
    with open(filename, 'r') as file_input:
        with open('unique.txt', 'w') as file_output:
            for riga in file_input:
                # Controlliamo se la riga è già stata incontrata
                if riga not in righe_viste:
                    file_output.write(riga) # La scriviamo nel nuovo file
                    righe_viste.add(riga)    # La aggiungiamo al set
                    
    return 'unique.txt'

print(f"Creato file: {clean('es2.txt')}")


