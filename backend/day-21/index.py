from flask import Flask, Blueprint
app = Flask(__name__)

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return "Welcome to the homepage"

@main_bp.route('/about')
def about():
    return "This is the about page"

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run()
