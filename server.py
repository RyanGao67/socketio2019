from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS
from routes.api.reading import Reading

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "secret"

api = Api(app)
api.add_resource(Reading, '/reading')

socketio = SocketIO(app)
@socketio.on('my event', namespace='/test')
def handleMessage(msg):
    print("Message:" +msg)
    emit("my response", msg, namespace='/chat')

CORS(app, supports_credentials=True)
if __name__ == '__main__':
    socketio.run(app)
