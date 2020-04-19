from flask import Flask, json
from Object.people import People

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello welcome!"

@app.route('/list')
def getAll():
    people = People()
    return json.dumps(people.getAll())


if __name__ == '__main__':
    app.run()
