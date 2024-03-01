import time
from random import randrange
import random
import string

# CREDITS https://github.com/brielpg


def lobby():
    # TITULO
    print("\t====#==============#====\n\tBem-Vindo(a) ao programa\n\t====#==============#====")
    ql_operacao = input("Qual aplicativo você quer iniciar?\n1-Calculadora\n2-Tabuada\n3-Gerador de número"
                        "\n4-Gerador de senha\n5-Sair\n")

    # CODE
    if ql_operacao == '1' or ql_operacao.lower == "calculadora":
        calculadora()
    elif ql_operacao == '2' or ql_operacao.lower() == "tabuada":
        calc_tabuada()
    elif ql_operacao == '3' or ql_operacao.lower() == "gerador de número":
        numero_random()
    elif ql_operacao == '4' or ql_operacao.lower() == "gerador de senha":
        pass_random()
    elif ql_operacao == '5' or ql_operacao.lower() == "sair":
        print("Saindo do programa...")
        time.sleep(0.6)
        exit()
    else:
        print("Valor Inválido, tente novamente com:\n1- Calculadora\n2- Tabuada\n3- Sair")


def calculadora():
    while True:
        ql_op = str(input("\nQual destas operações matemáticas você quer?\nDigite \"sair\" para sair'\n* Multiplicação"
                          "\n/ Divisão\n+ Soma\n- Subtração\n% Resto\n"))
        if ql_op == '*' or ql_op.lower() == "multiplicação" or ql_op.lower() == "multiplicacao":
            nmr1 = float(input("Escolha o primeiro número: "))
            nmr2 = float(input("Escolha o segundo número: "))
            print(f"O resultado da multiplicação entre {nmr1} x {nmr2} = {nmr1 * nmr2}")
            time.sleep(1.5)
        elif ql_op == '/' or ql_op.lower() == "divisão" or ql_op.lower() == "divisao":
            nmr1 = float(input("Escolha o primeiro número: "))
            nmr2 = float(input("Escolha o segundo número: "))
            print(f"O resultado da divisão entre {nmr1} / {nmr2} = {nmr1 / nmr2}")
            time.sleep(1.5)
        elif ql_op == '+' or ql_op.lower() == "soma" or ql_op.lower() == "adição":
            nmr1 = float(input("Escolha o primeiro número: "))
            nmr2 = float(input("Escolha o segundo número: "))
            # https://github.com/brielpg
            print(f"O resultado da soma entre {nmr1} + {nmr2} = {nmr1 + nmr2}")
            time.sleep(1.5)
        elif ql_op == '-' or ql_op.lower() == "subtração" or ql_op.lower() == "subtracao":
            nmr1 = float(input("Escolha o primeiro número: "))
            nmr2 = float(input("Escolha o segundo número: "))
            print(f"O resultado da subtração entre {nmr1} - {nmr2} = {nmr1 - nmr2}")
            time.sleep(1.5)
        elif ql_op == '%' or ql_op.lower() == "resto" or ql_op.lower() == "sobra":
            nmr1 = float(input("Escolha o primeiro número: "))
            nmr2 = float(input("Escolha o segundo número: "))
            print(f"O resultado do resto entre {nmr1} % {nmr2} = {nmr1 % nmr2}")
            time.sleep(1.5)
        elif ql_op.lower() == "sair":
            lobby()
        else:
            print("Valor Inválido, tente novamente")
            time.sleep(0.7)


def calc_tabuada():
    while True:

        tabuada = int(input("Digite o número que deseja a tabuada: "))
        qnt_tabuadaa = int(input("Até que número você deseja a tabuada?\n"))
        print(f"Tabuada do número {tabuada}")

        for conta in range(1, qnt_tabuadaa + 1):
            print(f"\t{tabuada} x {conta} = {tabuada * conta}")
        # https://github.com/brielpg
        deseja_continuar = str(input("Deseja continuar? s/n\n"))
        if deseja_continuar.lower() == 's' or deseja_continuar.lower() == "sim":
            time.sleep(0.65)
        else:
            lobby()


def numero_random():
    while True:

        ate_que_valor = int(input("Até que valor você gostaria de gerar um número aleatório?\n"))
        print(f"Número Gerado = {randrange(ate_que_valor)}")

        time.sleep(0.7)

        deseja_continuar = str(input("Deseja continuar? s/n\n"))
        if deseja_continuar.lower() == 's' or deseja_continuar.lower() == "sim":
            time.sleep(0.65)
        else:
            lobby()


def pass_random():
    tamanho_senha = int(input("Tamanho da senha: "))
    print("Escolha os caracteres da sua senha:\n1- Letras\n2- Números\n3- Caracteres Especiais\n4- Pronto")

    gerandosenha = ""

    while True:
        choice = int(input("Escolha o número "))

        if choice == 1:
            gerandosenha += string.ascii_letters

        elif choice == 2:
            gerandosenha += string.digits

        elif choice == 3:
            gerandosenha += string.punctuation

        elif choice == 4:
            break
        else:
            print("Valor Inválido, tente novamente com os valores\n1- Letras\n2- Números"
                  "\n3- Caracteres Especiais\n4- Pronto")
    password = []

    for i in range(tamanho_senha):
        # PEGA UM VALOR ALEATÓRIO DA VAR "gerandosenha" e ACRESCENTA ESSE VALOR À LISTA "password"
        randomchar = random.choice(gerandosenha)
        password.append(randomchar)

    print(f"Sua senha gerada é " + "".join(password))


input("Pressione ENTER para continuar...")
lobby()
