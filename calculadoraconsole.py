import time
from colorama import init, Fore

# CREDITS https://github.com/brielpg

init(autoreset=True)


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        return f"{Fore.RED}Divisão por zero não é permitida."
    else:
        return x / y


def comecando_programa():
    print(f"{Fore.LIGHTMAGENTA_EX}Selecione uma operação:")
    print(f"{Fore.LIGHTYELLOW_EX}+ {Fore.RESET}Adição")
    print(f"{Fore.LIGHTYELLOW_EX}- {Fore.RESET}Subtração")
    print(f"{Fore.LIGHTYELLOW_EX}* {Fore.RESET}Multiplicação")
    print(f"{Fore.LIGHTYELLOW_EX}/ {Fore.RESET}Divisão")
    print("")


input(f"Aperte {Fore.LIGHTYELLOW_EX}ENTER{Fore.RESET} para começar...")
comecando_programa()

eoperacao = input(f"Digite a sua operação ({Fore.LIGHTYELLOW_EX}+{Fore.RESET}, {Fore.LIGHTYELLOW_EX}-{Fore.RESET}, {Fore.LIGHTYELLOW_EX}*{Fore.RESET}, {Fore.LIGHTYELLOW_EX}/{Fore.RESET}): ")

enumero1 = float(input("\nDigite o primeiro número: "))
enumero2 = float(input("Digite o segundo número: "))

if eoperacao == '+':
    time.sleep(0.5)
    print(f"{enumero1} + {enumero2} = {Fore.LIGHTCYAN_EX}{adicao(enumero1, enumero2)}")

elif eoperacao == '-':
    time.sleep(0.5)
    print(f"{enumero1} - {enumero2} = {Fore.LIGHTCYAN_EX}{subtracao(enumero1, enumero2)}")

elif eoperacao == '*':
    time.sleep(0.5)
    print(f"{enumero1} * {enumero2} = {Fore.LIGHTCYAN_EX}{multiplicacao(enumero1, enumero2)}")

elif eoperacao == '/':
    time.sleep(0.5)
    print(f"{enumero1} / {enumero2} = {Fore.LIGHTCYAN_EX}{divisao(enumero1, enumero2)}")

else:
    print(f"{Fore.LIGHTRED_EX}Opção inválida")
