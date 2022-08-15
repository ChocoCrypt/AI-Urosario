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
    def __init__(self):
        self.password = ""

    def crackear_longitud(self):
        """Metodo para calcular la longitud de la llave"""
        # Los strings ciclicos se usan mucho en el hacking para descifrar
        # longitudes de llaves o espacios de memoria.
        opciones = [str(cyclic(i))[2:-1].upper() for i in range(100) ]
        print(opciones[69])
        print(len(opciones[69]))

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




test = SideChannel_Game()
test.crackear_longitud()
