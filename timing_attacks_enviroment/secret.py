"""
Simple comparison function that is going to be atacked via timing attacks in
this project.
"""


def simple_comp(str1, str2):
    """Intuitive comparison function."""
    if(len(str1) != len(str2)):
        return False
    else:
        for i in range(len(str1)):
            if(str1[i] != str2[i]):
                return False
        return True


def super_secret_password(user_input):
    """Secret password comparisson against the given string."""
    # The lenght of this password is long to compare different algorithms of
    # the attack
    #secret = "ThisIsSupossedToBeASuperSecretPassworThatNooneIsGoingToGuess"
    secret = "Hola"
    if(simple_comp(user_input, secret)):
        return True
    else:
        return False


