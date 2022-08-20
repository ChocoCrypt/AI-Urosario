from timing_enviroment import *


def greedy_search(problema):
    estado_inicial = problema.estado_inicial
    tam_llave = problema.crackear_longitud()
    not_solved = True
    while(not_solved):
        mejor_accion = np.argmax(juego.get_euristicas_tiempo(estado_inicial , tam_llave))
        estado_inicial = juego.transicion(estado_inicial , mejor_accion)
        print(estado_inicial)
    



juego = SideChannel_Game()
greedy_search(juego)

