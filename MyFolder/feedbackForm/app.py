from flask import Flask, request, redirect, url_for, flash, render_template

app = Flask(__name__)
app.secret_key = "my-secret-key"

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("username")
        if not name:
            flash("Name Not Found", "error")
            return redirect(url_for("feedback"))

        flash(f"Thanks {name}", "success")
        message = request.form.get("message")
        return render_template("thankyou.html", user=name, message=message)

    return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True)