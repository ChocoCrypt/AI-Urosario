import time
from tqdm import tqdm
from secret import simple_comp
from secret import super_secret_password
import numpy as np


class Side_Channel_Game:
    """
    An implementation of a side channel attack by timing as a game
    enviroment with different algorithms that may solve the problem of password
    cracking via timing attack.
    """
    def __init__(self):
        self.init_time = time.time
        self.cracked_initial_state = ""

    def crack_lenght(self):
        """Function for cracking the lenght of the key."""
        print("guessing lenght of the key...")
        base_string = ""
        means_vector = []
        for j,i in enumerate(range(10)):
            # This attack have sense if we check the mean of the times,
            # however, this may be incorrect, this method will be improved with
            # the time using reinforcement learning algorithms
            proms  = []
            for i in range(1000000):
                init = time.time()
                super_secret_password(base_string)
                fin = time.time()
                tot = fin-init
                proms.append(tot)
                base_string += "A"
            means_vector.append(np.mean(proms))
            print(np.mean(proms) , j)
        print(np.argmax(means_vector))



    def __str__(self):
        """
        This method is equivalent to the method called "Pintar Estado" in
        all the enviroments defined in class, the idea is to print the current
        state of the game
        """
        print(self.cracked_state)

    def acciones_aplicables(self , state):
        """
        Applicable actions are the words in the alphabet that may me used to
        crack a password, this can be dependent on the rules that a password may have.
        """
        alphabet = [chr(i) for i in range(ord("a") , ord("z")+1 )]
        alphabet += [chr(i) for i in range(ord("A") , ord("Z")+1 )]
        alphabet += "0 1 2 3 4 5 6 7 8 9 0".split(" ")
        alphabet += """! " # $ % & / ( ) = ? ¿ ¡ * ´ ' [ ] { } _ - . , :
            ;""".split(" ")



test = Side_Channel_Game()
# test.acciones_aplicables()
test.crack_lenght()
