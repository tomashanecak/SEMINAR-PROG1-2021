from base64 import encodebytes
from Crypto.Cipher import DES
import os

path = os.path.dirname(__file__)
filepath=os.path.join(path,"prisonerDetails")

number = 0
for i in range(0,1000):
    number = f"{i:03}"
    digits = list(number)
    first = "0"+digits[0]
    second = "0"+digits[1]
    third = "0"+digits[2]

    hexadecimal_string = f"00f1{first}{second}{third}4b6172"
    key = bytes.fromhex(hexadecimal_string)

    # key = b'\x00\xf1\x01\x02\x03\x4b\x61\x72'

    des = DES.new(key, DES.MODE_ECB)

    with open(filepath, "rb") as file:
        lines = b""
        for line in file:
            lines += line

        newfile = open("decrypted_stuff.txt", "a")
    
        decrypted = des.decrypt(lines)
        print(decrypted)
        print(decrypted, file=newfile)
        # decrypted_text = ""
        # for value in decrypted:
        #     value = chr(value).upper()
        #     decrypted_text += value
        # print(decrypted_text, file=newfile)
        print(" ------------------ ", file=newfile)





