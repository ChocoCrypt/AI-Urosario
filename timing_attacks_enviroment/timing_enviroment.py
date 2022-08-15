"""An implementation of side Side Channel game - Rodrigo Castillo Camargo"""
from pwn import * # Liberería de hacking para generar strings ciclicos.
import time
from tqdm import tqdm
from secret import simple_comp
from secret import super_secret_password
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class SideChannel_Game:
    """
    Juego mediante el cuál se implementa un side channel attack para atacar la
    función de comparación de strings intuitiva.
    """
    def __init__(self , plot = False):
        """Metodo Inicializador, la contraseña inicial es vacía"""
        self.plot = plot
        self.estado_inicial = ""

    def checkear_estado(self, estado):
        """
        Metodo para evaluar si un string (un estado) se no se ha equivocado en
        operaciones anteriores. Esto se puede saber puesto que en promedio
        todas las operaciones se demoran lo mismo. Si hay una diferencia
        significante entre alguna de las operaciones y el resto, esto significa
        que el estado se encuentra en un estado aceptable.
        """

    def crackear_longitud(self , n_tries = 100000):
        """
        Metodo para calcular la longitud de la llave
        1- Este metodo no funciona con exactitud precisa y se cree que es
        posible encontrar un algoritmo mejor para esto.
        2- Esta pendiente evaluar este metodo para medir su exactitud mediante
        un test de montecarlo.
        """
        # Los strings ciclicos se usan mucho en el hacking para descifrar
        # longitudes de llaves o espacios de memoria.
        opciones = [str(cyclic(i))[2:-1].upper() for i in range(100) ]
        medias_tiempos = []
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

    def acciones_aplicables(self,estado):
        """
        Devuelve una lista de acciones que representan las posibles letras
        que podemos añadir o quitar.
        """
        # Falta poner la restricción de la longitud de la lista
        indices  = [i for i in range(len(range(ord("A") , ord("Z") +1)))]
        return(indices)
    
    def transicion(self,estado,indice):
        """Devuelve una contraseña aplicando una letra """
        posibles_acciones = [estado + str(i) for i in range(ord("A") , ord("Z")+1)]
        return(posibles_acciones[indice])

    def test_objetivo(self , estado):
        """
        Llama a la función secreta para saber si la contraseña es verdadera
        o no.
        """
        return(super_secret_password(estado))

    def costo(self,estado,accion):
        return 1



