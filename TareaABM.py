import os
import time

execution=1
option=0
error=0
users=["admin"]
realnames=["admin"]
lastnames=["admin"]
dninumber=["admin"]
passwords=["123456789"]
usercount=0

command="cls" #Change to clear if you are using linux.
#ASCII art sheet: ╔ ╚ ╩ ╦ ╠ ═ ╬ ╣ ║ ╗ ╝ ═
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
    print("║                                                   ║")
    print("║                                                   ║")
    print("╚═══════════════════════════════════════════════════╝")
def registerMenu():
    print(colors.GREEN+"1 "+colors.RED+") "+colors.reset+" Pantalla registración")
    global users
    global realnames
    global lastnames
    global dninumber
    global passwords
    global usercount
    usercount+=1

    print("╔═══════════════════════════════════════════════════╗")
    print("║                                                   ║")
    print("║                                                   ║")
    print("║   ",end="")
    users.append(input("Nombre de usuario. "+colors.YELLOW))
    print(colors.reset+"║   ",end="")
    realnames.append(input("Nombre real. "+colors.YELLOW))
    print(colors.reset+"║   ",end="")
    lastnames.append(input("Apellido. "+colors.YELLOW))
    print(colors.reset+"║   ",end="")
    dninumber.append(input("Número de DNI. "+colors.YELLOW))
    print(colors.reset+"║   ",end="")
    passwords.append(input("Contraseña. "+colors.YELLOW))
    print(colors.reset+"║                                                   ║")
    print("║                                                   ║")
    print("║                                                   ║")
    print("╚═══════════════════════════════════════════════════╝")
    time.sleep(3)
    os.system(command)
def list(length,users,realnames,lastnames,dninumber):
    print(colors.GREEN+"2 "+colors.RED+") "+colors.reset)
    if length>0:
        sizes=[0,0,0,0]
        totalsize=0
        if length>1:
            for i in range(1,length-1):
                if len(users[i])<len(users[i+1]):
                    sizes[0]=i+1
            for i in range(1,length-1):
                if len(realnames[i])<len(realnames[i+1]):
                    sizes[1]=i+1
            for i in range(1,length-1):
                if len(lastnames[i])<len(lastnames[i+1]):
                    sizes[2]=i+1
            for i in range(1,length-1):
                if len(dninumber[i])<len(dninumber[i+1]):
                    sizes[3]=i+1
        else:
            sizes[0]=len(users[1])+len("usuario")
            sizes[1]=len(realnames[1])+len("nombre")
            sizes[2]=len(lastnames[1])+len("apellido")
            sizes[3]=len(dninumber[1])+len("dni.")
        totalsize=sizes[0]+sizes[1]+sizes[2]+sizes[3]+6
        print("╔",end="")
        for i in range(1,totalsize+2):
            print("═",end="")
        print("╗")
        print("║",end="")
        for i in range(1,totalsize+2):
            print(" ",end="")
        print("║")
        print("║", end="")
        for i in range(1, totalsize + 2):
            print(" ", end="")
        print("║")
        print("║",end="")
        for i in range(1,totalsize+2):
            print(" ",end="")
        print("║")
        print("║   ",end="")
        print("Usuario",end="")
        for i in range(len("Usuario"),sizes[0]-1):
            print(" ",end="")
        print(colors.BLUE+"| ", end=colors.reset)
        print("Nombre",end="")
        for i in range(len("Nombre"),sizes[1]-1):
            print(" ",end="")
        print(colors.BLUE+"| ", end=colors.reset)
        print("Apellido",end="")
        for i in range(len("Apellido"),sizes[2]-1):
            print(" ",end="")
        print(colors.BLUE+"| ", end=colors.reset)
        print("DNI.",end="")
        for i in range(len("DNI"),sizes[3]-1):
            print(" ",end="")
        print(" ║")
        if length>1:
            for x in range(1,usercount):
                print("║   ",end="")
                print(users[x], end="")
                for i in range(len(users[x]), sizes[0] - 1):
                    print(" ", end="")
                print(colors.BLUE+"| ", end=colors.reset)
                print(realnames[x], end="")
                for i in range(len(realnames[x]), sizes[1] - 1):
                    print(" ", end="")
                print(colors.BLUE+"| ", end=colors.reset)
                print(lastnames[x], end="")
                for i in range(len(lastnames[x]), sizes[2] - 1):
                    print(" ", end="")
                print(colors.BLUE+"| ", end=colors.reset)
                print(colors.GREEN+dninumber[x], end=colors.reset)
                for i in range(len(dninumber[x]), sizes[3] - 1):
                    print(" ", end="")
                print("  ║")
        else:
            print("║   ", end="")
            print(users[1], end="")
            for i in range(len(users[1]), sizes[0] - 1):
                print(" ", end="")
            print(colors.BLUE+"| ", end=colors.reset)
            print(realnames[1], end="")
            for i in range(len(realnames[1]), sizes[1] - 1):
                print(" ", end="")
            print(colors.BLUE+"| ", end=colors.reset)
            print(lastnames[1], end="")
            for i in range(len(lastnames[1]), sizes[2] - 1):
                print(" ", end="")
            print(colors.BLUE+"| ", end=colors.reset)
            print(colors.GREEN+dninumber[1], end=colors.reset)
            for i in range(len(dninumber[1]), sizes[3] - 1):
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



while execution:
    error=0
    mainMenu()
    option=input("Ingrese su opción. ")
    try:
        option=int(option)
    except ValueError:
        error=1
        print("El valor debe ser un número de los listados. Porfavor vuelva a ingresarlo.")
    if error!=1 and option<1 or option>2:
        error=1
        print("El valor debe ser un número de los listados. Porfavor vuelva a ingresarlo.")
    if error!=1:
        if option==1:
            os.system(command)
            registerMenu()
        elif option==2:
            os.system(command)
            list(usercount,users,realnames, lastnames, dninumber)
