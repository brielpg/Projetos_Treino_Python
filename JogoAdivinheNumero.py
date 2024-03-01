import random
import os
from colorama import init, Fore

# CREDITS https://github.com/brielpg

init(autoreset=True)


def titulo():
    print(Fore.LIGHTGREEN_EX + "####/#################/####")
    print(Fore.LIGHTGREEN_EX + "Caminho dos Digitos".center(28))
    print(Fore.LIGHTGREEN_EX + "####/#################/####")


def numero_aleatorio():
    numero_gerado = random.randint(1, 100)
    return numero_gerado


def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def cmdigitos(numero, tentativa):
    while True:
        try:
            chute = int(input(
                f"\nTente adivinhar o número que estou pensando entre {Fore.GREEN}1{Fore.RESET} e {Fore.GREEN}100"
                f"{Fore.RESET}\nResposta: "))
            if chute > 100 or chute < 1:
                print(Fore.RED + "\nValor inválido, tente novamente")
            elif chute > numero:
                print(f"\nQuase Lá... \nO número que eu pensei é {Fore.LIGHTYELLOW_EX}MENOR{Fore.RESET} que {chute}.")
                tentativa += 1
            elif chute < numero:
                print(f"\nQuase Lá... \nO número que eu pensei é {Fore.LIGHTYELLOW_EX}MAIOR{Fore.RESET} que {chute}.")
                tentativa += 1
            elif chute == numero:
                print(Fore.GREEN + f"\nPARABÉNS!! {Fore.RESET}Você descobriu meu número com {tentativa} tentativas.")
                break
        except ValueError:
            print(Fore.RED + "\nSó vale números inteiros! Tente novamente.")


titulo()
input(f"\nDigite {Fore.LIGHTYELLOW_EX}ENTER{Fore.RESET} para iniciar o jogo...")
numero = numero_aleatorio()
tentativa = 0
cmdigitos(numero, tentativa)
