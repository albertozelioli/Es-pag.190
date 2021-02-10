#Organizza con un dizionario la rubrica con i nomi delle persone e i rispettivi numeri telefonici.
#Fornito poi il nome della persona, il programma visualizza il suo numero di telefono oppure un messaggio nel caso la persona non sia presente nella rubrica.

rubrica = {"Marco":"343 897 3922",
"Filippo":"375 542 9054",
"Alberto":"366 738 0394",
"Riccardo":"329 489 3829",
"Lorenzo":"334 789 5692",
"Fausto":"329 239 1348",
"Luca":"390 687 2645"}
contatto = input("Inserire il nome del contatto della quale si vuole sapere il numero: ")

if contatto in rubrica:
    print("Il numero del contatto", contatto,"è:", rubrica[contatto])
else:
    print("Il contatto", contatto,"non è salvato nella rubrica.")
