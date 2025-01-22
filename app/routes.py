from flask import Blueprint, render_template, request
bp = Blueprint("main", "__name__")

@bp.route("/")
def get_startpage():
    return render_template("index.html")

@bp.route("/calculator", methods=["GET","POST"])
def calculator():
    print("HIT ROUTE")
    from .models import Calculation
    from app import db
    if request.method == "POST":
        expression = request.form["expression"]
        try:
            result = eval(expression, {"__builtins__": None}, {})
            new_calc = Calculation(expression = expression,result=result)
            db.session.add(new_calc)
            db.session.commit()
        except Exception as e:
            print("Fel i beräkningen")
    calc = Calculation.query.all()
    return render_template("calculator.html", calculations=calc)
        