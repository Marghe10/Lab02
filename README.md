# Lab 02

#### Argomenti

- Liste di liste: iterazioni e ordinamenti.
- Lettura da e scrittura su file.
- Eccezioni.


## Album Fotografico Digitale
Progettare e realizzare un programma per la gestione di un album fotografico digitale. L'album contiene una raccolta 
di foto, organizzate in base all'anno di scatto.

Le foto possono appartenere a un qualsiasi anno. Quando viene inserita la prima foto 
relativa a un anno non ancora presente nell'album, tale anno deve essere aggiunto alla struttura dati utilizzata per 
modellare il concetto di album.

Ogni foto è univocamente identificata da un codice, ed è caratterizzata da titolo, autore, mese di scatto (un intero
da 1 a 12) e anno di scatto.

I dati delle foto sono forniti nel file `album_foto.csv` che contiene un elenco di foto, una per riga, con le 
informazioni (codice, titolo, autore, mese, anno). 

Esempio di file `album_fotografico.csv`:
```file
codice, titolo, autore, mese, anno
P001,Tramonto sul mare,Elena Conti,7,2019
P002,Montagne innevate,Marco Bruni,1,2021
P003,Ritratto di famiglia,Giulia Ferri,12,2021
P004,Cascata nella foresta,Marco Bruni,6,2022
...
```
La prima riga del file contiene le intestazioni delle colonne e, pertanto, non deve essere interpretata come una 
foto.

Il file può contenere foto appartenenti a un numero qualsiasi di anni diversi, che non necessariamente devono 
essere consecutivi. 

### Implementazione
Per questo laboratorio è necessario implementare le funzioni presenti nel file `album_foto.py` e modellare il
concetto di foto utilizzando una struttura dati opportuna (una lista, una tupla, un dizionario, una
classe, ecc.).

La funzione `main()` presente nel file `album_foto.py` consente di interagire con il sistema tramite un menù
testuale utilizzabile dalla console.

```menu in console
1. Carica album da file
2. Aggiungi una nuova foto
3. Cerca una foto per codice
4. Elenco foto di un anno (ordinato per titolo)
5. Esci
Scegli un'opzione >>
```

Il menu permette di effettuare varie operazioni che devono essere gestite da opportune funzioni.

La funzione `carica_da_file()` riceve come parametro il percorso del file da leggere e deve creare e popolare una
struttura dati che rappresenta l'album, creando un nuovo anno ogni volta che viene incontrato per la prima volta
durante la lettura. La funzione deve restituire la struttura dati creata. Se l'apertura del file scatena
l'eccezione `FileNotFoundError`, la funzione deve restituire `None`.

L'aggiunta di una nuova foto non già presente nell'album viene gestita tramite la funzione `aggiungi_foto()`, che
riceve come parametri la struttura dati rappresentante l'album, il codice della foto, il titolo, l'autore, il mese,
l'anno e il percorso del file da aggiornare. Se l'anno indicato non è ancora presente nell'album, la funzione deve
crearlo. La funzione deve aggiornare la struttura dati ed il file, inserendo una nuova riga in fondo a quest'ultimo. In caso di
aggiornamento avvenuto con successo, la funzione deve ritornare un riferimento alla foto aggiunta. In caso di
errori, quali codice già presente, mese non valido (fuori dall'intervallo 1-12) o file non trovato, la funzione
deve restituire `None`.

Per accedere alle informazioni relative ad una qualsiasi delle foto memorizzate si utilizza la funzione
`cerca_foto()`, che riceve come parametro la struttura dati rappresentante l'album ed il codice della foto da
cercare. Nel caso in cui la foto non esista, la funzione restituisce `None`; altrimenti, restituisce una stringa
contenente il codice, il titolo, l'autore, il mese e l'anno della foto, nel seguente formato:

```formato
P001, Tramonto sul mare, Elena Conti, 7, 2019
```

Il sistema, attraverso la funzione `elenco_foto_anno_per_titolo()`, consente di ottenere un elenco delle foto
scattate in un dato anno, ordinate alfabeticamente per titolo. La funzione riceve come parametri la struttura dati
che rappresenta l'album e l'anno da consultare. Una volta eseguita l'operazione, il sistema restituisce la lista dei
titoli di quell'anno in ordine alfabetico. Nel caso in cui quell'anno non sia mai comparso nell'album (nessuna foto
è mai stata scattata in quell'anno), la funzione restituisce `None`: a differenza dell'aggiunta di una foto, qui non
si crea nulla, si può solo consultare ciò che esiste già.
