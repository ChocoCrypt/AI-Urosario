import time
from simple_comp import simple_comp
from simple_comp import super_secret_password


class Side_Channel_Game:
    """
    An implementation of a side channel attack by timing as a game
    enviroment with different algorithms that may solve the problem of password
    cracking via timing attack.
    """
    def __init__(self):
        self.init_time = time.time