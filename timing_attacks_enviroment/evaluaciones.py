from timing_enviroment import * 
import json


def evaluacion_test_longitud(sample_size , n_size):
    """
    Metodo para evaluar la presición del método para calcular la longitud de
    una contraseña mediante un test de Montecarlo.
    
    - La variable "sample size" hace referencia al tamaño de la prueba de
    montecarlo.
    - La variable "n_size" hace referencia al número de veces que se intenta la
    misma contraseña para la recolección de las medias en el método de
    descifrar el tamaño de la contraseña.
    """
    test = SideChannel_Game(plot=False)
    bien = 0
    for i in range(sample_size):
        longitud = test.crackear_longitud(n_tries=n_size)
        if(longitud == 28):
            bien += 1
    # Calculo de el accuracy por el método de montecarlo
    acc = bien/sample_size
    print(f"el accuracy es de  {acc}")
    # Guardo los resultados en un archivo externo para luego evaluar.
    with open(f"evaluaciones/eval_{n_size}.json" , "w") as fp:
        obj_eval = {
                "montecarlo_size":sample_size,
                "n_size":n_size,
                "accuracy":acc
                }
        json.dump(obj_eval , fp)
    return(acc)


# Evaluación para el accuracy con distintos tamaños del arreglo
if __name__ == "__main__":
    # Tamaños candidatos a tener un buen accuracy:
    tamaños = [1 , 1000, 10000 , 50000, 100000, 300000, 500000, 1000000, 5000000 ]
    for tam in tamaños:
        evaluacion_test_longitud(1000 , tam)
