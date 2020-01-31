import numpy as np
def rutasdisponibles():
    rutas=0
    while rutas < 1 or rutas > 2:
        print('Rutas Disponible: ')
        print('1. DBX-DEL')
        print('2. DBX-JFK')
        rutas = input('Elija una ruta:')
        if rutas.isdigit():
            rutas = int(rutas)
            if rutas < 1 or rutas > 2:
                print("¡Error!, ingrese una opción válida.")
        else:
            print("¡Error!, ingrese sólo números.")
            rutas = 0
    return rutas

def crearavion(modelo):
    archivo=open(modelo ,"r")
    fila = archivo.readline().strip().split("=")
    pri_clase = archivo.readline().strip().split("=")#ESTE COMENTARIO ES DE PRUEBA
    economico = archivo.readline().strip().split("=")
    cafeteria = archivo.readline().strip().split("=")
    banos = archivo.readline().strip().split("=")
    archivo.close()
    Matriz = np.zeros((int(fila[1]),(int(pri_clase[1])+int(economico[1])+int(cafeteria[1])+int(banos[1]))),int)
    Matriz[:,int(pri_clase[1])] = -2
    Matriz[:,int(pri_clase[1])+1] = -1
    n_ban=1
    contador=2
    eco = int(economico[1]) // int(cafeteria[1])
    while not (n_ban==int(banos[1])):
        if n_ban==int(banos[1])-1:
            Matriz[:,-1]=-1
        else:
            Matriz[:,int(pri_clase[1])+eco+contador+1] = -2
            Matriz[:, int(pri_clase[1])+eco+contador+2] = -1
        contador+=2
        n_ban+=1
        eco += int(economico[1]) // int(cafeteria[1])
    return Matriz

def cargarAvion(M, rutas):
    f = open(str(rutas) + ".txt", "r")
    f.readline()
    for linea in f:
        voca=['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        id, asiento, tipo, comida, categoria = linea.strip().split(",")
        var=voca.index(asiento[-1:].lower())
        colum = int(asiento[:-1]) - 1
        fila =int(var)
        if tipo == "Tercera Edad" or tipo == "Nino":
            M[fila, colum] = 5
        elif tipo == "Adulto":
            M[fila,colum] = 1
    return M

def imprimirmenu():
    print()
    print('+', '-' * 34, '+')
    print('|', '{:^34}'.format("EMIRANTES"), '|')
    print('+', '-' * 34, '+')
    print("1. Selecionar ruta")
    print("2. Cargar avion")
    print("3. Mostrar avion")
    print("4. Vender boletos")
    print("5. Check-in")
    print("6. Reportes")
    print("7. Salir")
    opcion = input("Elija una opción: ")
    opcion = int(opcion)

    return opcion
def mostrar_avion():
        fila = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        if M.shape[0] != 0:
            for x in range(M.shape[0]):
                print('%2s' % fila[x], end=" ")
                for j in range(M.shape[1]):
                    print('%2d' % M[x, j], end=' ')
                print()
        if M.shape[0] !=0:
            for x in range(M[0]):
                print('%2s' % fila[x], end=" ")
                for j in range(M[1]):
                    print('%2d' % M[x, j], end=' ')
                print()
# -- Programa Principal -- #
opcion = imprimirmenu()
if opcion > 1 or opcion < 7:
        while opcion != 7:
            if opcion == 1:
                rutas = 0
                while rutas != 3:
                    rutas = rutasdisponibles()
                    if rutas == 1:
                        M = crearavion('Boeign777.info')
                        print('\nSe ha cargado el avion Boeign777. ')
                    if rutas == 2:
                        M = crearavion('A380.info')
                        print('\n Se ha cargado el avion A380. ')
                    rutas=3
                opcion=imprimirmenu()
            elif opcion == 2:
                rutas = 0
                while rutas != 3:
                    rutas = rutasdisponibles()
                    if rutas == 1:
                        M = crearavion('Boeign777.info')
                        avion = cargarAvion(M, "DBX-DEL")
                        print("\nSe ha cargado el avión con los pasajeos de la ruta DBX-DEL.")
                        rutas=3
                    elif rutas == 2:
                        M = crearavion('A380.info')
                        avion = cargarAvion(M, "DBX-JFK")
                        print("Se ha cargado el avión con los pasajeos de la ruta DBX-JFK.")
                        rutas=3
                opcion = imprimirmenu()
            elif opcion==3:
                mostrar_avion()

elif opcion < 1 or opcion > 7:
    print("¡Error!, ingrese una opción válida.")
else:
    print("¡Error!, ingrese sólo números.")
