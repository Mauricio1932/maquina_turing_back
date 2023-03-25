from lenguajes.serializers import PostSerializer
from lenguajes.models import Conjunto
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import re
from lenguajes.maquina import TuringMachine
from lenguajes.gramatica import conjuntosal
from lenguajes.automataconjunto import automataconjunto
from lenguajes.generarfaloso import generafalso
from lenguajes.automataparticiones import automataparticiones
import os

tm = TuringMachine.parse(os.path.join('turing', 'transicion.tm'))


# valores de mapeo para lasparticiones 
matriz_uno = [["A"]]

matriz_dos = [["B"],
            ["C"]]

matriz_tres = [["D"],
               ["E"],
               ["F"],
               ["G"],
               ["H"]]

matriz_cuatro = [["I"],
                 ["J"],
                 ["K"],
                 ["Z"],
                 ["M"],
                 ["N"],
                 ["O"],
                 ["P"],
                 ["Q"],
                 ["T"],
                 ["U"],
                 ["V"],
                 ["W"],
                 ["X"],
                 ["Y"]]

# arreglos usados
cadena = []
particionesmal = []
arregloparticion = []
entradaparti = []



def personalisado(conjunto):
    ingresado = automataconjunto.automata(conjunto)
    if ingresado == "cadena no valida":
        mensaje = "ingrese de nuevo el conjunto"
        return mensaje
    else:
        crearparticiones(ingresado)
        parti()


def aletorio():
    conju = ""
    conju = conjuntosal.conjunto()
    crearparticiones(conju)
    parti()


def crearparticiones(entrada):
    cadena.clear()
    i = 0
    while i < len(entrada):
        # se remplazan valores para limpiar el texto
        lin = entrada
        lin = lin.replace("{", "")
        lin = lin.replace(",", "")
        lin = lin.replace("}", "")
        # print(lista[i])
        i = i + 1
    for i in range(len(lin)):
        for j in lin:
            for x in j:
                cadena.append(x)

    if len(lin) == 1:
        dato = limpiarvalores(matriz_uno[0])
        data = tm.accepts(dato)
        data = str(data)
        particiones(data)

    if len(lin) == 2:
        for i in range(len(matriz_dos)):
            dato = limpiarvalores(matriz_dos[i])
            data = tm.accepts(dato)
            data = str(data)
            particiones(data)

    if len(lin) == 3:
        for i in range(len(matriz_tres)):
            dato = limpiarvalores(matriz_tres[i])
            data = tm.accepts(dato)
            data = str(data)
            particiones(data)

    if len(lin) == 4:
        for i in range(len(matriz_cuatro)):
            dato = limpiarvalores(matriz_cuatro[i])
            data = tm.accepts(dato)
            data = str(data)
            particiones(data)

# limpiesa de valores 
def limpiarvalores(entrada):
    i = 0
    parseo = str(entrada)
    while i < len(parseo):
        # se remplazan valores para limpiar el texto
        lin = parseo
        lin = lin.replace("[", "")
        lin = lin.replace(",", "")
        lin = lin.replace("]", "")
        lin = lin.replace("'", "")
        lin = lin.replace("'", "")
        # print(lista[i])
        i = i + 1

    lin = lin.replace(" ", "")

    return lin

# particiones guardadas de la maquina
def particiones(val):
    i = 0
    parseo = val
    while i < len(parseo):
        # se remplazan valores para limpiar el texto
        lin = parseo
        lin = lin.replace("[", "")
        lin = lin.replace("]", "")
        lin = lin.replace("'", "")
        lin = lin.replace("'", "")
        lin = lin.replace("q2:", "")
        lin = lin.replace("#", "")

        # print(lista[i])
        i = i + 1

    cont = ""
    for j in lin:

        if j == "{":
            cont += j
        elif j == "0" or j == "1" or j == "2" or j == "3":
            val = int(j)
            cont += cadena[val]
        elif j == ",":
            cont += j
        elif j == "}":
            cont += j

    arregloparticion.append(cont)


def parti():
    for i in range(len(arregloparticion)):
        print(arregloparticion[i])


def generarerroneos():
    for i in range(3):
        conjuntomal = generafalso.generarfalsos()
        particionesmal.append(conjuntomal)

# maquina respuesta de particiones
# devuelve las particiones del conjunto añadido

#Metodo get
class GetParticiones(APIView):
    def get(self, response):
        res = {
            "verdadero": arregloparticion[0],
            "falso": particionesmal
        }

        return Response(res, status=status.HTTP_200_OK)

#Metodod get
class GetConjunto(APIView):
    def get(self, response):
        particionesmal.clear()
        arregloparticion.clear()
        aletorio()
        generarerroneos()
        conjunto1 = arregloparticion[0]

        return Response(conjunto1, status=status.HTTP_200_OK)

#variale para guardar respuesta del usuario
aut_conjunto = ""

#Metodo POST 
class PostConjunto(APIView):
    def post(self, request):
        aut_conjunto = request.data['conjuntos']
        arregloparticion.clear()
        mensaj = personalisado(aut_conjunto)
        return Response(arregloparticion, status=status.HTTP_200_OK)

#Metodo POST 
class PostParticiones(APIView):
    def post(self, request):
        particionadd = ""
        entradaparti.clear()
        particionadd = request.data['particion']
        elbueno = str(particionadd)
        value = elbueno.split(" ")

        for i in range(len(value)):
            entradaparti.append(value[i])

        for i in range(len(entradaparti)):
            respues = automataparticiones.automata(entradaparti[i])
            if respues == "cadena no valida":
                mensajeaviso = "Escribe bien tu respuesta"
                mensaj = str(mensajeaviso)
                return Response(mensaj, status=status.HTTP_200_OK)

            else:
                if respues in arregloparticion:
                    print("las particiones estan corretas", respues)
                    mensajeexito = "excelente todas estan correctas"
                    mensa = str(mensajeexito)

                else:
                    valor = respues
                    print("incorrecto", valor)
                    mensajeerror = "una de las particiones esta mal"
                    men = str(mensajeerror)
                    return Response(mensajeerror, status=status.HTTP_200_OK)

        return Response(mensa, status=status.HTTP_200_OK)


