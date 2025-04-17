from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your CurrencyFreaks API URL
API_URL = "https://api.currencyfreaks.com/latest?apikey=7d834c2fd2a044fab04359ee9655b90b"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    currencies = []

    # Fetch the latest rates
    response = requests.get(API_URL)
    data = response.json()

    if "rates" in data:
        currencies = list(data['rates'].keys())

        if request.method == 'POST':
            from_currency = request.form['from_currency']
            to_currency = request.form['to_currency']
            amount = float(request.form['amount'])

            # Convert input to USD, then from USD to target
            if from_currency == 'USD':
                rate = float(data['rates'][to_currency])
                result = round(amount * rate, 2)
            elif to_currency == 'USD':
                rate = float(data['rates'][from_currency])
                result = round(amount / rate, 2)
            else:
                rate_from = float(data['rates'][from_currency])
                rate_to = float(data['rates'][to_currency])
                usd_amount = amount / rate_from
                result = round(usd_amount * rate_to, 2)

    else:
        result = "Error fetching conversion data."

    return render_template('index.html', result=result, currencies=currencies)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

