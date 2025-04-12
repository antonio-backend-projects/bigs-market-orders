# Big Market Orders

## Scraping Bot per Transazioni Politiche

Questo è uno script Python che esegue il **web scraping** delle transazioni finanziarie effettuate dai membri del Congresso e invia notifiche via **Telegram**. L'obiettivo è monitorare le transazioni finanziarie di determinati politici e ricevere notifiche ogni volta che una transazione viene registrata.

## Struttura del Progetto

project-directory/
├── scraper_bot.py                 # Script principale per scraping e notifiche
├── requirements.txt               # File con tutte le dipendenze necessarie
├── config.py                      # Configurazione per il token e il chat_id
├── README.md                      # File README con spiegazione del progetto
└── cronjob.sh                     # Script per schedulare l'esecuzione automatica
```

## Configurazione

### 1. Creare un Bot Telegram

Per creare un bot Telegram, segui questi passaggi:

1. Apri **Telegram** e cerca il bot **@BotFather**.
2. Invia il comando `/start` e poi `/newbot` per creare il tuo bot.
3. Segui le istruzioni fornite da **BotFather** per ottenere il **Token** del tuo bot.

### 2. Ottenere il `chat_id`

1. Avvia una conversazione con il tuo bot su Telegram.
2. Usa il metodo `getUpdates` per ottenere il tuo `chat_id`. Puoi fare una richiesta HTTP per ottenere il JSON con il tuo ID utente:

   ```bash
   https://api.telegram.org/bot<TOKEN>/getUpdates
   ```

   Nell'output JSON, troverai il campo `chat` con il tuo `chat_id`.

### 3. Configurazione del File `config.py`

Crea un file `config.py` nella stessa directory del progetto con le seguenti informazioni:

```python
# Configurazione del Telegram Bot
BOT_TOKEN = "il_tuo_token_del_bot"  # Sostituisci con il token del bot Telegram
CHAT_ID = "il_tuo_chat_id"  # Sostituisci con il chat_id ottenuto
```

## Requisiti

Per eseguire lo script, sono necessarie le seguenti librerie Python. Puoi installarle facilmente utilizzando `pip`:

```bash
pip install -r requirements.txt
```

### File `requirements.txt`

```
requests
beautifulsoup4
python-telegram-bot
schedule
```

## Esecuzione

### 1. Esegui Manualmente lo Script

Per eseguire lo script manualmente, usa il comando:

```bash
python3 scraper_bot.py
```

Lo script eseguirà il web scraping delle transazioni politiche e invierà una notifica tramite Telegram ogni volta che un politico dell'elenco inserito ha effettuato una transazione.

### 2. Pianificazione Automatica dello Script

Se vuoi che lo script venga eseguito automaticamente ogni giorno, puoi usare il programma di pianificazione cron su un server Linux. 

Crea un file `cronjob.sh` per eseguire lo script ogni giorno:

#### `cronjob.sh`

```bash
#!/bin/bash
cd /path/to/your/project-directory  # Sostituisci con il percorso del tuo progetto
python3 scraper_bot.py
```

Poi aggiungi un cronjob per eseguire lo script ogni giorno:

```bash
crontab -e
# Aggiungi questa riga per eseguire lo script ogni giorno alle 8:00
0 8 * * * /bin/bash /path/to/your/project-directory/cronjob.sh
```

### 3. Personalizzazione

Puoi modificare il file `scraper_bot.py` per personalizzare l'elenco dei politici da monitorare. Modifica la lista `politicians_list` con i nomi dei politici che ti interessano:

```python
politicians_list = ["Politico 1", "Politico 2", "Politico 3"]
```

## Come Funziona

1. Lo script esegue il **web scraping** del sito di interesse (attualmente configurato per "QuiverQuant").
2. Estrae le transazioni dei politici dalla tabella HTML presente sulla pagina.
3. Confronta i nomi dei politici nelle transazioni con la lista di politici specificati nel file `scraper_bot.py`.
4. Se trova una transazione di uno dei politici monitorati, invia una notifica su Telegram utilizzando il bot.

## Pianificazione Automatica con `schedule`

Lo script può essere configurato per eseguire il controllo automaticamente a intervalli regolari. L'esempio di configurazione prevede l'esecuzione ogni giorno alle 8:00.

```python
import schedule
import time

def job():
    check_transactions()

# Pianifica l'esecuzione ogni giorno alle 8:00
schedule.every().day.at("08:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # Pausa di 60 secondi per eseguire il job
```

# Ecco dove puoi trovare informazioni sugli ordini degli investitori istituzionali e hedge fund:

1. **Form 13F (USA)**: Puoi consultare i report trimestrali degli investitori istituzionali tramite il **Form 13F** sul sito ufficiale della **SEC** (Securities and Exchange Commission) o su piattaforme come:
   - **WhaleWisdom** ([whalewisdom.com](https://www.whalewisdom.com/))
   - **SEC Edgar** ([sec.gov/edgar](https://www.sec.gov/edgar/searchedgar/companysearch.html))

2. **Market Data Providers**:
   - **Bloomberg**: Se hai accesso a Bloomberg Terminal, puoi usare strumenti come **IMT (Institutional Market Tracker)** e **IP (Investment Position Tracker)**.
   - **Refinitiv** e **FactSet**: Offrono accesso ai flussi di capitali istituzionali, ma sono soluzioni a pagamento. Le piattaforme come **S&P Capital IQ** forniscono anche dati dettagliati su posizioni e transazioni.

3. **Flussi di Capitali e Hedge Fund Analyses**:
   - **Hedgeye** ([hedgeye.com](https://www.hedgeye.com/)): Offre report e analisi sul comportamento di hedge fund e istituzionali.
   - **Bespoke Investment Group** ([bespokeinvest.com](https://www.bespokeinvest.com/)): Fornisce report e indicatori sui movimenti di istituzionali.

4. **Dark Pools**:
   - Puoi monitorare i dati relativi ai **dark pools** attraverso piattaforme come **FINRA** ([finra.org](https://www.finra.org/)) o attraverso report di broker che monitorano l'attività di questi mercati privati.

5. **Piattaforme di Trading e Broker**:
   - Alcuni broker, come **Interactive Brokers**, offrono report sui flussi di ordini istituzionali, ma potrebbero essere necessari strumenti specifici per raccogliere i dati più dettagliati.

Se stai cercando dati in tempo reale, **Bloomberg** o **Refinitiv** potrebbero essere le opzioni migliori, ma sono soluzioni costose. Se ti interessa monitorare i report trimestrali (13F), allora **SEC Edgar** o **WhaleWisdom** sono ottimi punti di partenza.

Vuoi un esempio pratico su come navigare una di queste piattaforme?

## Dettagli scraper

Per creare uno scraper che monitori le transazioni finanziarie dei membri del Congresso degli Stati Uniti, uno dei siti più utilizzati è **QuiverQuant** (https://www.quiverquant.com/). Questo sito raccoglie e visualizza i dati sulle transazioni di insider trading effettuate dai membri del Congresso degli Stati Uniti, come ad esempio gli acquisti e le vendite di azioni.

Altri siti che potrebbero essere utilizzati, ma meno specifici, sono:

1. **Senate Trading** (https://www.senatetrading.com/) - Un altro sito che raccoglie informazioni sulle transazioni dei senatori.
2. **OpenSecrets.org** (https://www.opensecrets.org/) - Raccoglie dati sulle attività finanziarie dei politici, anche se la disponibilità di informazioni specifiche sui singoli acquisti di azioni può essere limitata.

Per lo scraping, supponendo che tu voglia monitorare le transazioni di insider trading dei politici, **QuiverQuant** è probabilmente la fonte più interessante.

### Come raccogliere i dati:

- **URL di esempio**: `https://www.quiverquant.com/sources/senatetrading`
- **Tabella da cui raccogliere i dati**: Potresti estrarre informazioni da una tabella HTML che mostra il nome del politico, la transazione (acquisto/vendita), il titolo dell'azione e la data.

### Come configurare il tuo scraper:

1. **Accedi alla pagina contenente i dati** (ad esempio, su QuiverQuant).
2. **Identifica la struttura HTML** della tabella (utilizzando strumenti come l'ispettore del browser).
3. **Scrape i dati** della tabella, estraendo le informazioni rilevanti (nome politico, tipo di transazione, azioni, data).

### Avvertenza:
Fai attenzione alle politiche di scraping dei siti web. Verifica sempre i **Termini di Servizio** del sito per assicurarti che lo scraping sia permesso. Inoltre, se hai bisogno di raccogliere dati a lungo termine, potresti considerare di farlo in modo responsabile per non sovraccaricare i server del sito.

## Contribuire

Se desideri contribuire a questo progetto, fai una fork di questo repository, aggiungi le tue modifiche e invia una pull request.

## Licenza

Questo progetto è sotto la licenza MIT. Puoi usarlo, modificarlo e distribuirlo liberamente.

---

Buon lavoro e buona fortuna con il tuo progetto di scraping e notifiche via Telegram!


### Conclusione

Questo file `README.md` è completo e fornisce tutte le informazioni necessarie per utilizzare il progetto, configurare il bot Telegram, pianificare l'esecuzione automatica e personalizzare l'elenco dei politici da monitorare.

Con questa guida, puoi facilmente impostare il tuo bot e avviare il processo di monitoraggio delle transazioni politiche. Se hai bisogno di ulteriori modifiche o chiarimenti, fammi sapere!