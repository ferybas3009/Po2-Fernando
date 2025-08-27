from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hidro")
def reaper():
    return render_template("hidro.html")

@app.route("/comercial")
def ghost():
    return render_template("comercial.html")

@app.route("/jato")
def sea():
    return render_template("jato.html")

if __name__ == "__main__":
    app.run(debug=True)
