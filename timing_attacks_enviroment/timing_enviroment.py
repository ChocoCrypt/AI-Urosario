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
        self.cracked_initial_state = "jijiji"
        # Define alphabet 
        self.alphabet = [chr(i) for i in range(ord("A") , ord("Z")+1 )] + [" "]


    def crack_lenght(self):
        """
        Function for cracking the lenght of the key. This method test every
        possible lenght of a key and returns the one that take most time
        processing.
        """
        print("guessing lenght of the key...")
        base_string = ""
        means_vector = []
        for i in tqdm(range(100)):
            # This attack have sense if we check the mean of the times,
            # however, this may be incorrect, this method will be improved with
            # the time using reinforcement learning algorithms
            proms  = []
            # Get the mean
            for i in range(100000):
                init = time.time()
                super_secret_password(base_string)
                fin = time.time()
                tot = fin-init
                proms.append(tot)
            base_string += "A"
            means_vector.append(np.mean(proms))
        lenght = np.argmax(means_vector)
        print(f"the lenght of the key is {lenght}")
        return(lenght)


    def __str__(self):
        """This method is equivalent to the method called pintar_estado"""
        print(self.cracked_state)





test = Side_Channel_Game()
test.crack_lenght()
