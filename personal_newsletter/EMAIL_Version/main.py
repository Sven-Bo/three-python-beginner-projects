import os
import smtplib
from email.message import EmailMessage
from pathlib import Path

import requests
from dotenv import load_dotenv


def get_useless_fact():
    r = requests.get("https://uselessfacts.jsph.pl/today.json?language=en")
    if r.status_code !=200:
        return None
    return r.json()["text"]


def get_btc_rate():
    r = requests.get('https://api.coindesk.com/v2/bpi/currentprice.json')
    if r.status_code != 200:
        return None
    return r.json()["bpi"]["USD"]["rate"]


def get_chuck_norris_joke():
    r = requests.get(f"https://api.chucknorris.io/jokes/random")
    if r.status_code != 200:
        return None
    return r.json()["value"]



def send_email(message):
    msg = EmailMessage()
    msg["Subject"] = SUBJECT
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = EMAIL_ADDRESS

    msg.set_content(message, subtype="html")

    with smtplib.SMTP(SERVER, PORT) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())


if __name__ == "__main__":
    # Load the environment variables
    current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
    envars = current_dir / ".env"
    load_dotenv(envars)

    # Constants
    EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
    SERVER = "smtp-mail.outlook.com"
    PORT = 587
    SUBJECT = "Good Morning Message"

    # Get data from API's
    btc = get_btc_rate()
    useless_fact = get_useless_fact()
    chuck_norris_joke = get_chuck_norris_joke()

    # Construct message and send email
    message = f"""
    <html>
      <body>
        <p><strong>Good morning,</strong></p>
        <p>The current BTC price is: {btc} USD</p>
        <p>Here is a chuck norris joke for you: {chuck_norris_joke}</p>
        <p>Did you know...</p>
        <p>{useless_fact}</p>
        <p><strong>Have a sventastic day!</strong></p>
      </body>
    </html>
    """
    send_email(message)



