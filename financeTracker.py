from flask import Flask, render_template

app = Flask(__name__)

purchases = [
    {
        'item': 'Item1',
        'total': 0,
        'date_recorded': 'March 7, 2023'
    },
    {
        'item': 'Item2',
        'total': 0,
        'date_recorded': 'March 7, 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/financePortal")
def finance_portal():
    return render_template('financePortal.html', purchases=purchases)


if __name__ == '__main__':
    app.run(debug=True)
