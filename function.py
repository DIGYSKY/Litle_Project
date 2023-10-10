import random
import string


def gener_password(number_chara, include_number):
    if number_chara == 0:
        number_chara = 12
    caracteres = string.ascii_letters
    if include_number == 1:
        caracteres += string.digits
    caracteres += string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(number_chara))
    return password
