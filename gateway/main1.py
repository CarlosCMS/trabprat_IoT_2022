import socket

HOST = ''
PORT = 5555

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('Aguardando dados ...')
        while (1):
            message, address = s.recvfrom(8192)
            print(message)

if __name__ == "__main__":
    main()