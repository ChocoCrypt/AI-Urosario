"""
Simple comparison function that is going to be atacked via timing attacks in
this project.
"""
from time import sleep


def simple_comp(str1, str2):
    """Intuitive comparison function."""
    if(len(str1) != len(str2)):
        return False
    else:
        for i in range(len(str1)):
            # añadir un sleep acá para hacer pruebas sin tanto ruido.
            if(str1[i] != str2[i]):
                return False
        return True


def super_secret_password(user_input):
    """Secret password comparisson against the given string."""
    secret = "BIEN"
    if(simple_comp(user_input, secret)):
        return True
    return False
