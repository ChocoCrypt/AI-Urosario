from timing_enviroment import * 


class Nodo:
    def __init__(self, texto, madre, costo_caminao , profundidad):
        self.texto = texto
        self.madre = madre
        self.costo_camino = costo_camino
        self.profundidad = profundidad

class AttackTree:
    def __init__(self, profundidad):
        self.juego = SideChannel_Game()
        self.profundidad = profundidad
        self.raiz = Nodo("" , None, 0 , 0)
    
    def crear_arbol(self): 
        profundidad = self.raiz.profundidad
        while(profundidad < self.profundidad):





jaja = AttackTree(4)
jaja.crear_arbol()
