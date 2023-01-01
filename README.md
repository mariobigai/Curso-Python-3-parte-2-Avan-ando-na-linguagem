# Curso-Python-3-parte-2-Avan-ando-na-linguagem
Implementando algumas modificações no jogo de forca para revisar os conceitos do curso e adicionar algumas funcionalidades para deixar o jogo mais parecido
com a forca jogada manualmente.

Foram feitas 4 implementações:
1)Arquivo base com mais frutas;
2)Modificação da função "desenha_forca()" para contar os erros;
3)Tratamento de tentativas repetidas;
4)Modificações para deixar o jogo mais parecido com o real.

## 1)Arquivo base com mais frutas:
  o arquivo "palavra.txt" contém 69 frutas em ordem alfabética.
  
## 2)Modificação da função "desenha_forca()" para contar os erros:
Foi adicionado o print na função:
print("Ops, parece que você errou, você tem mais {} tentativas".format(7 - erros))
Assim o usuário sabe quantas erros ele ainda pode cometer

## 3)Tratamento de tentativas repetidas:

A string letras_tentadas = "" foi criada com a responsabilidade de adicionar as letras
chutadas pelo usuário, e foi utilizada no laço principal do jogo        
Dessa forma, se a letra chutada já foi considerada o é chamada a função imprime_aviso(),
que alerta o usuário que a letra já foi chutada, e que ele deve escolher um letra diferente,
sem penalizar o usuário com um erro.

## 4)Modificações para deixar o jogo mais parecido com o real:

### Ser menos rígido com acentos e "ç":

Como algumas frutas tem acentos e "ç", e geralmente não é necessários acertar os acentos.
Então foi implementado uma função "simplifica_palavra_secreta()", que retorna
a palavra secreta simplificada (ASCII), isso é feito pela biblioteca Unidecode: <https://pypi.org/project/Unidecode/>
Assim, no laço principal do jogo na condição para chamar a função "marca_chute_correto()" passa ser:
  
if (chute in palavra_secreta_simplificada or chute in palavra_secreta)
  
E a função "marca_chute_correto()" também recebe o a "palavra_secreta_simplificada" como
parâmetro, e modificada.
Desse modo, palavra_secreta e palavra_secreta_simplificada são percorridas, e são
exibidas as letras correspondentes do chute contidas na palavra secreta.        
Dessa forma o usuário se o usuário acertar apenas a letra, ou a letra e o acento em ambos os casos
é considerado o acerto. Por exemplo:

*Palavra_secreta:"MAÇÃ", se o primeiro chute for "A" irá marcar ["_", "A", "_", "Ã"]
                       , se o primeiro chute for "Ã' irá marcar ["_", "_", "_", "Ã"]
                       , se o primeiro chute for "C" irá marcar ["_", "_", "Ç", "_"]
                       , se o primeiro chute for "Ç" irá marcar ["_", "_", "Ç", "_"]

### Considerar o hífen como dado, e não letra a ser advinhada:

Algumas frutas tem hífen, e geralmente não é exigido do usuário advinhar isso.
Para corrigir isso foi feito uma modificação simples na função "inicializa_letras_acertadas()"
onde feita através de um LIST COMPREHESION com IF e ELSE: 

def incializa_letras_acertadas(palavra):
    return ["-" if letra == "-" else "_" for letra in palavra]
