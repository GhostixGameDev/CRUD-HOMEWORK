# -*- coding: utf-8 -*-
import os
import time

execution = 1
option = 0
error = 0
users = [["admin","admin","admin","admin","business@ghostix.com.ar","1234567890"]]


usercount = 0
notesv = ["La cuenta del administrador del sistema."]

command = "cls"  # Change to clear if you are using linux.


# ASCII art sheet: ╔ ╚ ╩ ╦ ╠ ═ ╬ ╣ ║ ╗ ╝ ═
class colors:
    RED = '\033[31m'
    reset = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


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


def registerMenu():
    os.system(command)
    print(colors.GREEN + "1 " + colors.RED + ") " + colors.reset + " Pantalla registración")
    global users
    global usercount
    aux=[]
    error = 0
    print("╔═══════════════════════════════════════════════════╗")
    print("║                                                   ║")
    print("║                                                   ║")
    print("║   ", end="")
    aux.append(input("Nombre de usuario. " + colors.YELLOW))
    for i in range(0, usercount+1):
        if users[i][0] == aux[0] and i != usercount+1:
            error = 1
    if error == 0:
        print(colors.reset + "║   ", end="")
        aux.append(input("Nombre real. " + colors.YELLOW))
        print(colors.reset + "║   ", end="")
        aux.append(input("Apellido. " + colors.YELLOW))
        print(colors.reset + "║   ", end="")
        aux.append(input("Número de DNI. " + colors.YELLOW))
        print(colors.reset + "║   ", end="")
        for i in range(0, usercount+1):
            if users[i][3] == aux[3] and i != usercount+1:
                error = 1
        if error == 0:
            aux.append(input("Email. " + colors.YELLOW))
            print(colors.reset + "║   ", end="")
            for i in range(0, usercount+1):
                if users[i][4] == aux[4] and i != usercount+1:
                    error = 1
            if error == 0:
                aux.append(input("Contraseña. " + colors.YELLOW))
                users.append(aux)
                print(colors.reset + "║                                                   ║")
                print("║                                                   ║")
                print("║                                                   ║")
                print("╚═══════════════════════════════════════════════════╝")
                usercount += 1
                time.sleep(3)
                os.system(command)
            else:
                print(colors.RED + "Email ya existente. Vuelva a empezar.", end=colors.reset)
                time.sleep(3)
                os.system(command)
                registerMenu()
        else:
            print(colors.RED + "Numero de DNI ya existente. Vuelva a empezar.", end=colors.reset)
            time.sleep(3)
            os.system(command)
            registerMenu()
    else:
        print(colors.RED + "Usuario ya existente. Vuelva a ingresarlo.", end=colors.reset)
        time.sleep(3)
        os.system(command)
        registerMenu()


def userlist(length, users):
    print(colors.GREEN + "2 " + colors.RED + ") " + colors.reset)
    if length > 0:
        sizes = [0, 0, 0, 0]
        totalsize = 0
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
            sizes[0] = len(users[0][0]) + len("usuario")
            sizes[1] = len(users[0][1]) + len("nombre")
            sizes[2] = len(users[0][2]) + len("apellido")
            sizes[3] = len(users[0][3]) + len("dni.")
        totalsize = sizes[0] + sizes[1] + sizes[2] + sizes[3] + 6
        print("╔", end="")
        for i in range(1, totalsize + 2):
            print("═", end="")
        print("╗")
        print("║", end="")
        for i in range(1, totalsize + 2):
            print(" ", end="")
        print("║")
        print("║", end="")
        for i in range(1, totalsize + 2):
            print(" ", end="")
        print("║")
        print("║", end="")
        for i in range(1, totalsize + 2):
            print(" ", end="")
        print("║")
        print("║   ", end="")
        print("Usuario", end="")
        for i in range(len("Usuario"), sizes[0] - 1):
            print(" ", end="")
        print(colors.BLUE + "| ", end=colors.reset)
        print("Nombre", end="")
        for i in range(len("Nombre"), sizes[1] - 1):
            print(" ", end="")
        print(colors.BLUE + "| ", end=colors.reset)
        print("Apellido", end="")
        for i in range(len("Apellido"), sizes[2] - 1):
            print(" ", end="")
        print(colors.BLUE + "| ", end=colors.reset)
        print("DNI.", end="")
        for i in range(len("DNI"), sizes[3] - 1):
            print(" ", end="")
        print(" ║")
        if length > 1:
            for x in range(1, usercount+1):
                    print("║   ", end="")
                    print(users[x][0], end="")
                    for i in range(len(users[x][0]), sizes[0] - 1):
                        print(" ", end="")
                    print(colors.BLUE + "| ", end=colors.reset)
                    print(users[x][1], end="")
                    for i in range(len(users[x][1]), sizes[1] - 1):
                        print(" ", end="")
                    print(colors.BLUE + "| ", end=colors.reset)
                    print(users[x][2], end="")
                    for i in range(len(users[x][2]), sizes[2] - 1):
                        print(" ", end="")
                    print(colors.BLUE + "| ", end=colors.reset)
                    print(colors.GREEN + users[x][3], end=colors.reset)
                    for i in range(len(users[x][3]), sizes[3] - 1):
                        print(" ", end="")
                    print("  ║")
        else:
            print("║   ", end="")
            print(users[1][0], end="")
            for i in range(len(users[1][0]), sizes[0] - 1):
                print(" ", end="")
            print(colors.BLUE + "| ", end=colors.reset)
            print(users[1][1], end="")
            for i in range(len(users[1][1]), sizes[1] - 1):
                print(" ", end="")
            print(colors.BLUE + "| ", end=colors.reset)
            print(users[1][2], end="")
            for i in range(len(users[1][2]), sizes[2] - 1):
                print(" ", end="")
            print(colors.BLUE + "| ", end=colors.reset)
            print(colors.GREEN + users[1][3], end=colors.reset)
            for i in range(len(users[1][3]), sizes[3] - 1):
                print(" ", end="")
            print("  ║")
        print("║", end="")
        for i in range(1, totalsize + 2):
            print(" ", end="")
        print("║")
        print("╚", end="")
        for i in range(1, totalsize + 2):
            print("═", end="")
        print("╝")
        time.sleep(5)
    else:
        print("Primero debe registrar al menos un usuario...")


def notes(usercount):
    global notesv
    os.system(command)
    id = 0
    option = 0
    print("╔═══════════════════════════════════════════════════╗")
    print("║                                                   ║")
    print("║                                                   ║")
    print("║    Agregar nota al usuario: ", end="")
    id = input(colors.YELLOW)
    try:
        if int(id) > 0 and int(id) <= usercount:
            print(colors.reset + "║                                                   ║")
            notesv.append(input("║    Nota: " + colors.YELLOW))
            print(colors.reset + "║                                                   ║")
            print("║                                                   ║")
            print("║                                                   ║")
            print("╚═══════════════════════════════════════════════════╝")
            time.sleep(3)
            os.system(command)

        else:
            os.system(command)
            print(colors.RED + "No existe ningun usuario con ese ID. ¿Ingresar la nota de vuelta?")
            print(colors.BLUE + "1: " + colors.GREEN + "Sí. " + colors.RED + "2: " + colors.GREEN + "No. >:)")
            option = input()
            if option == 1:
                notes(usercount)
            else:
                os.system(command)
    except ValueError:
        print("El ID. Es un valor númerico. En 2 segundos volvera a empezar.")
        time.sleep(2)
        notes(usercount)


while execution:
    error = 0
    mainMenu()
    option = input("Ingrese su opción. ")
    try:
        option = int(option)
    except ValueError:
        error = 1
        print("El valor debe ser un número de los listados. Porfavor vuelva a ingresarlo.")
    if error != 1:
        if option < 1 or option > 3:
            error = 1
            print("El valor debe ser un número de los listados. Porfavor vuelva a ingresarlo.")
    if error != 1:
        if option == 1:
            os.system(command)
            registerMenu()
        elif option == 2:
            os.system(command)
            userlist(usercount, users)
        elif option == 3:
            os.system(command)
            notes(usercount)