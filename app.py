from flask import Flask, render_template
from models import db, User

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Aditi123@#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aditi.db'

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True, port=5001)

