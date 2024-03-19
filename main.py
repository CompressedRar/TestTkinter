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
def insertelements():
    
    db.session.add(Elements(1,"H", "Hydrogen", "1.Hydrogen_.jpg"))
    db.session.add(Elements(2,"He", "Helium", "2.Helium.png"))
    db.session.add(Elements(3,"Li", "Lithium", "3.Lithium_.jpg"))
    db.session.add(Elements(4,"Be", "Beryllium", "4.Beryllium.jpg"))
    db.session.add(Elements(5,"B", "Boron", "5.Boron.png"))
    db.session.add(Elements(6,"C", "Carbon", "6.Carbon.png"))
    db.session.add(Elements(7,"N", "Nitrogen", "7.Nitrogen.jpg"))
    db.session.add(Elements(8,"O", "Oxygen", "8.Oxygen_.jpg"))
    db.session.add(Elements(9,"F", "Fluorine", "9.Fluorine_.jpg"))
    db.session.add(Elements(10,"Ne", "Neon", "10.Neon.png"))
    db.session.add(Elements(11,"Na", "Sodium", "11.Sodium.png"))
    db.session.add(Elements(12,"Mg", "Magnesium", "12.Magnesium.jpg"))
    db.session.add(Elements(13,"Al", "Aluminium", "13.Aluminium.png"))
    db.session.add(Elements(14,"Si", "Silicon", "14.Silicon.png"))
    db.session.add(Elements(15,"P", "Phosporus", "15.Phosporus.png"))
    db.session.add(Elements(16,"S", "Sulfur", "16.Sulfur.png"))
    db.session.add(Elements(17,"Cl", "Chlorine", "17.Chlorine.jpg"))
    db.session.add(Elements(18,"Ar", "Argon", "18.Argon.png"))
    db.session.add(Elements(19,"K", "Potassium", "19.Potassium.jpg"))
    db.session.add(Elements(20,"Ca", "Calcium", "20.Calcium.png"))
    db.session.add(Elements(21,"Sc", "Scandium", "21.Scandium.png"))
    db.session.add(Elements(22,"Ti", "Titanium", "22.Titanium.png"))
    db.session.add(Elements(23,"V", "Vanadium", "23.Vanadium.png"))
    db.session.add(Elements(24,"Cr", "Chromium", "24.Chromium.png"))
    db.session.add(Elements(25,"Mn", "Manganese", "25.Manganese.png"))
    db.session.add(Elements(26,"Fe", "Iron", "26.Iron.png"))
    db.session.add(Elements(27,"Co", "Cobalt", "27.Cobalt.png"))
    db.session.add(Elements(29,"Cu", "Copper", "29.Copper.png"))
    db.session.add(Elements(28,"Ni", "Nickel", "28.Nickel.png"))
    db.session.add(Elements(30,"Zn", "Zinc", "30.Zinc.png"))
    db.session.add(Elements(31,"Ga", "Gallium", "31.Gallium.png"))
    db.session.add(Elements(32,"Ge", "Germanium", "32.Germanium.png"))
    db.session.add(Elements(33,"As", "Arsenic", "33.Arsenic.png"))
    db.session.add(Elements(34,"Se", "Selenium", "34.Selenium.png"))
    db.session.add(Elements(35,"Br", "Bromine", "35.Bromine.png"))
    db.session.add(Elements(36,"Kr", "Krypton", "36.Krypton.png"))
    db.session.add(Elements(37,"Rb", "Rubidium", "37.Rubidium.png"))
    db.session.add(Elements(38,"Sr", "Strontium", "38.Strontium.png"))
    db.session.add(Elements(39,"Y", "Yttrium", "39.Yttrium.png"))
    db.session.add(Elements(40,"Zr", "Zirconium", "40.Zirconium.png"))
    db.session.add(Elements(41,"Nb", "Niobium", "41.Niobium.png"))
    db.session.add(Elements(42,"Mo", "Molybdenum", "42.Molybdenum.png"))
    db.session.add(Elements(43,"Tc", "Technitium", "43.Technitium.png"))
    db.session.add(Elements(44,"Ru", "Ruthenium", "44.Ruthenium.png"))
    db.session.add(Elements(45,"Rh", "Rhodium", "45.Rhodium.png"))
    db.session.add(Elements(46,"Pd", "Palladium", "46.Palladium.png"))
    db.session.add(Elements(47,"Ag", "Silver", "47.Silver.png"))
    db.session.add(Elements(48,"Cd", "Cadmium", "48.Cadmium.png"))
    db.session.add(Elements(49,"In", "Indium", "49.Indium.png"))
    db.session.add(Elements(51,"Sb", "Antimony", "51.Antimony.jpg"))
    db.session.add(Elements(52,"Te", "Tellurium", "52.Tellurium.jpg"))
    db.session.add(Elements(53,"I", "Iodine", "53.Iodine.png"))
    db.session.add(Elements(50,"Sn", "Tin", "50.Tin.png"))
    db.session.add(Elements(54,"Xe", "Xenon", "54.Xenon.png"))
    db.session.add(Elements(55,"Cs", "Caesium", "55.Caesium.jpg"))
    db.session.add(Elements(56,"Ba", "Barium", "56.Barium.png"))
    db.session.add(Elements(57,"La", "Lanthanium", "57.Lanthanium.jpg"))
    db.session.add(Elements(58,"Ce", "Cerium", "58.Cerium.png"))
    db.session.add(Elements(59,"Pr", "Praseodymium", "59.Praseodymium.jpg"))
    db.session.add(Elements(60,"Nd", "Neodymium", "60.Neodymium.jpg"))
    db.session.add(Elements(61,"Pm", "Promethium", "61.Promethium.jpg"))
    db.session.add(Elements(62,"Sm", "Samarium", "62.Samarium.jpg"))
    db.session.add(Elements(64,"Gd", "Gadolinium", "64.Gadolinium.jpg"))
    db.session.add(Elements(65,"Tb", "Terbium", "65.Terbium.jpg"))
    db.session.add(Elements(63,"Eu", "Europium", "63.Europium.jpg"))
    db.session.add(Elements(66,"Dy", "Dysprosium", "66.Dysprosium.jpg"))
    db.session.add(Elements(67,"Ho", "Holmium", "67.Holmium.jpg"))
    db.session.add(Elements(68,"Er", "Erbium", "68.Erbium.png"))
    db.session.add(Elements(69,"Tm", "Thulium", "69.Thulium.jpg"))
    db.session.add(Elements(70,"Yb", "Ytterbium", "70.Ytterbium.jpg"))
    db.session.add(Elements(71,"Lu", "Lutetium", "71.Lutetium.jpg"))
    db.session.add(Elements(72,"Hf", "Hafnium", "72.Hafnium.png"))
    db.session.add(Elements(73,"Ta", "Tantalum", "73.Tantalum.jpg"))
    db.session.add(Elements(74,"W", "Tungsten", "74.Tungsten.jpg"))
    db.session.add(Elements(75,"Re", "Rhenium", "75.Rhenium.jpg"))
    db.session.add(Elements(76,"Os", "Osmium", "76.Osmium.png"))
    db.session.add(Elements(77,"Ir", "Iridium", "77.Iridium.jpg"))
    db.session.add(Elements(78,"Pt", "Platinum", "78.Platinum.jpg"))
    db.session.add(Elements(79,"Au", "Gold", "79.Gold.png"))
    db.session.add(Elements(80,"Hg", "Mercury", "80.Mercury.jpg"))
    db.session.add(Elements(81,"Tl", "Thallium", "81.Thallium.jpg"))
    db.session.add(Elements(82,"Pb", "Lead", "82.Lead.png"))
    db.session.add(Elements(83,"Bi", "Bismuth", "83.Bismuth.jpg"))
    db.session.add(Elements(84,"Po", "Polonium", "84.Polonium.png"))
    db.session.add(Elements(85,"At", "Astatine", "85.Astatine.jpg"))
    db.session.add(Elements(86,"Rn", "Radon", "86.Radon.png"))
    db.session.add(Elements(87,"Fr", "Francium", "87.Francium.png"))
    db.session.add(Elements(88,"Ra", "Radium", "88.Radium.png"))
    db.session.add(Elements(89,"Ac", "Mercury", "80.Mercury.jpg"))
    
    


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
                print(authenticate.firstname)
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
