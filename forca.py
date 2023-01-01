import random
from unidecode import unidecode

def jogar():
    imprime_mensagem_abertura()

    palavra_secreta = carrega_palavra_secreta()
    palavra_secreta_simplificada = simplifica_palavra_secreta(palavra_secreta)

    letras_acertadas = incializa_letras_acertadas(palavra_secreta)
    letras_tentadas = ""

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto(True)
    while(not enforcou and not acertou):
        chute = pede_chute()

        if (chute in letras_tentadas):
            imprime_mensagem_aviso()
        else:
            letras_tentadas += chute

            if (chute in palavra_secreta_simplificada or chute in palavra_secreta):
                marca_chute_correto(chute, letras_acertadas, palavra_secreta, palavra_secreta_simplificada)
            else:
                erros += 1
                desenha_forca(erros)


        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)
        print("Letras tentadas: {}".format(list(letras_tentadas)))

    if ("_" not in letras_acertadas):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo")

def imprime_mensagem_aviso():
    print("Você já chutou essa letra! Escolha outra letra")


def simplifica_palavra_secreta(palavra_secreta):
    palavra = unidecode(palavra_secreta)
    return palavra

def desenha_forca(erros):
    print("Ops, parece que você errou, você tem mais {} tentativas".format(7 - erros))
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marca_chute_correto(chute, letras_acertadas, palavra_secreta, palavra_secreta_simplificada):
    index = 0
    for letra in palavra_secreta_simplificada:
        if (chute == letra):
            letras_acertadas[index] = palavra_secreta[index]
        index += 1
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = palavra_secreta[index]
        index += 1



def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    # arquivo = open("palavra.txt", "r")
    palavras = []
    with open("palavra.txt", "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)
    # arquivo.close()
    numero = random.randrange(0, len(palavras))
    #palavra_secreta = palavras[numero].upper()
    palavra_secreta = "maçã".upper()

    return palavra_secreta


def incializa_letras_acertadas(palavra):
    return ["-" if letra == "-" else "_" for letra in palavra]

def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()

    return chute

if (__name__ == "__main__"):
    jogar()