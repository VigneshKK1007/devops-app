from werkzeug.security import check_password_hash, generate_password_hash

from extensions import db


class User(db.Model):
    """User account stored in the SQLite database."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        """Hash and store a password instead of saving the raw text."""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """Return True when the supplied password matches the stored hash."""
        return check_password_hash(self.password, password)

    def to_dict(self):
        """Serialize safe user data for JSON responses."""
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }
