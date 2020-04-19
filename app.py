from flask import Flask, jsonify, json, request
from Object.people import People

app = Flask(__name__)

persons = []


@app.route('/')
def hello_world():
    return "Hello welcome!"


@app.route('/list')
def list():
    # people = People()
    return jsonify({'response': persons})


@app.route('/add', methods=['POST'])
def addPeople():
    # person = {'name': request.json['name'], 'age': request.json['age'], 'gender': request.json['gender']}
    person = People(request.json['name'], request.json['age'], request.json['gender'])
    persons.append(person)
    return jsonify({'response': [ob.__dict__ for ob in persons]})

if __name__ == '__main__':
    app.run()
