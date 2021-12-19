import socket
import sys
import re


HOST, PORT = "telnet.iamroot.eu", int(44553)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))

    data = s.recv(1024)
    print(data)

        # flag = s.recv(1024).decode()
        # print(flag)
        # fg = ""
        # while fg != "K":
        #     start = flag.find("e ") + len("e ") ; end = flag.find(",")
        #     numbers = flag[start:end]
        #     numbers = numbers.split(" + ")
        #     sum = str(int(numbers[0]) + int(numbers[1]))
        #     print(sum)
        #     s.sendall(sum.encode())
        #     flag = s.recv(1024).decode()
        #     print(flag)
        #     fg = flag[0]
