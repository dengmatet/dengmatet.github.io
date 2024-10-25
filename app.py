from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
from flask_session import Session

# Configure app
app = Flask(__name__)



# Reload after saving
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session
app.config["SESSION_PERMANENT"] = False

# Configure the Session to use filesystem
app.config["SESSION_TYPE"] = "filesystem"

# Initialize the session extension
Session(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    # Validate submission
    if request.method == "POST":
        session["email"] = request.form.get("email")
        session["password"] = request.form.get("password")
    return render_template("login.html" , placeholder=session.get("fname"))

@app.route("/logout")
def logout():
    # Remove user session data
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
