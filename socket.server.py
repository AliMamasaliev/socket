
import socket
import json

jj = {"ID": 000, "name": "BBB"}
data1 = json.dumps(jj)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 12345))
server.listen()

while True:
    user, adres = server.accept()

    print("connect")
    user.send(data1.encode("utf-8"))
