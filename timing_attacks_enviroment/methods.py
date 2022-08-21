from timing_enviroment import *
from itertools import permutations , product
import random


def greedy_search(problema, iteraciones):
    """
    Greedy search aplicado a la euristica definida como que el que mas se
    demora es mejor.
    """
    estado_inicial = problema.estado_inicial
    tam_llave = problema.crackear_longitud()
    solved = False
    while(not solved):
        mejor_accion = np.argmax(problema.get_euristicas_tiempo(estado_inicial , tam_llave, iteraciones))
        estado_inicial = problema.transicion(estado_inicial , mejor_accion)
        print(estado_inicial)
        solved = problema.test_objetivo(estado_inicial)
    print(f"Le pegó! la llave es {estado_inicial}")
    return(estado_inicial)

def limited_greedy_search(problema, iteraciones):
    """
    Limited Greedy search aplicado a la euristica definida como que el que mas
    se demora es mejor.
    """
    estado_inicial = problema.estado_inicial
    tam_llave = problema.crackear_longitud()
    solved = False
    while(not solved):
        mejor_accion = np.argmax(problema.get_euristicas_tiempo(estado_inicial , tam_llave, iteraciones))
        estado_inicial = problema.transicion(estado_inicial , mejor_accion)
        print(estado_inicial)
        solved = problema.test_objetivo(estado_inicial)
        if(len(estado_inicial) > tam_llave):
            print("Pailas, se equivocó")
            return(False)
    print(f"Le pegó! la llave es {estado_inicial}")
    return(estado_inicial)
    

def backtracking(problema, iteraciones):
    """
    Implementación del algoritmo de backtracking aplicado al problema de un
    ataque a la comparación trivial via Timming Attack.
    """
    estado_inicial = problema.estado_inicial
    tam_llave = problema.crackear_longitud()
    solved = False
    acciones = problema.get_transiciones(estado_inicial)
    while(not solved):
        transicion_aleatoria = random.choice(acciones)
        print(acciones)
        print(f"se elegio la opcion {transicion_aleatoria}")
        if(problema.validar_estado(transicion_aleatoria, iteraciones)):
            estado_inicial = transicion_aleatoria
            # Reseteo las acciones
            acciones = problema.get_transiciones(estado_inicial)
        else:
            # Si la acción que tomé está errada simplemente la elimino y sigo
            # buscando
            acciones.remove(transicion_aleatoria)
        solved = problema.test_objetivo(estado_inicial)
        # Si no hay acciones pailas
        if(len(acciones)==0):
            print("no funcionó")
            return(False)
    return(estado_inicial)

def bruteforcing_(problema):
    """Este problema es equivalente a mirar todos los nodos de la raiz"""
    tam_llave = problema.crackear_longitud()
    mystring = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    combos = [''.join(i) for i in product(mystring, repeat = tam_llave)]
    for i in combos:
        if(problema.test_objetivo(i)):
            print(f"la llave es {i}")
            return(i)
    return(False)


def test_limited_greedy(problema,sample ,iteraciones):
    """
    Función de montecarlo para evaluar la efectividad del algoritmo de
    greedy search
    """
    tot = 0
    for i in range(sample):
        if(limited_greedy_search(problema,iteraciones) == "ABC"):
            tot += 1
    accuracy = tot/sample
    print(accuracy)
    return(accuracy)

def test_backtracking(problema,sample,iteraciones):
    """
    Implementación del método de montecarlo para evaluar la efectividad del
    algoritmo de backtracking.
    """
    tot = 0
    for i in range(sample):
        if(backtracking(problema,iteraciones) == "ABC"):
            tot += 1
    accuracy = tot/sample
    print(accuracy)
    return(accuracy)
