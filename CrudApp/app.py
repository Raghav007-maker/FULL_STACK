from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "mySecretKey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):   # Capitalized class name
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(500), nullable=False)

# Create table if not exists
with app.app_context():
    db.create_all()

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form.get("name", '').strip()
        email = request.form.get("email", '').strip()
        if name and email:
            new_employee = Employee(name=name, email=email)
            db.session.add(new_employee)
            db.session.commit()
        else:
            flash("All Fields Required", "danger")
            return redirect(url_for("home"))
        return redirect(url_for("home"))

    allemployee = Employee.query.all()
    return render_template("index.html", allemployee=allemployee)


@app.route("/update/<int:sno>", methods=["POST", "GET"])
def update(sno):
    employee = Employee.query.filter_by(sno=sno).first()
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        if employee:
            employee.name = name
            employee.email = email
            db.session.commit()
        return redirect("/")
    return render_template("update.html", employee=employee)


@app.route("/delete/<int:sno>")
def delete(sno):
    employee = Employee.query.filter_by(sno=sno).first()
    if employee:
        db.session.delete(employee)
        db.session.commit()
    return redirect("/")
