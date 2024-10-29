# AI ACT Compliance Tool

L'**AI ACT Compliance Tool** è un'applicazione Python sviluppata per assistere nella valutazione della conformità dei progetti di intelligenza artificiale in base all'**AI Act** dell'Unione Europea. L'applicazione guida l'utente attraverso un questionario di valutazione, calcola il livello di rischio del progetto e genera un report PDF con i risultati.

## Funzionalità

- **Questionario di conformità**: l'applicazione pone domande chiave per valutare i rischi del progetto AI.
- **Calcolo del livello di rischio**: determina il livello di rischio (Inaccettabile, Alto, Moderato, Basso) in base alle risposte.
- **Esportazione report**: genera un report in formato PDF che riassume i risultati della valutazione.
- **Salvataggio e caricamento delle valutazioni**: permette di salvare e riprendere le valutazioni per completarle in un secondo momento.
- **Accesso a risorse aggiuntive**: fornisce link e risorse utili per approfondire l'AI Act e la conformità normativa.

## Requisiti di Sistema

- **Python 3.x**
- Moduli Python:
  - `tkinter`: per l'interfaccia grafica.
  - `reportlab`: per la generazione di report in formato PDF.
  
È possibile installare i moduli richiesti tramite `pip`:
  
pip install reportlab


## Clona il repository:

git clone https://github.com/yourusername/ai-act-compliance-tool.git


## Installa le dipendenze:

pip install -r requirements.txt


## Esegui l'applicazione:

python main.py

## Utilizzo


## Inserisci le informazioni sul progetto:

Fornisci il nome e la descrizione del progetto AI.

## Rispondi alle domande del questionario:

Segui le domande proposte e rispondi "Sì" o "No" per procedere.

## Visualizza i risultati:

Al termine della valutazione, l'applicazione mostrerà il livello di rischio e i requisiti di conformità.

## Esporta il report:

È possibile salvare un report in PDF che riassume i risultati della valutazione.

## Salva e carica le valutazioni:

Salva la valutazione in formato JSON per riprendere la sessione in un secondo momento.

Struttura del Codice
main.py: punto di ingresso dell'applicazione, avvia la GUI.
gui.py: contiene la logica dell'interfaccia utente (Tkinter).
data.py: contiene la classe DataManager con le domande, la logica di valutazione del rischio e la gestione delle risorse.
utils.py: contiene la funzione generate_pdf_report per generare il report in formato PDF.
questions.json (opzionale): file JSON contenente le domande personalizzate, se presente.
resources.txt (opzionale): file di testo contenente risorse aggiuntive sul tema dell'AI Act.


## Contribuire
Se desideri contribuire:

Fai un fork del progetto.
Crea un nuovo branch per le tue modifiche.
Invia una pull request con una descrizione delle tue modifiche.


## Licenza
Questo progetto è distribuito sotto la licenza MIT. Consulta il file LICENSE per maggiori dettagli.

## Contatti
Per domande o supporto, contatta Francesco Brina all'indirizzo: francescobrina9@gmail.com.
