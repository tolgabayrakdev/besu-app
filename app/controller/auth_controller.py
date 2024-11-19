from flask import Blueprint, render_template, redirect

auth_bluprint = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bluprint.route("/login")
def login():
    return render_template("auth/login.html")

@auth_bluprint.route("/register")
def register():
    return render_template("auth/register.html")