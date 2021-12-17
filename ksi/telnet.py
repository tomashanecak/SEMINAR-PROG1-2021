import socket
import sys
import re

def main():
    HOST, PORT = sys.argv[1], int(sys.argv[2])
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))

        flag = s.recv(1024).decode()
        print(flag)
        fg = ""
        while fg != "K":
            start = flag.find("e ") + len("e ") ; end = flag.find(",")
            numbers = flag[start:end]
            numbers = numbers.split(" + ")
            sum = str(int(numbers[0]) + int(numbers[1]))
            print(sum)
            s.sendall(sum.encode())
            flag = s.recv(1024).decode()
            print(flag)
            fg = flag[0]


        

if __name__ == '__main__':
    main()
