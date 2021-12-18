import ctypes

# zdroj: https://stackoverflow.com/q/36760127/1047788
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def main():
    print("\x1B[31mCervena", end='')
    print("\x1B[0m", end='')
    print(", ", end='')
    print("\x1B[34mmodra", end='\n')
    print("\x1B[0m", end='')
    
    print("pro \x1B7blazna dobra!", end='')
    print("\x1B8 soba \x1B[B", end='\n')
    
    print()
    input("Press Enter to continue...")

if __name__ == '__main__':
    main()