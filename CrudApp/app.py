from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        if name and email:  # avoid inserting None
            new_employee = Employee(name=name, email=email)  # use different variable name
            db.session.add(new_employee)
            db.session.commit()
        return redirect(url_for("home"))  # redirect after POST

    allemployee = Employee.query.all()
    return render_template("index.html", allemployee=allemployee)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/delete/<int:sno>")
def delete(sno):
    employee = Employee.query.filter_by(sno=sno).first()
    db.session.delete(employee)
    db.session.commit()
    return redirect("/")

@app.route("/update/<int:sno>", methods = ["POSt", "GET"])
def update(sno):
    if request.method == "POST":
        name = request.form.get("name")
        address = request.form.get("email")
        employee = Employee.query.filter_by(sno = sno).first()
        employee.name = name
        employee.email = address
        db.session.add(employee)
        db.session.commit()
        return redirect("/")

    employee = Employee.query.filter_by(sno=sno).first()
    return render_template("update.html", employee=employee)

if __name__ == "__main__":
    app.run(debug=True)