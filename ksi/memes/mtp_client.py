# ********************************************************************************************************
# AUTHOR: Tomáš Hanečák, Gymnázium Park mládeže 5, Košice :)
# Final Version Created 18.12.2021
# Check readme.txt to find more info about the APP
# Required Libraries installable via pip socket, pynetstring, base64, tkjnter, os, re
# Python 3.10 Compatible (Note: Please use python version 3.7 or higher to ensure the app works correctly)
# ********************************************************************************************************

import socket
import pynetstring
import base64
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfile
import os
import re

path = os.path.dirname(__file__)
window = tk.Tk()

# -------------- Set Global Variables ------------------------------------
auth_token = ""
d_token = ""
data_channel_port = 0
meme_path = ""
encoded_meme = ""
msg_size = 0
terminal_line = 0

## *********** Additional Functionality, display status messages from terminal in textarea in GUI ************
def terminalOutput(text, textarea, status = "normal"):
    global terminal_line
    terminal_line += 1

    textarea.tag_config("normal", background = "white")
    textarea.tag_config("success", background = "green")
    textarea.tag_config("warning", background = "orange")
    textarea.tag_config("error", background = "red")

    textarea.configure(state='normal')
    textarea.insert(tk.END, text)
    textarea.tag_add(status, f"{str(terminal_line)}.0", f"{str(terminal_line)}.{len(text)+1}")
    textarea.see(tk.END)
    textarea.configure(state='disabled')

    window.update()

#------------Browse for Meme File---------------
def memeBrowse():
    global meme_path, encoded_meme
    meme = askopenfile(mode = "r", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    meme_path = meme.name
    
    print(f"PATH TO MEME -> {meme_path} ")
    terminalOutput(f"PATH TO MEME -> {meme_path} \n", terminal)

    # Encode meme as base64
    encoded_meme = base64.b64encode(open(f"{meme_path}", "rb").read()).decode("ascii")


# __________________________ SEND MEME FUNCTION TAKES CARE OF COMMUNICATION WITH REMOTE SERVER AND SENDING MEME _________________________
def sendMeme():
    # Reset Message Size variable
    global msg_size
    msg_size = 0
    # ------------------------------------- Get Values from Text Boxes -----------------------------------

    try:
        HOST = str(IP_ENTRY.get())  # The server'mains hostname or IP address
        PORT = int(PORT_ENTRY.get())       # The port used by the server
    except ValueError:
        print("Check IP and PORT! Something is filled out incorrectly")
        terminalOutput("Check IP and PORT! Something is filled out incorrectly \n", terminal, "error")
        return 0

    nick = NICKNAME_ENTRY.get()
    password = PASSWORD_ENTRY.get()
    description = DESCRIPTION_ENTRY.get("1.0",'end-1c')

    if nsfw_state.get() == 0:
        isNSFW = "false"
    elif nsfw_state.get() == 1:
        isNSFW = "true"
    else:
        print("Internal Error With NSFW function, restart app")
        terminalOutput("Internal Error With NSFW function, restart app \n", terminal, "error")
        return 0

    # Check if everything is filled out (CORRECTLY!!) before establishing connection
    if len(encoded_meme) == 0:
        print("Please Select MEME")
        terminalOutput("Please Select MEME \n", terminal, "error")
        return 0
    
    if len(HOST) == 0:
        print("Please fill out IP Address")
        terminalOutput("Please fill out IP Address \n", terminal, "error")
        return 0

    if len(str(PORT)) == 0:
        print("Please fill out port")
        terminalOutput("Please fill out port \n", terminal, "error")
        return 0

    if len(nick) == 0:
        print("Please fill out your nickname")
        terminalOutput("Please fill out your nickname \n", terminal, "error")
        return 0

    if len(password) == 0:
        print("Please fill out your password")
        terminalOutput("Please fill out your password \n", terminal, "error")
        return 0

    if len(description) == 0:
        print("Please fill out description")
        terminalOutput("Please fill out description \n", terminal, "error")
        return 0

    # ------------------------------------------------------
    # Main Channel Communication
    # ------------------------------------------------------
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as mains:
        try:
            mains.connect((HOST, PORT))
        except:
            print("Cant Connect to server -> Check IP and PORT")
            terminalOutput("Cant Connect to server -> Check IP and PORT\n", terminal, "error")


        # Check If Server Responds
        mains.sendall(pynetstring.encode('C MTP V:1.0'))
        data = mains.recv(1024)

        if pynetstring.decode(data) != [b'S MTP V:1.0']:
            print("Server Not Alive -> Error 404")
            terminalOutput("Server Not Alive -> Error 404\n", terminal, "error")
        else:
            print('Server Alive Received ->', repr(data.decode()))
            terminalOutput(f"Server Alive Received -> {repr(data.decode())} \n", terminal, "success")

        
        # Get Auth Token
        mains.sendall(pynetstring.encode(f"C {nick}"))
        data = mains.recv(1024)
        auth_token = pynetstring.decode(data)

        if str(pynetstring.decode(data)) == "":
            print("Auth Token Not Received -> Auth Error")
            terminalOutput("Auth Token Not Received -> Auth Error\n", terminal, "error")
        else:
            print('Auth Token Generated ->', repr(data))
            terminalOutput(f"Auth Token Generated -> {repr(data)}\n", terminal, "success")

        
        # Get DataChannel Port
        data = mains.recv(1024)
        data_channel_port = int(str(pynetstring.decode(data))[4:10])
        if str(pynetstring.decode(data)) == "":
            print("Data Chanel Port NOT Received -> Server Error")
            terminalOutput("Data Chanel Port NOT Received -> Server Error\n", terminal, "error")
        else:
            print('Data Chanel Port Received ->', repr(data))
            terminalOutput(f"Data Chanel Port Received -> {repr(data)}\n", terminal, "success")

        
        #------------------------------------------------------------
        # Beggining of Data Channel communication
        #-----------------------------------------------------------
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as datas:
            try:
                datas.connect((HOST, data_channel_port))
            except:
                print("Can´t connect to Data Channel -> Internal Application Error")
                terminalOutput("Can´t connect to Data Channel -> Internal Application Error\n", terminal, "error")
            

            #Get Second Token
            datas.sendall(pynetstring.encode(f"C {nick}"))
            data = datas.recv(1024)
            print(data)
            
            if auth_token != pynetstring.decode(data):
                print("Auth Tokens not Equal Error!!!")
                terminalOutput("Auth Tokens not Equal Error!!!\n", terminal, "error")
                return 0
            else:
                print('--- Auth Token Validation Pass! ---', repr(data))
                print("-----------------------------------------------------------------------------")
                terminalOutput(f"--- Auth Token Validation Pass! --- {repr(data)}\n", terminal, "success")
                terminalOutput("-----------------------------------------------------------------------------\n", terminal)


            #Get data type from server
            def getDataType():
                data = datas.recv(1024)
                if len(data) == 0:
                    print('Data Type NOT Received -> Server Error')
                    terminalOutput('Data Type NOT Received -> Server Error\n', terminal, "error")
                    return 0
                else:
                    print('Data Type Received ->', repr(data))
                    terminalOutput(f'Data Type Received -> {repr(data)}\n', terminal, "success")

            # Get Received Packet size
            def getReceivedPacketSize(data):
                global msg_size
                start = data.find("ACK:") + len("ACK:") ; end = data.find("']")
                msg_size += int(data[start:end])

            def sendReceivePackets(data_to_send, type):
                datas.sendall(pynetstring.encode(f"C {data_to_send}"))
                data = str(pynetstring.decode(datas.recv(1024)))
                if len(data) == 0:
                    print('Server NOT Responding XO -> Server Error')
                    terminalOutput('Server NOT Responding XO -> Server Error\n', terminal, "error")
                    return 0
                else:
                    print(f'{type} type was sent with Server Response Message ->', repr(data))
                    terminalOutput(f'{type} type was sent with Server Response Message -> {repr(data)}\n', terminal, "success")
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
            if len(data) > 0:
                print('Data Secret Token Received ->', repr(data))
                terminalOutput(f'Data Secret Token Received -> {repr(data)}\n', terminal, "success")
                # Get Data Token from received message
                start = data.find("END:") + len("END:") ; end = data.find(",")
                d_token = data[start:end]

                datas.close
            else:
                print('Server NOT Responding XO -> Server Error')
                terminalOutput('Server NOT Responding XO -> Server Error\n', terminal, "error")
                return 0



        # Receive Data sent size for verification
        data = str(mains.recv(1024))
        if len(data) > 0:
            # Get size from received packet
            start = data.find("S ") + len("S ") ; end = data.find(",")
            s_calc_size = int(data[start:end])
            print(f'All Data Sent Size was -> {msg_size}', f"Server Calculated ->{repr(s_calc_size)}")
            terminalOutput(f'All Data Sent Size was -> {msg_size} Server Calculated ->{repr(s_calc_size)}\n', terminal)
            # Check Data sizes
            if s_calc_size == msg_size:
                print("Data Size Check Passed")
                terminalOutput("Data Size Check Passed\n", terminal, "success")
            else:
                print("WARNING Lost Packets !!!")
                terminalOutput("WARNING Lost Packets !!!\n", terminal, "warning")
                print("There was a problem sending your meme --- TERMINATING CONNECTION ---")
                terminalOutput("There was a problem sending your meme --- TERMINATING CONNECTION ---\n", terminal, "error")
                return 0
        else:
            print('Server NOT Responding XO -> Server Error')
            terminalOutput('Server NOT Responding XO -> Server Error\n', terminal, "error")
            return 0


        # Send Data Token to server to terminate connection
        mains.sendall(pynetstring.encode(f"C {d_token}"))

        # Check S ACK if session was terminated
        data = str(mains.recv(1024))
        if len(data) > 0:
            print(f"Message from server received stating -> {data}")
            print("--------------------------------------------------------------------------------")
            terminalOutput(f"Message from server received stating -> {data}\n", terminal, "success")
            terminalOutput("--------------------------------------------------------------------------------\n", terminal)
            if "S ACK" in data:
                print("Meme was Sent Succesfully --- CONNECTION TERMINATED BY SERVER ---")
                terminalOutput("Meme was Sent Succesfully --- CONNECTION TERMINATED BY SERVER ---\n", terminal, "success")
            else:
                print("There was a problem sending your meme --- TERMINATING CONNECTION ---")
                terminalOutput("There was a problem sending your meme --- TERMINATING CONNECTION ---\n", terminal, "error")
                mains.close()
        else:
            print('Server NOT Responding XO -> Server Error')
            terminalOutput('Server NOT Responding XO -> Server Error\n', terminal, "error")
            return 0
        
        terminalOutput("********************************************************************\n", terminal)

# ----------------------- gui ---------------------------------------------

bg_color = "#ebb434"
window.title(string="--- MUNI MTP CLIENT ---")
window.geometry("800x500")
window.configure(bg=bg_color)

try:
    icon = tk.PhotoImage(file = os.path.join(path, 'icon.png'))
    window.iconphoto(False, icon)
except:
    pass

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

BROWSEBTN = tk.Button(window, text ="Browse ", command = memeBrowse)
BROWSEBTN.place(x=50,y=420)

SENDBTN = tk.Button(window, text ="Send MEME", command = sendMeme)
SENDBTN.place(x=660,y=420)

terminal = tk.Text(window, height=5, width=85)
terminal.configure(state='disabled')
terminalOutput("INFO: \n", terminal)
terminal.place(x=50,y=180)

author = Label(window, text="Author -> TOMÁŠ HANEĆÁK", background=bg_color)
author.place(x=0, y=480)

# -----------------------------------------------------------------------
window.mainloop()

