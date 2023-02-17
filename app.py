
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://sql12598326:KLGhaq5F9D@http://sql12.freemysqlhosting.net/db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    return app



app = create_app()
db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    course = db.Column(db.String(100))

    def __init__(self,name,course):
        self.name = name
        self.course = course

@app.route('/')
def Index():
    return render_template ("index.html")
@app.route('/insert' , methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form['name']
        course = request.form['course']

        my_data = Data(name,course)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug = True)
