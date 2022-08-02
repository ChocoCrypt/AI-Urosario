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
        self.alphabet = [chr(i) for i in range(ord("a") , ord("z")+1 )]
        self.alphabet += [chr(i) for i in range(ord("A") , ord("Z")+1 )]
        self.alphabet += "0 1 2 3 4 5 6 7 8 9 0".split(" ")
        self.alphabet += """! " # $ % & / ( ) = ? ¿ ¡ * ´ ' [ ] { } _ - . , :
            ;""".split(" ")

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

    def check_letter(self):
        """
        This method check if the last letter is okay, if it returns true it
        means that the letter is okay, but if it does not return true, it means
        that one letter before the letter that we already put is not okay.

        The way to know if a letter is okay is to check the nextone, if all the
        means of the next letter are similars it means we commit an error in a
        previous state.
        """
        print(f"checking if {self.cracked_initial_state} is ok or not")
        means = []
        for char in tqdm(self.alphabet):
            time_per_char = []
            for i in range(10000):
                init = time.time()
                super_secret_password(char)
                fin = time.time()
                time_per_char.append(fin - init)
            means.append(np.mean(time_per_char))
        # Empirically i noticed that when the key is ok the variance goes to
        # 2.2 and when is bad the variances go below 0.1, then i'll  say that
        # they key is not okay when the variance goes below 0.5
        var = np.var(means)
        print(var)
                




    def __str__(self):
        """
        This method is equivalent to the method called "Pintar Estado" in
        all the enviroments defined in class, the idea is to print the current
        state of the game
        """
        print(self.cracked_state)


    def acciones_aplicables(self , position):
        """
        Applicable actions are the words in the alphabet that may me used to
        crack a password, this can be dependent on the rules that a password may have.
        """
        try:
            self.cracked_initial_state += self.alphabet[i]
        except:
            print("this position is not a valid interger corresponding to the alphabet")



test = Side_Channel_Game()
# test.acciones_aplicables()
# test.crack_lenght()
test.check_letter()
