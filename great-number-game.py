from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = "Husam 136633"

@app.route("/checknumber", methods=["POST"])
def checknumber():
    user_input = request.form.get("user_input")

    count = session.get("count", 0)
    acutal_number = session.get("acutal_number", random.randint(1, 100))

    session["acutal_number"] = acutal_number
    text = ""
    print(session["acutal_number"])
    print(user_input)
    boxcolor = "green"

    if int(acutal_number) > int(user_input):
        boxcolor = "aqua"
        text = "Too low !"
        session["count"] = count + 1
    elif int(acutal_number) < int(user_input):
        boxcolor = "red"
        text = "Too High !"
        session["count"] = count + 1
    else:
        boxcolor = "green"
        text = "Great Job, Correct ! # is:" + str(acutal_number)
    return render_template(
        "index.html",
        user_input=user_input,
        boxcolor=boxcolor,
        text=text,
        count=session["count"],
    )

@app.route("/restcounter", methods=["POST"])
def restcounter():
    return redirect("/")


@app.route("/")
def index():
    session.clear()
    return render_template("index.html", count=0)

if __name__ == "__main__":
    app.run(debug=True)
