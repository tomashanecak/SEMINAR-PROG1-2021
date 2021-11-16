import os
from posixpath import join
path = os.path.dirname(__file__)


with open(os.path.join(path, "text.txt"), "r") as f:
    for row in f:
        stripped = row.strip()
        print(stripped)

with open(os.path.join(path, "novysubor.txt"), "w") as f:
    inp = str(input("ZADAJ VETU BUZIK!"))
    while inp != "":
        print(inp, file=f)
        inp = str(input("ZADAJ VETU BUZIK!"))



