from miscelaneus import *
def modification(users,usercount):
    os.system(command)
    print(colors.GREEN + "1 " + colors.RED + ") " + colors.reset + " Pantalla modificación")
    aux=[]
    error = 0
    wich=0
    print("╔═══════════════════════════════════════════════════╗")
    print("║                                                   ║")
    print("║                                                   ║")
    print(colors.reset + "║   ", end="")
    try:
        wich=int(input("Ingrese el ID del usuario a modificar. "+colors.YELLOW))
    except ValueError:
        print(colors.RED+"EL ID DEBE SER NUMERICO."+colors.reset)
        error=1
    if error!=1 and wich>0 and wich<=usercount:
        print(colors.reset + "║   ", end="")
        aux.append(input("Nombre de usuario. " + colors.YELLOW))
        for i in range(0, usercount+1):
            if users[i][0] == aux[0] and i != wich:
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
                if users[i][3] == aux[3] and i != wich:
                    error = 1
            if error == 0:
                aux.append(input("Email. " + colors.YELLOW))
                print(colors.reset + "║   ", end="")
                for i in range(0, usercount+1):
                    if users[i][4] == aux[4] and i != wich:
                        error = 1
                if error == 0:
                    aux.append(input("Contraseña. " + colors.YELLOW))
                    users[wich]=aux
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
                    modification(users,usercount)
            else:
                print(colors.RED + "Numero de DNI ya existente. Vuelva a empezar.", end=colors.reset)
                time.sleep(3)
                os.system(command)
                modification(users,usercount)
        else:
            print(colors.RED + "Usuario ya existente. Vuelva a ingresarlo.", end=colors.reset)
            time.sleep(3)
            os.system(command)
            modification(users,usercount)
    else:
        print(colors.RED+"ID no existente. Vuelva a ingresarlo."+colors.reset)
        time.sleep(3)
        os.system(command)
        modification(users,usercount)