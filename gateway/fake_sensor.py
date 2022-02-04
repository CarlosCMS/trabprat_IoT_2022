import socket
import random

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
    msg = "179581.18296, 1, -22.899715, {},  19.0, 3,  -0.192,  0.086,  9.898, 6,  4290201.922,-4018758.449,-2466499.854, 7,  0.048,-0.045, 0.157, 8, 1629073159310, 86, 26".format(random.random())
    sock.sendto(msg.encode(), ("127.0.0.1", 5555))