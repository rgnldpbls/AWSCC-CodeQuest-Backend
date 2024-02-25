from flask import Flask, render_template, request, redirect, send_file, url_for
from flask_sqlalchemy import SQLAlchemy
import csv
import time
timestr = time.strftime("%Y%m%d-%H%M%S")


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

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_password(id):
    upd_pass = Password.query.get_or_404(id)
    if request.method == "POST":
        upd_pass.web_url = request.form["web_url"]
        upd_pass.email = request.form["email"]
        upd_pass.password = request.form["password"]
        try:
            db.session.commit()
            return redirect("/")
        except:
            return "There was an error updating"
    return render_template("update.html", upd_pass=upd_pass)

@app.route("/delete/<int:id>")
def delete_password(id):
    del_pass = Password.query.get_or_404(id)
    try:
        db.session.delete(del_pass)
        db.session.commit()
        return redirect("/")
    except:
        return "There was an error deleting"

@app.route("/export")
def export_data():
    with open('dump.csv', 'w') as f:
        out = csv.writer(f)
        out.writerow(['id', 'web_url', 'email', 'password'])
        for item in Password.query.all():
            out.writerow([item.id, item.web_url, item.email, item.password])
        return send_file('dump.csv', mimetype='text/csv', download_name=f"Export_Password_{timestr}.csv", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True) # development & production set to False