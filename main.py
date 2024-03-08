from flask import *

app = Flask(__name__)
app.secret_key = "hehe"
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        mode = request.form["mode"]
        
        if mode == "login":
            return f"{mode}"
        else:
            
            password = request.form["signup-password"]
            confirmpassword = request.form["signup-confirmpassword"]

            if password != confirmpassword:
                flash("The passwords don't match!", "info")
                return render_template("login.html", model = "false")



            
    return render_template("login.html",model="true")

if __name__ == "__main__":
    app.run()
