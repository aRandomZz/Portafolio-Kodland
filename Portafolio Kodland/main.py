# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
# Conectando SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Creando una base de datos
db = SQLAlchemy(app)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Título
    email = db.Column(db.String(40), nullable=False)
    text = db.Column(db.Text, nullable=False)

    # Salida del objeto y del id
    def __repr__(self):
        return f'<Card {self.id}>'


# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_discord=request.form.get('button_discord')
    button_python = request.form.get('button_python')
    button_db=request.form.get('button_db')
    button_html=request.form.get('button_html')
    return render_template('index.html', button_python=button_python, button_discord= button_discord, button_db=button_db, button_html=button_html)
@app.route('/feedback_create', methods=['GET', 'POST'])
def feedback_form():
    if request.method=='POST':
        email=request.form['email']
        text=request.form['text']
        feedback=Feedback(email=email, text=text)
        db.session.add(feedback)
        db.session.commit()
    return render_template('index.html')
    
@app.route('/secret')
def see_feedback():
    feed=Feedback.query.order_by(Feedback.email).all()
    return render_template('feed.html', feed=feed)


if __name__ == "__main__":
    app.run(debug=True)
