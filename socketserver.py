###################################################################
# Socket Server
###################################################################
import SocketServer
import json
import blueid

# socket declaration
HOST, PORT = "192.168.0.102", 9999


class socketHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()


        # print "{} wrote:".format(self.client_address[0])
        # print self.data

        # get message and decode
        message = json.loads(self.data)
        command = message["command"]
        params = message["params"]
        username = params["username"]
        password = params["password"]

        db = blueid.CRUD()
        if command == "login":
            db.login(username,password)
        else: #todo add logout
            if command == "logout":
                db.logout("sessionkey")

        self.request.sendall(self.data.upper())


if __name__ == "__main__":
    # Create the server on localhost port 9999
    server = SocketServer.TCPServer((HOST, PORT), socketHandler)
    server.serve_forever()