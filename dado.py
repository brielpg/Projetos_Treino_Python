import random
import time
from colorama import init, Fore

# CREDITS https://github.com/brielpg

init(autoreset=True)


def titulo():
    print(Fore.LIGHTGREEN_EX + "####/############/####")
    print(Fore.LIGHTGREEN_EX + "\tJogo dos Dados")
    print(Fore.LIGHTGREEN_EX + "####/############/####")


def codigo():

    numero_aleatorio = random.randint(1, 6)
    numero_aleatorio2 = random.randint(1, 6)

    print("Irei jogar dois dados, vamos ver quais números cairao")
    time.sleep(0.9)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1.1)
    print("...")
    time.sleep(1.3)
    print(f"Os números sorteados foram: {Fore.LIGHTBLUE_EX}{numero_aleatorio} {Fore.RESET}e {Fore.LIGHTBLUE_EX}{numero_aleatorio2}")


titulo()
input(f"\nPressione {Fore.LIGHTYELLOW_EX}ENTER{Fore.RESET} para jogar os dados...")
codigo()
