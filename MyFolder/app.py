from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/submit",  methods = ["POST"])
def submit():
    username = request.form.get("username")
    password = request.form.get("password")

    action = request.form.get("login")

    valid_user = {
        'admin':"123",
        'sagar':'sag',
        'rajat':"546"
    }
    if username in valid_user and password == valid_user.get(username):
        return render_template("welcome.html", name2 = username)
    
    else:
        return "Invalid credentials"
    
    
if __name__ == "__main__":
    app.run(debug = True)
