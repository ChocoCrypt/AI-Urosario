"""An implementation of side Side Channel game - Rodrigo Castillo Camargo"""
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




test = SideChannel_Game()
