from flask import Flask, render_template, request
from python import bitcoin_wallet as btc
from forms import forms

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homepage():
    search = forms.WalletSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template("index.html", form=search, title="Hashboard Search")


@app.route('/results', methods=['GET', 'POST'])
def search_results(search):
    search_string = search.data['search']
    wallet = btc.Wallet(search_string)
    search = forms.WalletSearchForm(request.form)
    if wallet.get_exists():
        return render_template('results.html', results=search_string, wallet=wallet, form=search, title="Hashboard Search")
    else:
        return render_template('results_not_found.html', form=search, title="Hashboard Search")
    

@app.route('/settings')
def settings_page():
    return render_template("settings.html", title="Settings")


if __name__ == "__main__":
    app.run(debug=True)
