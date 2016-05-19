from flask import Flask, render_template

app = Flask(__name__)


app.secret_key = 'secret'



@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")

if __name__ == "__main__":
    app.run(debug=True)