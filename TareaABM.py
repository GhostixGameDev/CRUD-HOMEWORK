# -*- coding: utf-8 -*-
import os
import time

execution = 1
option = 0
error = 0
users = [["admin","admin","admin","admin","business@ghostix.com.ar","1234567890"]]
notesv = ["La cuenta del administrador del sistema."]

usercount = 0

from miscelaneus import *
from notes import *
from register import *
from listing import *


# ASCII art sheet: ╔ ╚ ╩ ╦ ╠ ═ ╬ ╣ ║ ╗ ╝ ═

while execution:
    error = 0
    mainMenu()
    option = input("Ingrese su opción. ")
    try:
        option = int(option)
    except ValueError:
        error = 1
        print("El valor debe ser un número de los listados. Porfavor vuelva a ingresarlo.")
        time.sleep(2)
    if error != 1:
        if option < 1 or option > 3:
            error = 1
            print("El valor debe ser un número de los listados. Porfavor vuelva a ingresarlo.")
    if error != 1:
        if option == 1:
            os.system(command)
            usercount=registerMenu(users, usercount)
        elif option == 2:
            os.system(command)
            userlist(usercount, users, usercount)
        elif option == 3:
            os.system(command)
            notesv=notesMenu(usercount)