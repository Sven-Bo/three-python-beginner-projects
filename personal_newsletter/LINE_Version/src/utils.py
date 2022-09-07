import requests


def get_useless_fact():
    r = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
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





