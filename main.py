from flask import *
from datetime import *
app = Flask(__name__)
app.secret_key = "hehe"
app.permanent_session_lifetime = timedelta(minutes=30)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    
    if request.method == "POST":
        mode = request.form["mode"]
        
        #checks what form it came from
        # login or signin
        if mode == "login":
            username = request.form["login-username"]
            password = request.form["login-password"]

            #checks if user is already in session    
            #if not, authenticate
            if "currentuser" in session:
                return redirect(url_for("lobby", user = "HEHE"))

            if username == "hehe" and password == "hehe":
                flash("Login successful", "info")
                session["currentuser"] = "HEHE"
                return redirect(url_for("lobby", user = "HEHE"))
            else: 
                return f"Invalid account"
            
        elif mode == "signin":
            #signup
            #checks if passwords match
            password = request.form["signup-password"]
            confirmpassword = request.form["signup-confirmpassword"]
            

            if password != confirmpassword:
                flash("The passwords don't match!", "info")
                return render_template("login.html", model = "false")



            
    return render_template("login.html",model="true")


@app.route("/<user>")
def lobby(user):
    return render_template("lobby.html")

if __name__ == "__main__":
    app.run()
