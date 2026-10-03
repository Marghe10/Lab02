from csv import DictReader


def carica_da_file(file_path):
    """Carica le foto dal file, creando un nuovo anno ogni volta che compare per la prima volta"""
    # TODO
    try:
        file=open(file_path,"r")
        lettore=DictReader(file)
        lettore.fieldnames = [name.strip() for name in lettore.fieldnames]
        lista_foto=list(lettore)
        file.close()
        album_anno={}
        for i in lista_foto:
            anno=i["anno"]
            if anno not in album_anno: # se "2019" non è ancora una chiave del dizionario "album_anno"
                album_anno[anno] = [] # -> creo una lista vuota per il nuovo anno {"2019":[]}
            album_anno[anno].append(i) # ->Se l’anno non esiste ancora, viene creato come chiave del dizionario con una lista vuota come valore: {"2019": [ {...} ] }
        print(album_anno)
        return album_anno

    except FileNotFoundError:
        return None


def aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path):
    """Aggiunge una foto all'album, creando l'anno al volo se non è ancora presente"""
    # TODO
    nuova_foto={"anno":anno, "codice":codice,"titolo":titolo,"autore":autore,"mese":mese}
    anno=str(anno)
    if anno not in album:
        album[anno]=[]
    album[anno].append(nuova_foto)
    return nuova_foto

def cerca_foto(album, codice):
    """Cerca una foto nell'album dato il codice"""
    # TODO
    for i in album:
        for x in album[i]:
            if x["codice"] == codice:
                return x
    return None


def elenco_foto_anno_per_titolo(album, anno):
    """Ordina i titoli delle foto di un dato anno in ordine alfabetico"""
    # TODO
    anno=str(anno)
    if anno not in album:
        return None
    return sorted(album[anno], key=lambda x: x["titolo"])

def main():
    album = []
    file_path = "album_fotografico.csv"

    while True:
        print("\n--- MENU ALBUM FOTOGRAFICO ---")
        print("1. Carica album da file")
        print("2. Aggiungi una nuova foto")
        print("3. Cerca una foto per codice")
        print("4. Elenco foto di un anno (ordinato per titolo)")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                album = carica_da_file(file_path)
                if album is not None:
                    break

        elif scelta == "2":
            if not album:
                print("Prima carica l'album da file.")
                continue

            codice = input("Codice della foto: ").strip()
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                mese = int(input("Mese (1-12): ").strip())
                anno = int(input("Anno: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per mese e anno.")
                continue

            foto = aggiungi_foto(album, codice, titolo, autore, mese, anno, file_path)
            if foto:
                print(f"Foto aggiunta con successo!")
            else:
                print("Non è stato possibile aggiungere la foto.")

        elif scelta == "3":
            if not album:
                print("L'album è vuoto.")
                continue

            codice = input("Inserisci il codice della foto da cercare: ").strip()
            risultato = cerca_foto(album, codice)
            if risultato:
                print(f"Foto trovata: {risultato}")
            else:
                print("Foto non trovata.")

        elif scelta == "4":
            if not album:
                print("L'album è vuoto.")
                continue

            try:
                anno = int(input("Inserisci l'anno da consultare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_foto_anno_per_titolo(album, anno)
            if titoli is not None:
                print(f'\nFoto del {anno}:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))
            else:
                print(f"Nessuna foto trovata per l'anno {anno}.")

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()
