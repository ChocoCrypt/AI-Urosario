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
        print(self.password)


print(np.matrix([[0] *8]*8 ) )
