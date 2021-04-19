import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydb.db"))
print("print:", database_file)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)


# validation
class Form(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=80)])
    remember = BooleanField('remember me')


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Form()
    if form.validate_on_submit():
        name = Detail(name=request.form.get("name"))
        phone = Detail(phone=request.form.get("phone"))
        email = Detail(email=request.form.get("email"))
        db.session.add(id)
        db.session.add(name)
        db.session.add(phone)
        db.session.add(email)
        db.session.commit()
    d = Detail.query.all()
    return render_template("home.html", d=d)


class Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)

    def __repr__(self):
        return "<id: {}, name: {},phone: {} , email:{} >".format(self.id, self.name, self.phone, self.email)


if __name__ == '__main__':
    app.run(debug=True)
