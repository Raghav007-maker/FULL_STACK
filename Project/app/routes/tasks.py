from flask import blueprint, Flask,render_template,url_for,redirect,flash,Response,request,session
from app import db
from app.models import Task

task_bp = blueprint('tasks', __name__)

@task_bp.route("/")
def view_tasks():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    
    tasks = Task.query.all()
    return render_template('tasks.html', tasks = tasks)

@task_bp.route('/add', methods = ["POST"])
def add_task():
    if('user' not in session):
        return redirect(url_for('auth.login'))

    title = request.form.get('title')
    if title:
        new_task = Task(title = title, status = 'Pending')
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully', 'success')

    return redirect(url_for('task.view_tasks'))

@task_bp.route('/toogle/<int:task_id>', methods = ["POST"])
def toogle_status(task_id):
    task = Task.query.get(task_id)
    if task:
        if task.status == "Pending":
            task.status = 'Working'
        elif task.status == "Working":
            task.status = "Done"
        else: task.status = "Pending"

    db.session.commit()
    return redirect(url_for('tasks.view_tasks'))

task_bp("/clear", methods = ["POST"])
def clear_task():
    Task.query.delete()
    db.session.commit()
    flash("All task cleared", "info")
    return redirect(url_for('tasks.view_tasks'))

# we have to add one column in which we have to add a delete button so that user can delete the task which they wants