#es1 Stampare l’equivalente di 538 minuti nel formato 8h:58min.
"""
def minuti_ore(minuti):
    risultato= int(minuti/60) #posso anche fare risultato=risultato//60
    resto= minuti-(risultato*60) #posso fare anche resto=minuti%60
    print(risultato,":",resto)

x = int(input())
minuti_ore(x)
"""
#es2 Scrivere un programma che chiede all’utente un numero intero e stampa il suo quadrato e il suo cubo.
"""
print("inserire numero")
x=int(input()) #posso scrivere anche saltando la riga 13 -> x=int(input("inserire numero"))
print(x**2,x**3)
"""
#es3 Scrivere un programma che verifica se un numero inserito dall’utente è pari o dispari.
"""
def is_par(x):
    if x%2==0:
        print(x," è pari")
    else:
        print(x," è dispari")

print("inserire numero")
x=int(input())
is_par(x)
"""
#es4 Definire una funzione che prende come argomento una parola e una lettera e ritorna quante volte quella lettera è contenuta nella parola.
"""
def rip(p,l):
    i=0
    p=p.lower() #aggiunto dopo, render la parola tutta in minuscole
    l=l.lower() #così la funzione non è più case sensitive
    for lettera in p:
        if(lettera==l):
            i=i+1
        else: 
            pass
    print(i)

print("inserire parola e lettera")
p=input()
l=input()
rip(p,l)
"""
#es5 Scrivere un programma che verifica se un numero inserito dall’utente è primo.
"""
def primo(x):
    i=2
    flag=True
    while i<=x/2:
        if(x%i==0):
            flag=False #potrei aggiungere una condizione di exit per uscire dalla funzione
            # print("False")
            # return 
        i=i+1
    print(flag)

print("inserire numero")
x=int(input())
primo(x)
"""
#es6 Scrivere un programma che fa la somma di n numeri inseriti dall’utente. Di all'utente di scrivere 0 per fermarsi.
"""
print("inserire numeri, inserire 0 per fermarsi")
sum=0
x=int(input())
while x!=0:
    sum=sum+x
    x=int(input())
print(sum)
"""
#es7 Definire la funzione fattoriale (versione iterativa).
"""
def fatt(x):
    i=0
    fatt=1
    while x>0:
        fatt=fatt*x
        x=x-1
        i=i+1
    print(fatt)

fatt(int(input()))
"""
#es8 Definire una funzione che dati 3 numeri interi stabilisce se possono essere i valori dei lati di un triangolo e, 
# se sì, di che tipo di triangolo.
"""
def tri(a,b,c):
    # Verifica se la somma di due lati è maggiore del terzo
    if (a + b > c) and (b + c > a) and (a + c > b):
        # Equilatero 
        if a == b == c:
            print("triangolo equilatero")
        # Isoscele 
        elif a == b or b == c or a == c:
            print("triangolo isoscele")
        # Rettangolo 
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            print("triangolo rettangolo")
        # Scaleno 
        else:
            print("triangolo scaleno")
    else:
        print("Non è un triangolo valido")

print("Inserisci i tre lati del triangolo, uno per riga:")
a = int(input())
b = int(input())
c = int(input())
tri(a, b, c)
"""
#es9 Definire una funzione che conta quante vocali sono presenti in una stringa.
"""
def contav(s):
    i=0
    s=s.lower()
    for l in s:
        if(l=="a" or l=="e" or l=="i" or l=="o" or l=="u"):
            i=i+1
        else:
            pass
    print(i)

contav(input())
"""
