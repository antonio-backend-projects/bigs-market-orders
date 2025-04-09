import requests
from bs4 import BeautifulSoup
from telegram import Bot
import time
import schedule

# Funzione per inviare notifiche su Telegram
def send_telegram_message(message, bot_token, chat_id):
    bot = Bot(token=bot_token)
    bot.send_message(chat_id=chat_id, text=message)

# Funzione per lo scraping dei dati
def scrape_transactions():
    url = "https://www.quiverquant.com/sources/senatetrading"  # Sostituisci con il URL del sito desiderato
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    politicians_data = []

    # Supponiamo che le transazioni siano in una tabella HTML
    for row in soup.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) > 0:
            name = cols[0].text.strip()
            transaction = cols[1].text.strip()  # Azione, tipo di transazione, ecc.
            date = cols[2].text.strip()
            politicians_data.append(f"{name} ha comprato/venduto {transaction} il {date}")

    return politicians_data

# Funzione principale per il controllo e notifica
def check_transactions():
    # Elenco dei politici di interesse
    politicians_list = ["Politico 1", "Politico 2", "Politico 3"]  # Sostituisci con i nomi che ti interessano

    # Scrape delle transazioni
    transactions = scrape_transactions()

    # Configurazioni per il bot Telegram
    from config import BOT_TOKEN, CHAT_ID  # Importa il token e chat_id dal file di configurazione

    # Controlla se qualcuno dei politici desiderati ha effettuato delle transazioni
    for transaction in transactions:
        for politician in politicians_list:
            if politician in transaction:
                # Invia una notifica via Telegram
                send_telegram_message(transaction, BOT_TOKEN, CHAT_ID)
                print(f"Notifica inviata per {politician}: {transaction}")

# Funzione per schedulare l'esecuzione giornaliera dello script
def schedule_jobs():
    # Pianifica l'esecuzione dello script ogni giorno alle 8:00
    schedule.every().day.at("08:00").do(check_transactions)

    while True:
        schedule.run_pending()
        time.sleep(60)  # Pausa di 60 secondi per eseguire il job

if __name__ == "__main__":
    schedule_jobs()
