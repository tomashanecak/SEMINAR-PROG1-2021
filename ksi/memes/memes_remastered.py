import socket
import pynetstring
import base64
import tkinter as tk
import os
import re

window = tk.Tk()
window.title(string="--- MUNI MTP CLIENT ---")
window.geometry("800x500")
window.mainloop()

path = os.path.dirname(__file__)

HOST = '159.89.4.84'  # The server'mains hostname or IP address
PORT = 42069       # The port used by the server

auth_token = ""
d_token = ""
data_channel_port = 0
msg_size = 0

meme_path = os.path.join(path, "meme.jpg")
nick ="Hany"
password = "123456"
description = "Popis Memečka"
isNSFW = "false"

# Encode meme as base64
encoded_meme = base64.b64encode(open(f"{meme_path}", "rb").read()).decode("ascii")

# ------------------------------------------------------
# Main Channel Communication
# ------------------------------------------------------
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mains:
    mains.connect((HOST, PORT))


    # Check If Server Responds
    mains.sendall(pynetstring.encode('C MTP V:1.0'))
    data = mains.recv(1024)
    print('Server Alive Received ->', repr(data.decode()))

    if pynetstring.decode(data) != [b'S MTP V:1.0']:
        print("Server Not Alive -> Error 404")


    # Get Auth Token
    mains.sendall(pynetstring.encode(f"C <{nick}>"))
    data = mains.recv(1024)
    auth_token = pynetstring.decode(data)
    print('Auth Token Generated ->', repr(data))

    if str(pynetstring.decode(data)) == "":
        print("Auth Token Not Received -> Auth Error")
    

    # Get DataChannel Port
    data = mains.recv(1024)
    data_channel_port = int(str(pynetstring.decode(data))[4:10])
    print('Data Chanel Port Received ->', repr(data))
    
    #------------------------------------------------------------
    # Beggining of Data Channel communication
    #-----------------------------------------------------------
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as datas:
        datas.connect((HOST, data_channel_port))

        #Get Second Token
        datas.sendall(pynetstring.encode(f"C <{nick}>"))
        data = datas.recv(1024)
        
        if auth_token != pynetstring.decode(data):
            print("Auth Tokens not Equal Error!!!")
            exit()
        else:
            print('--- Auth Token Validation Pass! ---', repr(data))
            print("-----------------------------------------------------------------------------")


        #Get data type from server
        def getDataType():
            data = datas.recv(1024)
            print('Data Type Received ->', repr(data))

        # Get Received Packet size
        def getReceivedPacketSize(data):
            global msg_size
            start = data.find("ACK:") + len("ACK:") ; end = data.find("']")
            msg_size += int(data[start:end])

        def sendReceivePackets(data_to_send, type):
            datas.sendall(pynetstring.encode(f"C {data_to_send}"))
            data = str(pynetstring.decode(datas.recv(1024)))
            print(f'{type} was sent with Server Response Message ->', repr(data))
            getReceivedPacketSize(data)

        getDataType()

        # Send Meme to MUNI Server
        sendReceivePackets(encoded_meme, "Meme")

        getDataType()

        # Send Password to MUNI Server
        sendReceivePackets(password, "Password")

        getDataType()

        # Send Description to MUNI Server
        sendReceivePackets(description, "Description")

        getDataType()

        # Send isNSFW to MUNI Server
        sendReceivePackets(isNSFW, "isNSFW")

        # Receive Data Token
        data = str(datas.recv(1024))
        print('Data Secret Token Received ->', repr(data))
        # Get Data Token from received message
        start = data.find("END:") + len("END:") ; end = data.find(",")
        d_token = data[start:end]

        datas.close

    # Receive Data sent size for verification
    data = str(mains.recv(1024))
    # Get size from received packet
    start = data.find("S ") + len("S ") ; end = data.find(",")
    s_calc_size = int(data[start:end])
    print(f'All Data Sent Size was -> {msg_size}', f"Server Calculated ->{repr(s_calc_size)}")
    # Check Data sizes
    if s_calc_size == msg_size:
        print("Data Size Check Passed")
    else:
        print("Error 4 Lost Packets !!!")

    # Send Data Token to server to terminate connection
    mains.sendall(pynetstring.encode(f"C {d_token}"))

    # Check S ACK if session was terminated
    data = str(mains.recv(1024))
    print(f"Message from server received stating -> {data}")
    print("--------------------------------------------------------------------------------")
    if "S ACK" in data:
        print("Meme was Sent Succesfully --- CONNECTION TERMINATED BY SERVER ---")
    else:
        print("There was a problem sending your meme --- TERMINATING CONNECTION ---")
        mains.close()

