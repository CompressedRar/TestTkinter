from flask import *

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content=["jerald", "owa"])
if __name__ == "__main__":
    app.run()