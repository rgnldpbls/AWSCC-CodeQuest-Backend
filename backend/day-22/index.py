from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    title = "My Web App"
    user = "Regienald"
    return render_template("index.html", title=title, user=user)

@app.route('/about')
def about():
    title = 'About Us'
    content = 'Welcome to our About Us page!'
    return render_template('about.html', title=title, content=content)

if __name__ == '__main__':
    app.run()