import socket
import sys
import os

class Server(object):

    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1
    directory_path = os.path.dirname(os.path.abspath(__file__))
    response = []

    def __init__(self, host='', port=8000):
        self.HOST = host
        self.PORT = port
        # Create socket
        self.listen_socket = listen_socket = socket.socket(
            self.address_family,
            self.socket_type
        )
        self.listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_socket.bind((self.HOST, self.PORT))
        self.listen_socket.listen(self.request_queue_size)

        self.headers = """\
        HTTP/1.1 200 OK\n
        Content-Type: text/html

        """
        print('Serving HTTP on port {}'.format(self.PORT))

    def serve_forever(self):
        while 1:
            connection, adress = self.listen_socket.accept()
            request_headers = connection.recv(1024)
            request = request_headers.decode().split('\n\r')[0].split('\r')[0]
            for index in 'index.html', 'index.htm':
                index_path = os.path.join(directory_path, index)
                if os.path.exists(index_path):
                    response = 


            response = self.handle_request(request)

            connection.sendall(response.encode())
            connection.close()

    def handle_request(self, request):
        pass
        




    

if __name__ == '__main__':
    # Determine the port number
    if len(sys.argv) > 1:
        HOST, PORT = '', sys.argv[1]
    else:
        HOST, PORT = '', 8000
    # Create server instanse
    server = Server(HOST, PORT)
    server.serve_forever()
