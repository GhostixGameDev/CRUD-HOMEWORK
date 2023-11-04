command="cls" # Change to clear if you are using linux.
import os
import time

def mainMenu():
    os.system(command)
    print("╔═══════════════════════════════════════════════════╗")
    print("║                                                   ║")
    print("║                                                   ║")
    print("║                1-Registración                     ║")
    print("║                2-Listado                          ║")
    print("║                3-Notas                            ║")
    print("║                                                   ║")
    print("║                                                   ║")
    print("╚═══════════════════════════════════════════════════╝")

class colors:
    RED = '\033[31m'
    reset = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

def Sizes(length,users):
        sizes = [0, 0, 0, 0]
        if length > 1:
            for i in range(0, length ):
                if len(users[i][0]) < len(users[i + 1][0]):
                    sizes[0] = len(users[i+1][0]) + len("usuario")
            for i in range(0, length ):
                if len(users[i][1]) < len(users[i + 1][1]):
                    sizes[1] = len(users[i+1][1]) + len("nombre")
            for i in range(0, length ):
                if len(users[i][2]) < len(users[i + 1][2]):
                    sizes[2] = len(users[i+1][2]) + len("apellido")
            for i in range(0, length):
                if len(users[i][3]) < len(users[i + 1][3]):
                    sizes[3] = len(users[i+1][3]) + len("dni.")
        else:
            sizes[0] = len(users[1][0]) + len("usuario")
            sizes[1] = len(users[1][1]) + len("nombre")
            sizes[2] = len(users[1][2]) + len("apellido")
            sizes[3] = len(users[1][3]) + len("dni.")
        return sizes

def autoSpacing(index,users,sizes):
    print("║   ", end="")
    print(users[index][0], end="")
    for i in range(len(users[index][0]), sizes[0] - 1):
        print(" ", end="")
    print(colors.BLUE + "| ", end=colors.reset)
    print(users[index][1], end="")
    for i in range(len(users[index][1]), sizes[1] - 1):
        print(" ", end="")
    print(colors.BLUE + "| ", end=colors.reset)
    print(users[index][2], end="")
    for i in range(len(users[index][2]), sizes[2] - 1):
        print(" ", end="")
    print(colors.BLUE + "| ", end=colors.reset)
    print(colors.GREEN + users[index][3], end=colors.reset)
    for i in range(len(users[index][3]), sizes[3] - 1):
        print(" ", end="")
    print("  ║")