from flask import Flask, render_template

from python import bitcoin_wallet as btc

app = Flask(__name__)


@app.route("/")
def homepage():
    wallet = "3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"
    balance = btc.get_curent_balance("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC")
    sent = btc.get_total_sent("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC")
    recieved = btc.get_total_received("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC")
    first_seen = btc.get_first_seen("3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC")
    return render_template("index.html", title="Hashboard", wallet=wallet, balance=balance, sent=sent, received=recieved, first_seen=first_seen)


if __name__ == "__main__":
    app.run(debug=True)
