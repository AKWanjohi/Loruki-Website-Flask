from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/loruki'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Contact(db.Model):
    __tablename__ = 'contact'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    company = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)

    def __init__(self, name, company, email):
        self.name = name
        self.company = company
        self.email = email


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/features')
def features():
    return render_template('features.html')


@app.route('/docs')
def docs():
    return render_template('docs.html')


@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        company = request.form['company']
        email = request.form['email']
        if db.session.query(Contact).filter(contact.email == email).count() == 0:
            data = Contact(name, company, email)
            db.session.add(data)
            db.session.commit()
            return render_template('contact.html')
        return render_template('index.html', message='You have already requested to be contacted.')


if __name__ == '__main__':
    app.debug = True
    app.run()
