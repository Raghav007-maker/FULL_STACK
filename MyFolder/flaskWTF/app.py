from flask import Flask,redirect,Response,url_for,render_template,request,flash
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = 'my-secret-key'

@app.route("/", methods = ["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        flash(f"Welcome {name}! You Registered Succesfully", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)
     

@app.route("/success")
def success():
    return render_template("success.html")

