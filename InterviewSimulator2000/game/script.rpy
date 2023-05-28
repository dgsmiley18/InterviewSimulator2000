# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define eil = Character("Eileen")
image BG FutonRoom = ("images/Futon_Room.png")
image entrevistadora = ("images/entrevistadora.png")
image entrevistadora choque = ("images/entrevistadora_choque.png")

define Entrevistadora = Character("Entrevistadora")

define Candidato = Character("Candidato")

# The game starts here.

label inicio:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene BG FutonRoom with dissolve
    play sound "audio/vntrack01.mp3" fadein 0.8

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # Imagem da entrevistadora vai aparec
    show entrevistadora with dissolve:
        xzoom 0.5 yzoom 0.5

    # These display lines of dialogue.

    Entrevistadora "Boa noite, como você vai?"

    # This displays a menu of choices. The player will be able to click

    stop sound
    menu apresentar:
        "Como será que devo responder ela?"
        "Dar boa noite também":
            Candidato "Boa noite, eu estou muito bem e você?"

        "Responder de forma rude":
            Candidato "Vá te fuder, não é da sua conta"
            show entrevistadora choque with dissolve
            Entrevistadora "Como assim? Você não quer o emprego?"
            jump caminho_da_rua

        "Não responder":
            Candidato "..."
            Entrevistadora "Você está bem?"
            jump inicio_entrevista

label caminho_da_rua:
    Entrevistadora "Parece que você não é apto para esse emprego"

label inicio_entrevista:

    Entrevistadora "Vamos começar com a nossa entrevista?"

    # This ends the game.
label primeira_pergunta:

label segunda_pergunta:
    return
