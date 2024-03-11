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
    #checks if user is already in session    
    #if not, authenticate
    if "currentuser" in session:
                return redirect(url_for("lobby", user = "HEHE"))

    if request.method == "POST":
        mode = request.form["mode"]
        
        #checks what form it came from
        # login or signin
        if mode == "login":
            username = request.form["login-username"]
            password = request.form["login-password"]
            
            if username == "hehe" and password == "hehe":
                flash("Login successful", "info")
                session["currentuser"] = "HEHE"

                #redirect  to lobby page
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
    if "currentuser" in session:
        return render_template("lobby.html")     
    return redirect(url_for("login"))

@app.route("/logout")
def logout():

    session.pop("currentuser", None)
    return redirect(url_for("login", model = "false"))

@app.route("/level")
def level():
    return render_template("level.html") 

if __name__ == "__main__":
    app.run()
