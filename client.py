import socket

def send_data_to_server(data, host='127.0.0.1', port=8080):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(data.encode())
        response = s.recv(1024)
        print('Received from server:', response.decode())

if __name__ == "__main__":
    send_data_to_server("Hello, Server!")