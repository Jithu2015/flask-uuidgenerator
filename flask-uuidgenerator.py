from flask import Flask
from flask_uuid import FlaskUUID
import uuid
import json

#Initializing Flask app
app = Flask(__name__)
FlaskUUID(app)

#V1 version of UUID
@app.route('/uuid/1')
def uuidv1():
    v1=str(uuid.uuid1())
    return json.dumps(v1)

#v4 version of uuid
@app.route('/uuid/4')
def uuidv4():
    v4=str(uuid.uuid4())
    return json.dumps(v4)

#running flask app
if __name__ == '__main__':
    app.run()
