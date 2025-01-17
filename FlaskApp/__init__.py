from flask import Flask, render_template
from .extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tbc.db'
db.init_app(app)

with app.app_context():
    from FlaskApp.Models.Profile import Profile
    from FlaskApp.Models.Project import Project
    from FlaskApp.Models.Employer import Employer
    from FlaskApp.Models.Consulting import Consulting
    from FlaskApp.Models.Education import Education
    db.create_all()

    profile = db.session.execute(db.select(Profile)).fetchone()
    if profile is None:
        profile = Profile()
        db.session.add(profile)
        db.session.commit()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello/<name>", methods=['GET'])
def hello(name: str):
    return f"hello {name}"


@app.route("/module")
def module():
    return f"loaded from FlaskApp.package.module = {MODULE_VALUE}"


if __name__ == "__main__":
    app.run()
