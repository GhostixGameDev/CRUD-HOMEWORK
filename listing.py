from miscelaneus import *
import os
import time

def userlist(length, users):
    if length>0:
        sizes=Sizes(length,users)
        totalsize = 0
        totalsize=sizes[0]+sizes[1]+sizes[2]+sizes[3]+6
        print(colors.GREEN + "2 " + colors.RED + ") " + colors.reset)
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
            for x in range(1, length+1):
                    autoSpacing(x,users,sizes)
        else:
            autoSpacing(1,users,sizes)
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
