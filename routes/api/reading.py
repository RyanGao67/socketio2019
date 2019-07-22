from flask_restful import Resource
from flask_socketio import SocketIO, send, emit
from  flaskweb20190721.server import socketio
class Reading(Resource):
    def get(self):
        msg = 'this is from reading'
        socketio.emit('test', msg)
