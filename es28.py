#I nomi delle città e i corrispondenti Codici di Avviamento Postale (CAP) vengono inseriti da tastiera e memorizzati in un dizionario, dove il CAP è la chiave.
#Fornito poi da tastiera il nome di una città, costruisci un programma che visualizzi il suo CAP oppure un messaggio nel caso la città non si è compresa nell'elenco.
#Analogamente, fornendo il CAP restituisce il nome della città oppure un messaggio di errore.

d_CAP = {}
d_città = {}

while True:
    risposta_città = input("Inserire il nome della città che si vuole aggiungere all'elenco (per terminare l'elenco scrivere STOP): ")
    if risposta_città == "STOP":
        break
    else:
        risposta_CAP = int(input("Inserire il CAP: "))
        d_CAP[risposta_CAP] = risposta_città
        d_città[risposta_città] = risposta_CAP

città = input("Inserire il nome della città della quale si vuole sapere il CAP: ")

if città in d_città:
    print("Il CAP della città di", città, "è:", d_città[città])
else:
    print("La città di", città, "non è presente nell'elenco.")

CAP = int(input("Inserire il CAP del quale si vuole sapere la città: "))

if CAP in d_CAP:
    print("Il CAP",CAP ,"appartiene alla città di", d_CAP[CAP])
else:
    print("Il CAP",CAP ,"non è presente nell'elenco.")
