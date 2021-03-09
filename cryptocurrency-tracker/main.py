from flask import Flask, render_template, request
import requests

# Variables
name = ""
cost = 0

# Making the app
app = Flask(__name__)

# Making the home and main page


@app.route("/", methods=['GET', 'POST'])
def home():
    global name
    global cost

    if request.method == "POST":
        print(request.form)
        webpage = request.form
        crypt_name = str(webpage['moneyInp'])
        url = f"https://api.coingecko.com/api/v3/coins/{crypt_name}"

        response = requests.get(url)

        jsonated_response = response.json()

        print(jsonated_response)

        try:
            name = (jsonated_response['id'])
            cost = (jsonated_response['market_data']['current_price']['usd'])
        except:
            name = "Could not find coin"
            cost = "Please try another one"

    return render_template('index.html', crypt_name=name, crypt_price=cost)


# Running the app
if __name__ == '__main__':
    app.run(debug=True)
