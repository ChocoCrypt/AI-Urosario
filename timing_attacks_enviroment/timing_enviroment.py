"""An implementation of side Side Channel game - Rodrigo Castillo Camargo"""
from pwn import * # Liberería de hacking para generar strings ciclicos.
import time
from tqdm import tqdm
from secret import simple_comp
from secret import super_secret_password
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pprint import pprint # Libreria para imprimir diccionarios bonitos


def formatear_longitud(string , lenght):
    """Metodo para formatear un string al tamaño de la llave"""
    faltante = lenght - len(string)
    result = string + "A"*(faltante )
    return(result)


class SideChannel_Game: 
    """
    Juego mediante el cuál se implementa un side channel attack para atacar la
    función de comparación de strings intuitiva.
    """
    def __init__(self , plot = False):
        """Metodo Inicializador, la contraseña inicial es vacía"""
        self.plot = plot
        self.estado_inicial = ""

    def crackear_longitud(self , n_tries = 100000):
        """
        Metodo para calcular la longitud de la llave
        1- Este metodo no funciona con exactitud precisa y se cree que es
        posible encontrar un algoritmo mejor para esto.
        2- Esta pendiente evaluar este metodo para medir su exactitud mediante
        un test de montecarlo.
        3- No se está dispuesto a aceptar una eficacia menor a 98%
        """
        # Los strings ciclicos se usan mucho en el hacking para descifrar
        # longitudes de llaves o espacios de memoria.
        # Se supone que la llave mas larga posible tiene 10 caracteres
        opciones = [str(cyclic(i))[2:-1].upper() for i in range(10)] 
        medias_tiempos = []
        print("crackeando longitud...")
        for i in tqdm(opciones):
            tiempos = []
            for j in range(n_tries):
                tiempo_inicial = time.time()
                super_secret_password(i)
                tiempo_final = time.time()
                tiempo_total = tiempo_final - tiempo_inicial
                tiempos.append(tiempo_total)
            media = np.mean(tiempos)
            medias_tiempos.append(media)
        # Ploteo la media de tiempos
        if(self.plot): 
            y = [i for i in range(len(opciones))]
            x = medias_tiempos
            plt.xlabel("tamaño de la llave")
            plt.ylabel("duración de la comparación")
            plt.scatter(y,x)
            plt.show()
        # El indice que mas se demoró en promedio es el tamaño del password.
        print(f"la longitud de la llave es {np.argmax(medias_tiempos)}  ")
        return(np.argmax(medias_tiempos))

    def pintar_estado(self , estado):
        """
        Dibuja el estado correspondiente a la contraseña ingresada en el
        momento.
        """
        print(estado)
        return estado

    def acciones_aplicables(self,estado):
        """
        Devuelve una lista de acciones que representan las posibles letras
        que podemos añadir o quitar.
        - ¿Deberia poner en las acciones aplicables la opción de eliminar una
          letra al estado?
        """
        # Falta poner la restricción de la longitud de la lista
        indices  = [i for i in range(len(range(ord("A") , ord("Z") +1)))]
        return(indices)
    
    def transicion(self,estado,indice):
        """Devuelve una contraseña aplicando una letra """
        posibles_acciones = [estado + chr(i) for i in range(ord("A") , ord("Z")+1)]
        return(posibles_acciones[indice])

    def get_transiciones(self,estado):
        """Devuelve una lista con todas las posibles transiciones de un estado"""
        lista = [self.transicion(estado, i) for i in self.acciones_aplicables(estado)]
        return(lista)

    def test_objetivo(self , estado):
        """
        Llama a la función secreta para saber si la contraseña es verdadera
        o no.
        """
        return(super_secret_password(estado))

    def costo(self,estado,accion):
        return 1

    def test(self, estado , tam_llave, iteraciones):
        """
        Metodo para evaluar si un string (un estado) se no se ha equivocado en
        operaciones anteriores. Esto se puede saber puesto que en promedio
        todas las operaciones se demoran lo mismo. Si hay una diferencia
        significante entre alguna de las operaciones y el resto, esto significa
        que el estado se encuentra en un estado aceptable.
        1- Este metodo funciona en conjunto con el metodo llamado 'test' , de
        lo contrario, no tiene sentido.
        """ 
        # Agarro todas las posibles acciones
        acciones_aplicables = self.acciones_aplicables(estado)
        todas_transiciones = [self.transicion(estado,i) for i in acciones_aplicables]
        # Formateo la longitud de los estados para que encajen con la llave
        transiciones_formateadas = [formatear_longitud(i , tam_llave) for i in todas_transiciones]
        # Lista de medias de tiempos de cada string formateado
        medias = []
        # Las pruebas me dieron que con 5000000 se puede evaluar bien la longitud de un estado
        print("calculando resultados...")
        for pal in tqdm(transiciones_formateadas):
            observaciones = []
            for i in range(iteraciones): # Funciona bien desde 5000000
                tiempo_inicial = time.time()
                super_secret_password(pal)
                tiempo_final = time.time()
                tiempo_total = tiempo_final - tiempo_inicial
                observaciones.append(tiempo_total)
            media = np.mean(observaciones)
            medias.append(media)
        indice_correcto = np.argmax(medias)
        accion_correcta = transiciones_formateadas[indice_correcto]
        return(accion_correcta)

    def validar_estado(self , estado, iteraciones):
        """
        La letra que mas se demora es la correcta, para verificar si no se ha
        equivocado el algoritmo antes se me ocurrió calcular la letra n
        veces, si todas son iguales, quiere decir que es la correcta, si no,
        la probabilidad de que se esté fallando es muy alta.
        """
        # Calculo el tamaño de la llave para crackearla.
        tam_llave = self.crackear_longitud()
        results = []
        # Entre mayor sea n se está mas seguro de que los resultados están bien.
        for i in range(3): 
            result = self.test(estado , tam_llave, iteraciones)
            results.append(result)
        if(len(set(results)) == 1):
            return(True)
        return False

    def get_euristicas_tiempo(self, estado , tam_llave, iteraciones):
        """
        Definimos una euristica la cuál considera como la mejor opción la
        acción que mas tiempo se demora en promedio.
        """
        # Agarro todas las posibles acciones
        acciones_aplicables = self.acciones_aplicables(estado)
        todas_transiciones = [self.transicion(estado,i) for i in acciones_aplicables]
        # Formateo la longitud de los estados para que encajen con la llave
        transiciones_formateadas = [formatear_longitud(i , tam_llave) for i in todas_transiciones]
        # Lista de medias de tiempos de cada string formateado
        medias = []
        print("calculando resultados...")
        for pal in tqdm(transiciones_formateadas):
            observaciones = []
            for i in range(iteraciones): # Funciona bien desde 5000000
                tiempo_inicial = time.time()
                super_secret_password(pal)
                tiempo_final = time.time()
                tiempo_total = tiempo_final - tiempo_inicial
                observaciones.append(tiempo_total)
            media = np.mean(observaciones)
            medias.append(media)
        if(self.plot):
            x = [i for i in range(len(medias))]
            y = [medias]
            plt.xlabel("posiciones de caracteres")
            plt.ylabel("tiempos de ejecución")
            plt.scatter(x,y)
            plt.show()
        return(medias)
    
    def codigo(self,estado):
        """Funcion codigo necesaria para implementar la clase Nodo"""
        self.estado

    def quitar_ultimo_caracter(self,estado):
        """
        Decidimos tomar la accion de eliminar el ultimo caracter de un estado
        como una accion independiente puesto que de ponerlo en las transiciones
        posibles se dañaría el método de greedy search.
        """
        if(len(estado) > 1):
            return(estado[:-1])
        else:
            return(estado)
