import time
from secret import simple_comp
from secret import super_secret_password


class Side_Channel_Game:
    """
    An implementation of a side channel attack by timing as a game
    enviroment with different algorithms that may solve the problem of password
    cracking via timing attack.
    """
    def __init__(self):
        self.init_time = time.time
        self.cracked_state = ""

    def __str__(self):
        """
        This method is equivalent to the method called "Pintar Estado" in
        all the enviroments defined in class, the idea is to print the current
        state of the game
        """
        print(self.cracked_state)

    def acciones_aplicables(self):
        """
        Applicable actions are the words in the alphabet that may me used to
        crack a password.
        """
        alphabet = [chr(i) for i in range(ord("a") , ord("z")+1 )]
        alphabet += [chr(i) for i in range(ord("A") , ord("Z")+1 )]
        alphabet += "0 1 2 3 4 5 6 7 8 9 0".split(" ")
        print(alphabet)
        print(len(alphabet))


test = Side_Channel_Game()
test.acciones_aplicables()
