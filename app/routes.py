from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint("main", "__name__")

@bp.route("/")
def get_startpage():
    return render_template("index.html")

@bp.route("/login", methods=["GET", "POST"])
def login():
    from .models import User
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("main.calculator"))
        else:
            flash("Invalid username or password")
    return render_template("login.html")

@bp.route("/register", methods=["GET", "POST"])
def register():
    from app import db
    from .models import User
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if User.query.filter_by(username=username).first():
            flash("Username already taken")
            return redirect(url_for("main.register"))
        hashed_password = generate_password_hash(password, method="scrypt")
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash("Registration complete. You will be redirected to the login page now")
        return redirect(url_for("main.login"))
    return render_template("register.html")

@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out")
    return render_template("index.html")


@bp.route("/calculator", methods=["GET","POST"])
def calculator():
    from .models import Calculation
    from app import db
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            result = eval(expression, {"__builtins__": None}, {})
            new_calc = Calculation(expression = expression,result=result, owner=current_user)
            db.session.add(new_calc)
            db.session.commit()
        except Exception as e:
            flash("Fel i beräkningen")
    calc = Calculation.query.all()
    return render_template("calculator.html", calculations=calc)
        
    