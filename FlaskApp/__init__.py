import os
from flask import Flask, render_template
from .extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY')
app.config['SITE_NAME'] = os.getenv('FLASK_SITE_NAME')
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
    userprofile = db.session.execute(db.select(Profile)).scalar_one_or_none()
    return render_template("index.html", profile=userprofile, title="Home")


if __name__ == "__main__":
    app.run()
