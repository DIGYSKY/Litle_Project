import random
import string


def gener_password(number_chara, include_number):
    caracteres = string.ascii_letters
    if include_number:
        caracteres += string.digits
    caracteres += string.punctuation
    password = ''.join(random.choice(caracteres) for _ in range(number_chara))
    return password


print("Generateur de mots de passe !")
print("\n")
print("Definissez le nombre de charactère attandue ! (Par defaut 8 charactère)")

number_chara = input(">> ")

if number_chara != '':
    number_chara = int(number_chara)

if not isinstance(number_chara, int):
    number_chara: int = 8

print("\n")
print("Inclure des chiffre ? (Par defaut : oui)")

include_number = input("oui / non >> ").lower()

if include_number != "non" or include_number == "oui":
    include_number = "oui".lower() == "oui"
elif include_number == "non":
    include_number = "non".lower() == "oui"

MDP = gener_password(number_chara, include_number)

print("\n")

print(f"Votre nouveau mot de passe est : {MDP}")