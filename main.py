from flask import Flask, render_template, request
from python import mock_bitcoin_wallet as btc
from forms import forms

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homepage():
    search = forms.WalletSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template("index.html", form=search, title="Hashboard")


@app.route('/results', methods=['GET', 'POST'])
def search_results(search):
    search_string = search.data['search']
    wallet = btc.Wallet(search_string)
    search = forms.WalletSearchForm(request.form)
    if wallet.get_exists():
        return render_template('results.html', results=search_string, wallet=wallet, form=search, title="Hashboard")
    else:
        return render_template('results_not_found.html', form=search, title="Hashboard")


if __name__ == "__main__":
    app.run(debug=True)
