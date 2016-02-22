import socket

ADDRESS = "0.0.0.0"
PORT = 2222
CHUNK_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((ADDRESS, PORT))
s.listen(1)

try:
    while True:
        connection, client_address = s.accept()

        try:
            while True:
                data = connection.recv(CHUNK_SIZE)
                if not data:
                    break
                if "close" in data:
                    connection.close()
                    break
                connection.sendall(data)
        finally:
            connection.close()
finally:
    s.close()
