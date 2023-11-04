
import os
import time
notesv = ["La cuenta del administrador del sistema."]
from miscelaneus import *
def notesMenu(usercount):
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
            return notesv
            os.system(command)

        else:
            os.system(command)
            print(colors.RED + "No existe ningun usuario con ese ID. ¿Ingresar la nota de vuelta?")
            print(colors.BLUE + "1: " + colors.GREEN + "Sí. " + colors.RED + "2: " + colors.GREEN + "No. >:)")
            option = input()
            if option == 1:
                notesMenu(usercount)
            else:
                os.system(command)
    except ValueError:
        print("El ID. Es un valor númerico. En 2 segundos volvera a empezar.")
        time.sleep(2)
        notesMenu(usercount)
