from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key =  "Secret123"

@app.route("/", methods = ["GET", "POST"])
def index():
    if "number" not in session:
        session["number"]  = random.randint(1, 100)
        session["guesses"] = 0
    message = ""

    if request.method == "POST":
        guess = int(request.form["guess"])
        session["guesses"] += 1

        if guess>session["number"]:
            message = "Lower number please"
        elif guess < session["number"]:
            message = "Higher number please"
        
        else:
            message = f"Correct you guessed it in {session['guesses']} tries."
            session.pop("number")
            session.pop("guesses")
    return render_template("index.html", message=message)
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug=True)