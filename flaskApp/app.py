from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
#return "<p>This is My Home Page</p>"

@app.route("/about")
def about():
    return render_template("about.html")
#
    return "<p>About Page</p>"

@app.route("/dashboard/<name>")
def dashboard(name):
    items = ["apple", "orange", "mango", "pear"]
    return render_template("dashboard.html", username=name, data=items)

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)