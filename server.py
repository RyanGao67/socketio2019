from flask import Flask
from flask_restful import Api
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS


import sys
sys.path.append('/home/tgao/tgao2019/socketio2019')

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "secret"

api = Api(app)

socketio = SocketIO(app)
# @socketio.on('my event', namespace='/test')
# def handleMessage(msg):
#     print("Message:" +msg['data'])
#     socketio.emit("my response", msg['data'], namespace='/chat')

@app.route('/', methods=['GET', "POST"])
def handleMessage():
    print("Message:")
    socketio.emit("my response", 'dd', namespace='/chat')
    return 'te'

CORS(app, supports_credentials=True)
if __name__ == '__main__':
    from routes.api.reading import Reading
    api.add_resource(Reading, '/reading')

    socketio.run(app)
