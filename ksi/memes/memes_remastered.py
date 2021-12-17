import socket
import pynetstring
import base64
import tkinter as tk
from tkinter import *
import subprocess
import os
import re
import sys

path = os.path.dirname(__file__)
window = tk.Tk()


# -------------- Set Global Variables ------------------------------------
auth_token = ""
d_token = ""
data_channel_port = 0
meme_path = os.path.join(path, "meme.jpg")
msg_size = 0

# Encode meme as base64
encoded_meme = base64.b64encode(open(f"{meme_path}", "rb").read()).decode("ascii")

#__________________________SEND MEME FUNCTION TAKES CARE OF COMMUNICATION WITH REMOTE SERVER AND SENDING MEME _________________________
def sendMeme():
    # ------------------------------------- Get Values from Text Boxes -----------------------------------

    HOST = str(IP_ENTRY.get())  # The server'mains hostname or IP address
    PORT = int(PORT_ENTRY.get())       # The port used by the server

    nick = NICKNAME_ENTRY.get()
    password = PASSWORD_ENTRY.get()
    description = DESCRIPTION_ENTRY.get("1.0",'end-1c')
    isNSFW = "false" #todo !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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

# ----------------------- gui ---------------------------------------------

bg_color = "#424447"
window.title(string="--- MUNI MTP CLIENT ---")
window.geometry("800x500")
window.configure(bg=bg_color)
icon = tk.PhotoImage(file = os.path.join(path, 'icon.png'))
window.iconphoto(False, icon)

IP_LABEL = Label(window, text="IP Address: ", bd=8)
IP_LABEL.config(bg=bg_color)
IP_LABEL.place(x=50, y=50)
IP_ENTRY = Entry(window, bd=8)
IP_ENTRY.place(x=150, y=48)

PORT_LABEL = Label(window, text="Port: ")
PORT_LABEL.config(bg=bg_color)
PORT_LABEL.place(x=400, y=50)
PORT_ENTRY = Entry(window, bd=8)
PORT_ENTRY.place(x=450, y=48)

NICKNAME_LABEL = Label(window, text="Nickname: ")
NICKNAME_LABEL.config(bg=bg_color)
NICKNAME_LABEL.place(x=50, y=100)
NICKNAME_ENTRY = Entry(window, bd=8)
NICKNAME_ENTRY.place(x=150, y=98)

PASSWORD_LABEL = Label(window, text="Password: ")
PASSWORD_LABEL.config(bg=bg_color)
PASSWORD_LABEL.place(x=372, y=100)
PASSWORD_ENTRY = Entry(window, bd=8)
PASSWORD_ENTRY.place(x=450, y=98)

nsfw_state = IntVar()
nsfw_checkbox = Checkbutton(window, text="NSFW", variable=nsfw_state, background=bg_color).place(x=50,y=150)

DESCRIPTION_LABEL = Label(window, text="Description: ")
DESCRIPTION_LABEL.config(bg=bg_color)
DESCRIPTION_LABEL.place(x=50, y=270)

DESCRIPTION_ENTRY = tk.Text(window, height = 5, width = 85)
DESCRIPTION_ENTRY.place(x=50,y=300)

MEME_LABEL = Label(window, text="Meme: ")
MEME_LABEL.config(bg=bg_color)
MEME_LABEL.place(x=50, y=390)

BROWSEBTN = tk.Button(window, text ="Browse ", command = sendMeme)
BROWSEBTN.place(x=50,y=420)

SENDBTN = tk.Button(window, text ="Send MEME", command = sendMeme)
SENDBTN.place(x=660,y=420)

# #experimental 
class Redirect():
    
    def __init__(self, widget):
        self.widget = widget

    def write(self, text):
        self.widget.insert('end', text)
        #self.widget.see('end') # autoscroll

    #def flush(self):
    #    pass

terminal = tk.Text(window, height=5, width=85)
terminal.place(x=50,y=180)

# -----------------------------------------------------------------------

old_stdout = sys.stdout    
sys.stdout = Redirect(terminal)

window.mainloop()

sys.stdout = old_stdout