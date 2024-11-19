from flask import Flask, render_template
from .model import db
from .controller.auth_controller import auth_bluprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://root:root@localhost:5432/postgres"

db.init_app(app)
with app.app_context():
    db.create_all()

app.register_blueprint(auth_bluprint, url_prefix="/auth")


@app.route("/")
def index():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
