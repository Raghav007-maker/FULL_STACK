from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/about")
def about():
    return "this is a about page"


@app.route("/contact")
def contact():
    return "Contact Us"

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "POST":
        return "You sent Data!"
    else:
        return "You are Viewing the data!"

if __name__ == "__main__":
    app.run(debug = True)
 