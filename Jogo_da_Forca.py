import random


def boas_vindas():
    print("*" * 45)
    print("*" + " " * 43 + "*")
    print("*        Bem-vindo ao Jogo de Forca!        *")
    print("*   Tente advinhar qual a palavra secreta!  *")
    print("*                 Boa Sorte!                *")
    print("*" + " " * 43 + "*")
    print("*" * 45, end="\n\n")


def escolher_palavra_secreta():
    lista = []

    with open("./Jogo_da_Forca/lista.txt") as palavras:
        for palavra in palavras:
            palavra = palavra.strip().upper()
            lista.append(palavra)

    escolhe_palavra = random.randrange(0, len(lista))
    palavra_secreta = lista[escolhe_palavra]
    return palavra_secreta


def definir_letras_acertadas(palavra_secreta):
    return ["_" for letra in palavra_secreta]


def pedir_chute():
    chute = input("Chute uma letra: ")
    chute = chute.strip().upper()
    return chute


def acertou_chute(palavra_secreta, chute, letras_acertadas):
    posicao = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[posicao] = letra
        posicao += 1


def mostrar_boneco(erros):
    if erros == 0:
        print(
            """
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========
            """
        )

    if erros == 1:
        print(
            """
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========
            """
        )

    if erros == 2:
        print(
            """
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========
            """
        )

    if erros == 3:
        print(
            """
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========
            """
        )

    if erros == 4:
        print(
            """
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========
            """
        )

    if erros == 5:
        print(
            """
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                =========
            """
        )

    if erros == 6:
        print(
            """
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                =========
            """
        )


def mensagem_vitoria():
    print("Você GANHOU!")
    print(
        """
             ___________
            '._==_==_=_.'
            .-\:      /-.
           | (|:.     |) |
            '-|:.     |-'
              \::.    /
               '::. .'
                 ) (
               _.' '._
              `"""
        """"`
    """
    )


def mensagem_derrota(palavra_secreta):
    print("Você foi ENFORCADO!")
    print(
        """
 _;~)                  (~;_
(   |                  |   )
 ~', ',    ,''~'',   ,' ,'~
     ', ','       ',' ,'
       ',: {'} {'} :,'
         ;   /^\   ;
          ~\  ~  /~
        ,' ,~~~~~, ',
      ,' ,' ;~~~; ', ',
    ,' ,'    '''    ', ',
  (~  ;               ;  ~)
   -;_)               (_;-
    """
    )
    print(
        "A palavra secreta era {}. Mais sorte da próxima vez!".format(palavra_secreta)
    )


def jogar():
    boas_vindas()
    palavra_secreta = escolher_palavra_secreta()
    print("A palavra têm {} letras".format(len(palavra_secreta)), end="\n")

    erros = 0
    mostrar_boneco(erros)

    letras_acertadas = definir_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    while True:
        chute = pedir_chute()

        if chute in palavra_secreta:
            acertou_chute(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            print(
                "Você errou! Você ainda têm {} tentativas.".format(6 - erros),
                end="\n\n",
            )

        mostrar_boneco(erros)

        print(letras_acertadas)
        print("Ainda faltam {} letras para acertar".format(letras_acertadas.count("_")))

        if "_" not in letras_acertadas:
            mensagem_vitoria()
            break

        if erros == 6:
            mensagem_derrota(palavra_secreta)
            break


if __name__ == "__main__":
    jogar()
