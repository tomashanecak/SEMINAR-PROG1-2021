## Vstupuje číslo, zoraď jeho cifry od najmänšej po najväčšiu

num = int(input("Zadaj číslo: "))

num_list = list(str(num))
num_list.sort()
print("".join(num_list))
