from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home") # can have multiple routes
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/layout")
def layout():
    return render_template("layout.html")

@app.route("/logout")
def logout():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug = True)
