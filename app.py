from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/add-income", methods=["POST", "GET"])
def income():
    return render_template("income.html")

@app.route("/add-expenses", methods=["POST", "GET"])
def expenses():
    return render_template("expense.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

app.run(debug=True)