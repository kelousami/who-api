from flask import Flask
from flask_json import FlaskJSON, json_response

app = Flask(__name__)
json = FlaskJSON(app)

@app.route("/")
def hello():
    return "Helllo World!"

@app.route("/api/name")
def get_name():
    return json_response(name="who-api")

@app.route("/api/version")
def get_version():
    return json_response(version="0.0.1")

@app.route("/api/details")
def get_details():
    return json_response(name="who-api", version="0.0.1")

if __name__ == '__main__':
    app.run(debug=True)
