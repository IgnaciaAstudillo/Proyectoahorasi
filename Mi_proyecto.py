#burscar regiones, regiones cod, comunas, comunas cod.

archivo = open("C:\\Users\eddie\OneDrive\Documentos\Archivos.txt\CasosPorComuna.csv.txt", "r")

lineas = archivo.readlines() #lee cada linea y las almacena en una lista, cada elemento de la lista es una linea
#print(lineas)
regiones = []
regionescod = []
comunas = []
comunascod = []

#ciclo que recorre cada elemento de la lista lineas
for linea in lineas:
    linea = linea.strip()                #borramos el salto de linea      
    #print(linea)                        #imprimimos la linea
    listalinea = linea.split(",")        #encerramos la linea en una lista
    #print(listalinea)                   #imprimimos la lista que corresponde a toda una linea con sus elementos separados

    for elemento in range(len(listalinea)):     #ciclo for que recorre el largo de la listalinea que contiene todos los elementos de una linea

        if elemento == 0 and listalinea[elemento] not in regiones:          #si el indice es igual a 0, o sea, si reconoce el primer elemento de la lista
            regiones.append(listalinea[elemento])                   #añadir a la lista regiones
        
        if elemento == 1 and listalinea[elemento] not in regionescod:       #si el indice es igual a 1
          regionescod.append(listalinea[elemento])                          #añadir a lista de código de regiones
        
        if elemento == 2:                                                   #si el indice es igual a 2
            comunas.append(listalinea[elemento])                    #añadir a lista de comunas
        
        if elemento == 3:                                                   #si el indice es igual a 3
            comunascod.append(listalinea[elemento])                         #añadir a lista de código de regiones
        
print(regiones, "\n")
print(regionescod, "\n")
print(comunas, "\n")
print(comunascod, "\n")

archivo.close()

print("-------------Bienvenido-------------")
print("-----Busque por nombre o código-----\n")
region = input("Ingrese la región que desea buscar: ")
print("\n")

while not ((region.lower() in regiones) or (region in regionescod)):            #verificar si la región está en la lista de regiones
    region = input("ERROR, ingrese región nuevamente: ")                        # o lista de códigos de regiones

comuna = input("Ingrese la comuna que desea buscar: ")                          
print("\n")                                                         

while not ((comuna.lower() in comunas) or (comuna in comunascod)):              #verificar si la región está en la lista de regiones
    comuna = input("ERROR, ingrese comuna nuevamene: ")                         # o lista de códigos de regiones
