from flask import Flask, render_template
from flask_ultime import FlaskUltime


app = Flask(__name__)

# Initialize FlaskUltime
tailwind = FlaskUltime(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

