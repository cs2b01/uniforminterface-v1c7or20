from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import json

db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def users():
    db_session = db.getSession(engine)
    users = db_session.query(entities.Usuario)
    data = users[:]
    return Response(json.dumps(data, cls=connector.AlchemyEncoder), mimetype = 'application/json')

@app.route('/create_user', methods = ['GET'])
def create_test_books():
    db_session = db.getSession(engine)
    newuser = entities.Usuario(codigo=201810741, nombre="Juan", apellido="Ramirez",password="12345")
    db_session.add(newuser)
    db_session.commit()
    return "New user created!"

if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('0.0.0.0'))
