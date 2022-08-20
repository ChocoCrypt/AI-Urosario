from timing_enviroment import *


def greedy_search(problema):
    """
    Greedy search aplicado a la euristica definida como que el que mas se
    demora es mejor.
    """
    estado_inicial = problema.estado_inicial
    tam_llave = problema.crackear_longitud()
    solved = False
    while(not solved):
        mejor_accion = np.argmax(juego.get_euristicas_tiempo(estado_inicial , tam_llave))
        estado_inicial = problema.transicion(estado_inicial , mejor_accion)
        print(estado_inicial)
        solved = problema.test_objetivo(estado_inicial)
        if(len(estado_inicial) > tam_llave):
            print("Pailas, se equivocó")
            return("Pailas!")
    print(f"Le pegó! la llave es {estado_inicial}")
    return(estado_inicial)
    
def backtracking(problema):
    """
    Implementación del algoritmo de backtracking aplicado al problema de un
    ataque a la comparación trivial via Timming Attack.
    """



juego = SideChannel_Game()
greedy_search(juego)

