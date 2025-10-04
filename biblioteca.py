import csv

def carica_da_file(percorso_file):
    """Carica i libri dal file"""
    biblioteca = []
    try:
        file=open(percorso_file,"r")
        lettore = csv.reader(file)
        prima_riga=True
        for riga in lettore:
            if prima_riga==True:
                biblioteca = []
                n=int(riga[0])
                for _ in range(n):
                    biblioteca.append([])
                print(f"nella biblioteca ci sono: {riga[0]} sezioni")
                prima_riga=False
            else:
                libro = {"titolo": riga[0], "autore": riga[1], "anno": riga[2], "numero_pagine": riga[3],
                         "sezione": riga[4]}
                i = int(libro["sezione"]) - 1
                if 0<=i<n:
                    biblioteca[i].append(libro)
        file.close()
        return biblioteca
    except FileNotFoundError:
        print("File not found")
        return None

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, percorso_file):
    """Aggiunge un libro nella biblioteca"""
        # Controllo se il libro esiste già
    if biblioteca is None:
        print("la biblioteca non esiste: ")
        return None
    for sezione in biblioteca:
        for libro in sezione:
            if libro["titolo"] == titolo:
                print("il libro è già presente nella biblioteca!")
                return None

        # Controllo se la sezione è valida
    if sezione < 1 or sezione > len(biblioteca):
        print("Errore: sezione non esistente.")
        return None

        # Creo il nuovo libro
    nuovo_libro = {"titolo": titolo, "autore": autore, "anno": anno, "numero_pagine": pagine, "sezione": sezione}

        # Aggiungo il libro alla struttura dati
    biblioteca[sezione - 1].append(nuovo_libro)

        # Aggiungo il libro anche al file
    file = open(percorso_file, "a", newline="")
    scrittore = csv.writer(file)
    scrittore.writerow([titolo, autore, anno, pagine, sezione])
    file.close()

    return nuovo_libro


def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    for sezione in biblioteca:  # scorro tutte le sezioni
        for libro in sezione:  # scorro i libri dentro ogni sezione
            if libro["titolo"] == titolo:  # controllo se il titolo corrisponde
                return libro  # se trovato, restituisco il dizionario

    return None  # se non trovo niente, ritorno None


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    # Controllo se la sezione esiste
    if sezione < 1 or sezione > len(biblioteca):
        return None

    # Prendo la lista dei libri della sezione
    libri_sezione = biblioteca[sezione - 1]

    # Creo una lista vuota per i titoli
    titoli = []

    # Aggiungo ogni titolo alla lista
    for libro in libri_sezione:
        titoli.append(libro["titolo"])

    # Ordino alfabeticamente
    titoli.sort()

    return titoli


def main():
    biblioteca = []

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                percorso_file = input("Inserisci il percorso del file da caricare: ").strip()
                biblioteca = carica_da_file(percorso_file)
                if biblioteca is not None:
                    print("nella biblioteca ci sono questi libri: ")
                    for sezione in biblioteca:
                        print("nuova sezione:")
                        for libro in sezione:
                            print(libro)
                    break
                else:
                    print("non esiste il file inserito")

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            nuovo_libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, percorso_file)
            if nuovo_libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


main()

