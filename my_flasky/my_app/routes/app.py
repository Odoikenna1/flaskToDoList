from flask import Blueprint, render_template, request, redirect, url_for

user_bp = Blueprint("user_bp", __name__)

to_do_lst = [{"task": "Sample Todo", "done": False}]


@user_bp.route('/')
def home():
    return render_template('index.html', to_do_lst=to_do_lst)


@user_bp.route('/add', methods=["POST"])
def add():
    if request.form['task'] != " " and request.form['task'] != "":
        task = request.form['task']
        to_do_lst.append({"task": task, "done": False})
        return redirect(url_for("user_bp.home"))
    else:
        return "Invalid input."


@user_bp.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    if index < 0 or index >= len(to_do_lst):
        return redirect(url_for("user_bp.index"))
    task = to_do_lst[index]
    if request.method == "POST":
        task['task'] = request.form['task']
        return redirect(url_for("user_bp.home"))
    else:
        return render_template("edit.html", task=task, index=index)


@user_bp.route("/check/<int:index>")
def check(index):
    to_do_lst[index]['done'] = not to_do_lst[index]['done']
    return redirect(url_for("user_bp.home"))


@user_bp.route("/delete/<int:index>")
def delete(index):
    del to_do_lst[index]
    return redirect(url_for("user_bp.home"))
