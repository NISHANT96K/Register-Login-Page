from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello!!"

@app.route("/")
def about():
    return "This is About Page"

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        print(username, password)
        return "Form recived"
    return render_template("login.html")

if __name__ == ("__main__"):
    app.run(debug = True)