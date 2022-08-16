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
    result = string + "A"*faltante
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
        # Se supone que la llave mas larga posible tiene 50 caracteres
        opciones = [str(cyclic(i))[2:-1].upper() for i in range(50)] 
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

    def test_objetivo(self , estado):
        """
        Llama a la función secreta para saber si la contraseña es verdadera
        o no.
        """
        return(super_secret_password(estado))

    def costo(self,estado,accion):
        return 1

    def checkear_estado(self, estado):
        """
        Metodo para evaluar si un string (un estado) se no se ha equivocado en
        operaciones anteriores. Esto se puede saber puesto que en promedio
        todas las operaciones se demoran lo mismo. Si hay una diferencia
        significante entre alguna de las operaciones y el resto, esto significa
        que el estado se encuentra en un estado aceptable.
        1 - Este metodo funciona pero necesito un método matemático para
        retornar el resultado
        2 - Con el fin de reducir el ruido, sería buena idea añadir un delay en
        la función secret.
        """ 
        # Calculo el tamaño de la llave para crackearla.
        tam_llave = self.crackear_longitud()
        # Agarro todas las posibles acciones
        acciones_aplicables = self.acciones_aplicables(estado)
        todas_transiciones = [self.transicion(estado,i) for i in acciones_aplicables]
        transiciones_formateadas = [formatear_longitud(estado , tam_llave) for i in todas_transiciones]
        # Evaluacion segun la diferencia de medias
        datos_medias = []
        print(transiciones_formateadas)
        print("Evaluando todas las posibles transiciones...")
        for tra in tqdm(transiciones_formateadas):
            tiempos = []
            for j in range(100000): # Parece que 10000000 es un buen numero
                tiempo_inicial = time.time()
                super_secret_password(tra)
                tiempo_final = time.time()
                total = tiempo_final - tiempo_inicial
                tiempos.append(total)
            media = np.mean(tiempos)
            dat = {
                    "transicion":tra,
                    "media":media
                    }
            datos_medias.append(dat)
        pprint(datos_medias)
        # Plot
        if(self.plot):
            x = [i for i in range(len(datos_medias))]
            y = [i["media"] for i in datos_medias]
            sns.scatterplot(x,y)
            plt.show()
        


# Test
if __name__ == "__main__":
    test = SideChannel_Game(plot=True)
    test.checkear_estado("")
