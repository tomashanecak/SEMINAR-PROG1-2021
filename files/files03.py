import os 
path = os.path.dirname(__file__)


def LoadFile():
    name = str(input("Zadaj názov súboru: "))
    try:
        with open(os.path.join(path, name), "r") as file:
            for i, row in enumerate(file):
                row_list = row.split(" ")
                name = row_list[0]
                surname = row_list[1]

                id_number_list = list(row_list[2])
                id_number_pop = id_number_list[:-5]
                date_of_birth = list(reversed(id_number_pop))

                for j in range(len(date_of_birth) - 1):
                    if j % 2 == 0:
                        date_of_birth[j], date_of_birth[j+1] = date_of_birth[j+1], date_of_birth[j]
                
                date_of_birth.insert(2, ".")
                date_of_birth.insert(5, ".")

                if int(date_of_birth[3]) >= 5:
                    date_of_birth[3] = str(int(date_of_birth[3]) - 5)
                    

                if int(date_of_birth[6]) > 2:
                    date_of_birth.insert(6, "19")
                else:
                    date_of_birth.insert(6, "20")

                date_of_birth = "".join(date_of_birth)
                print(f"{i+1}. {surname} {name} {date_of_birth}")
    except FileNotFoundError:
        print("CHYBA-> Súbor sa nenašiel.")
        LoadFile()

LoadFile()



