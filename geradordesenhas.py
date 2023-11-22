import random


def password_costumer():
    key = input("Digite os caractéres que você deseja para criar a senha: ")

    password = ""
    for word in key:
        if word in "Aa":
            password += "0"
        elif word in "Bb":
            password += "1"
        elif word in "Cc":
            password += "2"
        elif word in "Dd":
            password += "3"
        elif word in "Ee":
            password += "4"
        elif word in "Ff":
            password += "5"
        elif word in "Gg":
            password += "6"
        elif word in "Hh":
            password += "7"
        elif word in "Ii":
            password += "8"
        elif word in "Jj":
            password += "9"
        elif word in "Kk":
            password += "@"
        elif word in "Ll":
            password += "#"
        elif word in "Mm":
            password += "!!"
        elif word in "Nn":
            password += "$"
        elif word in "Oo":
            password += "*"
        elif word in "Pp":
            password += "+"
        elif word in "Qq":
            password += "{"
        elif word in "Rr":
            password += "}"
        elif word in "Ss":
            password += "["
        elif word in "Tt":
            password += "]"
        elif word in "Uu":
            password += "^"
        elif word in "Vv":
            password += "~"
        elif word in "Ww":
            password += "/"
        elif word in "Xx":
            password += "?"
        elif word in "Yy":
            password += ";"
        elif word in "Zz":
            password += ".,"
        elif word in "Çç":
            password += "="
        elif word in "Nn":
            password += "1"
        elif word in "0":
            password += "a"
        elif word in "1":
            password += "b"
        elif word in "2":
            password += "c"
        elif word in "3":
            password += "d"
        elif word in "4":
            password += "e"
        elif word in "5":
            password += "f"
        elif word in "6":
            password += "g"
        elif word in "7":
            password += "h"
        elif word in "8":
            password += "g"
        elif word in "{":
            password += "||"
        elif word in "}":
            password += "&"
        elif word in "[":
            password += "("
        elif word in "]":
            password += ")"
        elif word in "/":
            password += "__"
        elif word in ";":
            password += "//"
        elif word in ":":
            password += "<"
        elif word in ",":
            password += ">"
        elif word in ".":
            password += ","
        elif word in "-":
            password += "¨¨"

    print(f"Aqui está sua senha: {password}")


def random_password(length=12):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = 1234567809
    symbols = "[]{}/?*&%$#@;:|_-"
    all = f"{lower}{upper}{number}{symbols}"
    password = "".join(random.sample(all, length))
    print(password)


while True:
    print('A-Senha customizada')
    print('B-Senha aleatória')
    print('Pressione qualquer tecla para sair do programa')

    select = input('selecione a forma de gerar sua senha (A ou B): ')

    if not select:
        print("Por favor, selecione uma opção.")
    elif select.upper() == 'A':
        password_costumer()
    elif select.upper() == 'B':
        random_password()
    elif select.upper() != 'A' or 'B':
        break

