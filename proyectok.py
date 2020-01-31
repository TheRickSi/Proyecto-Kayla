import numpy as np
import random as rd
dicRutas ={('Guayaquil','GYE'):[('Quito','UIO'),('Barcelona','BCN'),('Bogota','BOG'),('Panama','PTY'),('Quito','UIO'),('Madrid','MAD'),('Lima','LIM'),('Amsterdam','AMS'),('Cancun','CUN')],('Quito','UIO'):[('Miami','MIA'),('Cuenca','CUE'),('Manta','MEC'),('Barcelona','BCN'),('Bogota','BOG'),('Panama','PTY'),('Salvador','SAL'),('Lima','LIM'),('Amsterdam','AMS'),('Guayaquil','GYE')],('Manta','MEC'):[('Quito','UIO')],('Cuenca','CUE'):[('Quito','UIO')]}
voca=['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i']
def abrirArch():
    f=open("rutas.txt","r")
    f.readline()
    arch=f.readlines()
    dic={}
    for linea in arch:
        lin=linea.replace("\n","").split(",")
        codigoruta=lin[0]
        avion=lin[1]
        dic[codigoruta]=avion
    f.close()
    return dic



def presentarMenu():
    print(''''+---------------------------------------+
| EMIRATES |
+---------------------------------------+
1. Seleccionar Ruta
2. Cargar Avión
3. Mostrar Avión
4. Vender Boletos
5. Modificar Pasajero
6. Reporte y grafico Comida
7. Salir''')

def validaciones(ciudades,tipo):#Presenta las opciones y valida que se escoja una opcion disponible
    conta = 0
    while conta < len(ciudades):
        print(conta + 1, ". ", ciudades[conta][0])
        conta += 1
    ciudad = input("Ingrese la ciudad de "+tipo+": ")
    if not ciudad.isdigit():
        ciudad = 0
    while not (1 <= int(ciudad) <= len(ciudades)):
        ciudad = input("Ingrese una ciudad valida\nIngrese la ciudad de "+tipo+": ")
    ciudad = int(ciudad) - 1
    return ciudad

def obtenerDestinos(ciudad, dicRutas): #Esta funcion era innecesaria pero esta en el pdf
    ciudades=list(dicRutas.keys())
    for i in ciudades:
        if ciudad == i[0]:
            valor=ciudades.index(i)
    destinos=list(dicRutas[ciudades[valor]])
    ciudadestino=validaciones(destinos,"Llegada")
    return ciudadestino,destinos


def crearavion(modelo):
    archivo=open(modelo ,"r")
    fila = archivo.readline().strip().split("=")
    pri_clase = archivo.readline().strip().split("=")
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
    archivo.close()
    return Matriz

def cargarAvion(M, rutas):
    f = open(str(rutas) + ".txt", "r")
    f.readline()
    for linea in f:
        voca=['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j']
        id, asiento, tipo, comida, categoria = linea.strip().split(",")
        var=voca.index(asiento[-1:].lower())
        colum = int(asiento[:-1]) - 1
        fila =int(var)
        if tipo == "Tercera Edad" or tipo == "Nino":
            M[fila, colum] = 5
        elif tipo == "Adulto":
            M[fila,colum] = 1
    return M

def mostrar_avion(M):
    fila = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    if M.shape[0] != 0:
        for x in range(M.shape[0]):
            print('%2s' % fila[x], end=" ")
            for j in range(M.shape[1]):
                print('%2d' % M[x, j], end=' ')
            print()

def obtenerprimeraclase(modelo):
    archivo = open(modelo, "r")
    fila = archivo.readline().strip().split("=")
    pri_clase = int(archivo.readline().strip().split("="))
    archivo.close()
    return pri_clase


#---------MENU PRINCIPAL-------------#
opci=1
flag=[1,0,0,0,0,0] #Esta matriz permite que no se pueda seleccionar una opcion antes de tiempo o dos veces
while opci !=7 and opci <=6 and opci >=1:
    presentarMenu()
    opci=input("Ingrese una opcion:")
    while not opci.isdigit():
        print("Ingrese una opcion valida.")
        presentarMenu()
        opci=input("Ingrese una opcion: ")
    opci=int(opci)
    if opci==1 and flag[0]==1:
        ciudadorigen=list(dicRutas.keys())
        ciudad1=validaciones(ciudadorigen,"Salida")
        ciudad2,ciudadestino=obtenerDestinos(ciudadorigen[ciudad1][0],dicRutas)
        codigoruta=ciudadorigen[ciudad1][1]+"-"+ciudadestino[ciudad2][1] #Crea el codigo en formato "Ciudadorigen-ciudaddestino"
        dicio=abrirArch()
        avion=dicio[codigoruta]+".info"
        flag[0]=0
        flag[1]=1
    elif flag[0]==0 and opci==1:
        print("=================== LA RUTA YA A SIDO SELECCIONADA ===================")
    if opci==2 and flag[1]==1:
        mavion = crearavion(avion)
        mavion=cargarAvion(mavion,codigoruta)
        pasajeros={}
        flag[3]=1
        flag[1]=0
        flag[2]=1
        print("================================ AVION CARGADO CORRECTAMENTE ======================")
    elif opci==2 and flag[1]==0:
        if flag[0]==1:
            print("================ PORFAVOR SELECCIONE LA RUTA ANTES DE CARGAR EL AVION ================")
        else:
            print("=============== EL AVION YA ESTA CARGADO ===========")
    if opci==3 and flag[2]==1:
        print("\n\n\n")
        mostrar_avion(mavion)
        print("\n\n\n")
    elif opci==3 and flag[2]==0:
        print("======================== OPCION NO DISPONIBLE =================")
    if opci==4 and flag[3]==1:
        cantidadCompra=input("¿Cuantos boletos desea comprar?")
        if not cantidadCompra.isdigit():
            cantidadCompra = 0
        else:
            cantidadCompra=int(cantidadCompra)
        while not int(cantidadCompra)>0 or int(cantidadCompra)>9:
            if cantidadCompra>9:
                print("Solo pueden efectuarse 9 compras por transaccion")
            cantidadCompra = input("Ingrese una cantidad valida: ")
            if not cantidadCompra.isdigit():
                cantidadCompra = 0
        print()
        print("Escoja la seccion: ")
        print("1. Primera Clase\n2. Clase Economica\n")
        clase=input("Ingrese una opcion : ")
        if not clase.isdigit():
            clase = 0
        else:
            clase=int(clase)
        while not 1<=clase<=2:
            clase=input("Ingrese una opcion valida: ")
            if not clase.isdigit():
                clase = 0
        tuplaavion=mavion.shape
        comprobante=True
        primeraclase=obtenerprimeraclase(avion)
        while comprobante:
            if clase==1:
                avioncolum = rd.randint(0, primeraclase-1)
            else:
                avioncolum = rd.randint(primeraclase+2, tuplaavion[1] - 1)
            avionfila = rd.randint(0, tuplaavion[0] - 1)
            asientos = []
            conta = 1
            while conta <= cantidadCompra:
                if not mavion[avionfila][avioncolum] == 0:
                    comprobante = False
                asientos.append((avionfila, avioncolum))
                if avionfila == int(tuplaavion[0] - 1):
                    avioncolum+=1
                    avionfila=0
                else:
                    avionfila+=1
                conta+=1
            if comprobante:
                comprobante=False
            else:
                comprobante=True
                asientos=[]
        print("Los asientos designados son:")
        for asiento in asientos:
            f = voca[asiento[0]].upper()
            asientonumerado=str(asiento[1]+1)+f
            print(asientonumerado,end=" ")
        print()
        conta=1
        while conta <=cantidadCompra:
            print("Ingrese los datos del pasajero ",conta+1," :")
            id=input("ID: ")
            fecha=input("Fecha de Nacimiento(dd/mm/aaa): ")
            print('''Tipo de Comida:
                    1. Normal
                    2. Vegetariana
                    3. Vegana
                    4. Gluten Free''')




