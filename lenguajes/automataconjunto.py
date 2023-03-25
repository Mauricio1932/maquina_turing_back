#El siguiente programa necesita un parametro para poder ser ejecutado
#El parametro es la direccion del documento dodne se encuentra el automata
#Ejemplo de ejecucion:
#  python3 afnd.py data.txt


import sys 
import json, os

#abrimos el documento dodne se encuentran los datos del automata

tm = os.path.join('turing','automataconjunto.tm')

class automataconjunto():
    def automata(valor):
        with open(tm) as f:
            lineas = f.readlines()

        i=0
        lista = []
        #Se limpia el texto donde se encuentran los datos del automata para crear listas donde podemos manejar los datos 
        #esto con la finalidad de poder manejar mas facil la informacion 
        while i < len(lineas):
                # se remplazan valores para limpiar el texto
                lin = lineas[i].replace("=", "")
                lin = lin.replace("  ", "+")
                lin = lin.replace("\n", "")
                lin = lin.replace("[", "")
                lin = lin.replace("]", "")
                lista.append(lin.split("+"))
                
                i = i + 1
                

        #una vez limpio el texto se crean las variables de tipo lista que usara el sistema
        #variable de estados
        q = lista[0][1].split("-")
        #variable del alfabeto
        s = lista[1][1].split("-")
        #aqui se agrega epsilon, si el epsilon lo agregan al alfabeto hay que comentar esta linea 
        #s.append('e')
        #variable de estado incial
        q0 = lista[2][1].split("-")
        #variable de estados finales 
        f = lista[3][1].split("-")
        #aplicamos un segundo filtro para obtener los estados de transicion
        aux = lista[4][1]
        r = aux[1:len(aux)-1].split(")-(")
        #creamos nuestra lista donde estan los estados de transicion
        estados = []
        i=0
        while i < len(r):
            estados.append(r[i].split("-"))
            i = i + 1
        #se termina de crear la lista de estados de transicion

        cadena1 = valor

        cadena = cadena1
        cadena = list(cadena)
        
        #INICIO DE AFND
        valoresusados = " "
        estado_final = False
        #al ser un afnd estte puede tomar multiples caminos por lo cual esta lista sirve para analizar dichos caminos
        estados_actuales = []
        #el primer elemento a analizar sera el estado inicial
        estados_actuales.append(q0[0])
        while cadena:
            #con los elementos de la cadena ingresada buuscamoss que dicha transicion exista en el alfabeto 
            if(cadena[0] in s):
                num_estados = len(estados_actuales)
                for i in range(len(estados)):    
                    for j in range(num_estados):
                        #buscamos que los posibles caminos tengan una trancision si estos la tienen agregan un elementto a la lista de estados actuales para su posterior analisis
                        if estados[i][0] == estados_actuales[j] and estados[i][1] == cadena[0]:
                            #actualziamos los estados actuales
                            estados_actuales.append(estados[i][2])
                            #print(estados_actuales[j])
                for y in range(num_estados):
                    #una vez analizados todos los estados posibles los removemos
                    estados_actuales.remove(estados_actuales[0])
                #print(estados_actuales)
                valoresusados = valoresusados + cadena[0]
                cadena.remove(cadena[0])
            else:
                print("Un estado en la cadena no es valido")
                print("No valido: "+cadena[0])
                cadena.remove(cadena[0])
                

        for i in range(len(estados_actuales)):
            #si los ultimos estados encontrados son parte de los estados finales consideramos que es una cadena valida 
            if(estados_actuales[i] in f):
                #si la cadena es valida marcamos como true de lo contrario es un false
                estado_final = True
                break
            else:
                estado_final = False

        #imprimimmos si la cadena es valida o no
        if estado_final == True:
            resultado = valoresusados.replace(" ","")
            return resultado
        else:
                nosirve = "cadena no valida"
                return nosirve
                

