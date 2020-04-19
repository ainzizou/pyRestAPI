from flask import Flask, jsonify, json, request
from Object.people import People

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello welcome!"


@app.route('/list')
def list():
    people = People()
    response = [ob.__dict__ for ob in people.getAll()]
    return jsonify({'response': response})


@app.route('/add', methods=['POST'])
def addPeople():
    person = People(request.json['name'], request.json['age'], request.json['gender'])
    people = People.addPeople(person)
    response = [ob.__dict__ for ob in people]
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run()
