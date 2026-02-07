from flask import Blueprint, render_template, request, url_for,flash,session,redirect

auth_bp = Blueprint('auth', __name__)

# H.W we have to make login and sign up for everyone

USER_CREDENTIALS = {
    'username' : 'admin',
    'password' : '1234'
}

@auth_bp.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS["password"]:
            session['user'] = username
            flash("Login Succesful", 'success')
            return redirect(url_for('tasks.view_tasks'))
        else:
            flash("Invalid username or Password", 'danger')
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Logged out','info')
    return redirect(url_for('auth.login'))
