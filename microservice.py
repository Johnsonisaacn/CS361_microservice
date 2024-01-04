import zmq
import winsound



context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    winsound.PlaySound('cardflip.wav', 0)
    returnmessage = "played"
    socket.send_string(returnmessage)