import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "mydb.db"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)
'''
@app.route('/',methods=['GET','POST'])
def home():
    data=request.form
    print(data)
    return render_template('index.html')

@app.route('/forms/<int:id>')
def forms(id):
'''


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.form == 'POST':
        name = Detail(name=request.form.get("name"))
        phone = Detail(phone=request.form.get("phone"))
        email = Detail(email=request.form.get("email"))
        db.session.add(name)
        db.session.add(phone)
        db.session.add(email)
        db.session.commit()
    # d=Detail.query.all()
    return render_template("home.html")


class Detail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
   # phone = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40),nullable=False,unique=True)

    def __repr__(self):
        return "<name: {},phone: {} , email:{} >".format(self.name, self.phone, self.email)


if __name__ == '__main__':
    app.run(debug=True)
