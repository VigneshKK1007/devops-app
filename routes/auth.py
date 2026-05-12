from functools import wraps

from flask import Blueprint, flash, redirect, render_template, request, session, url_for

from extensions import db
from models.user import User


auth_bp = Blueprint("auth", __name__)


def get_current_user():
    """Load the currently logged-in user from the session."""
    user_id = session.get("user_id")
    if not user_id:
        return None
    return db.session.get(User, user_id)


def login_required(view):
    """Redirect visitors to login before allowing access to protected pages."""
    @wraps(view)
    def wrapped_view(*args, **kwargs):
        if get_current_user() is None:
            flash("Please log in to access that page.", "warning")
            return redirect(url_for("auth.login"))
        return view(*args, **kwargs)

    return wrapped_view


@auth_bp.app_context_processor
def inject_user():
    """Make current_user available in every template."""
    return {"current_user": get_current_user()}


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")

        if not username or not email or not password:
            flash("Username, email, and password are required.", "error")
            return render_template("register.html")

        if User.query.filter_by(username=username).first():
            flash("That username is already taken.", "error")
            return render_template("register.html")

        if User.query.filter_by(email=email).first():
            flash("That email is already registered.", "error")
            return render_template("register.html")

        user = User(username=username, email=email)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash("Account created. You can now log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "")
        user = User.query.filter_by(email=email).first()

        if user is None or not user.check_password(password):
            flash("Invalid email or password.", "error")
            return render_template("login.html")

        session.clear()
        session["user_id"] = user.id

        flash("Welcome back!", "success")
        return redirect(url_for("main.dashboard"))

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("main.home"))
