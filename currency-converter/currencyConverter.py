import requests

API_KEY = ''
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]
def convert_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None
while True:
    base = input("Enter the base currency (l for list of currencies, q for quit)").upper()
    if base == "Q":
        break
    if base == "L":
        print("List of Currencies:")
        for ticker in CURRENCIES:
            print(f"{ticker}")
        continue
    data = convert_currency(base)
    if not data:
        continue
    del data[base]
    for ticker, value in data.items():
        print(f"{ticker}: {round(value,2)}")
