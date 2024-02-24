from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SECRET_KEY"] = "thisissecret"

db = SQLAlchemy(app)

#Model/Schema for the database
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    web_url = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Password %r>' % self.email

with app.app_context():
    db.create_all()

#Routes
@app.route("/")
def index():
    passList = Password.query.all()
    return render_template("index.html", passList=passList)

@app.route("/add", methods=["GET", "POST"])
def add_password():
    if request.method == "POST":
        web_url = request.form["web_url"]
        email = request.form["email"]
        password = request.form["password"]
        details = Password(web_url=web_url, email=email, password=password)
        db.session.add(details)
        db.session.commit()
        return redirect("/")   
    return "Hello World"

@app.route("/update")
def update_password():
    return "Hello World"

@app.route("/delete")
def delete_password():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True) # development & production set to False