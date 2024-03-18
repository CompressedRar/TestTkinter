from flask import *
from datetime import *
from flask_sqlalchemy import *
import os
from models import *
app = Flask(__name__)
app.secret_key = "hehe"
app.permanent_session_lifetime = timedelta(minutes=30)

#models
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)



#views
    
@app.before_request
def create_tables():
    
     db.create_all()

@app.route("/")
def home():
    all = Students.query.filter_by(firstname = "testuser")
    
    print()
    #db.session.add(newacc)
    db.session.commit()
    
    return render_template("index.html")

@app.route("/createlevel")
def create():
    return render_template("submitlevel.html")
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
            passwo = request.form["login-password"]
            
            authenticate = Students.query.filter_by(firstname = username, password = passwo).first()
            print(authenticate.firstname)
            if authenticate:
                flash("Login successful", "info")
                session["currentuser"] = authenticate.firstname

                #redirect  to lobby page
                return redirect(url_for("lobby", user = authenticate.firstname))
            else: 
                flash("The account doesn't exists!", "info")
                return render_template("login.html", model = "true")
            
        elif mode == "signin":
            #signup
            #checks if passwords match
            username = request.form["signup-username"]

            alluser = Students.query.filter_by(firstname = username).all()

            #check if user already exists
            if alluser.count(0) > 0:
                flash("Username already existed!!", "signin")
                return render_template("login.html",model="false")             
            password = request.form["signup-password"]
            confirmpassword = request.form["signup-confirmpassword"]
            #ayusing sa javascript yung textchanged event
            newuser = Students(username, password, confirmpassword)
            db.session.add(newuser)
            db.session.commit()
            get_flashed_messages(category_filter="signin").clear()

            
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
