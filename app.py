from flask import Flask, render_template
from models import db, Admin, Customer, Seller, Storage

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Aditi123@#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aditi.db'

db.init_app(app)

#predefing admin credentials
def create_admin():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        admin = Admin.query.filter_by(username='admin').first()
        if not admin:
            admin = Admin(username='admin', email='admin@example.com', contact=1234567890, password='admin123')
            db.session.add(admin)
            db.session.commit()


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    create_admin()
    app.run(debug=True, port=5001)

