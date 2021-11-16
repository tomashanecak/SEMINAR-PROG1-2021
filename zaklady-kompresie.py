def compress(bin):
    count = 0

    if bin[0] == "1":
        compressed = "0"
        looking_for = "1"
    else:
        compressed = ""
        looking_for = "0"

    for digit in bin:
        if digit == looking_for:
            count += 1
        else:
            compressed += str(count)
            looking_for = digit
            count = 1

    compressed += str(count)
    return compressed 

print(compress("1111000110110"))









