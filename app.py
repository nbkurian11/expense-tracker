from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Expense Tracker</p>"

@app.route("/add-income")
def income():
    return "<p>Add Income page</p>"

@app.route("/add-expenses")
def expenses():
    return "<p>Add expenses page</p>"

@app.route("/view-stats")
def history():
    return "<p>View Personal Stats</p>"