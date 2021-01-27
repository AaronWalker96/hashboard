from flask import Flask, render_template, request
from python import bitcoin_wallet as btc
from forms import forms

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homepage():
    wallet = "3QJmV3qfvL9SuYo34YihAf3sRCW3qSinyC"

    search = forms.WalletSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template("index.html", form=search, title="Hashboard")


@app.route('/results', methods=['GET', 'POST'])
def search_results(search):
    search_string = search.data['search']
    wallet = btc.Wallet(search_string)

    # if search.data['search'] == '':
    #     qry = db_session.query(Album)
    #     results = qry.all()
    # if not results:
    #     flash('No results found!')
    #     return redirect('/')
    # else:
    #     # display results

    search = forms.WalletSearchForm(request.form)

    return render_template('results.html', results=search_string, wallet=wallet, form=search, title="Hashboard")


if __name__ == "__main__":
    app.run(debug=True)
