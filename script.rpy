init python:
    Prosseguir = False

init python:
    exp = False

init python:
    sp = False
   

define e = Character("Entrevistadora")
define en = Character('Entrevistado')

image entrevistadora = "images/en.png"
image fundao = "images/ci.png"


label start:
    play music "audio/audiofundo1.weba"
    scene fundao:
        zoom 1.5

    show entrevistadora
    with fade

    e "Olá, tudo bem? Eu represento a Flux Express, uma empresa estabelecida há 20 anos no mercado, dedicada a prestar serviços à comunidade, comercializar produtos e apoiar profissionais no campo de Tecnologia da Informação." 
    e "Gostaríamos de informar que você está atualmente participando do nosso processo seletivo para a posição de Analista de Testes. Esta breve entrevista online tem como objetivo nos permitir conhecer melhor você e avaliar como sua experiência e habilidades podem contribuir para o nosso ambiente de trabalho."

    e "Se estiver de acordo, poderíamos prosseguir com a entrevista?"

    menu:
        "Podemos sim":
            en 'Prossiga, por favor!'
            $Prosseguir = True
            
        "Desisto":
            en "Não quero prosseguir"
            $Prosseguir = False 

    if Prosseguir == True:
        e "Otimo! Entâo vamos prosseguir."
        jump pergunta_inicial

    if Prosseguir == False:
        e "Vamos encerrar por aqui."
    return

label pergunta_inicial:
    e "Vamos começar! Para comerçarmos, precisamos inicialmente saber se essa é a sua primeira  experiência?"
    
    menu:
        "Sim, essa é minha primeira experiência.":
            en "Já tive experiência na área."
            $exp = True

        "Rasoalvelmente, já ocupei cargo por pouco tempo.":
            en "Já trabalhei por curto périodo."
            $exp = True

        "Não possuo experiência nessa área.":
            en "Essa é será minha primeira experiência."
            $exp = False

if exp == True:
    e 'Otimo! Toda a experiência é bem vinda em nossa empresa.'
    jump segunda_pergunta
    
if exp == False:
    e 'Ok! Então vamos prosseguir para a próxima pergunta.'
    jump segunda_pergunta

label segunda_pergunta:
    e "Vamos para a segunda pergunta. Por que você quer este trabalho?  " 

    menu: 
        "Responder com desdém":
            en "Essa pergunta é realmente importante?"
            $sp = False
        "Responder com sarcasmo":
            en "Talvez eu precise do dinheiro."
            $sp = False
        "Responder com educação":
            en "Acredito que vou adquirir bastante conhecimento nesta empresa"
            $sp = True
if sp == True:
    e "Ótima resposta. Vamos prosseguir!"
    jump terceira_pergunta
    
if sp == False:
    e "Vamos a próxima pergunta!"
    jump terceira_pergunta

label terceira_pergunta:
    e "Agora que sabemos o motivo  de sua bsuca por esse emprego, vamos a próxima pergunta.  Onde você se vê daqui a 5 anos?"
    menu:
        "Responder com arrogância":
            en "bem longe daqui"
        "Responder com dúvida":
            en "Ainda não pensei sobre isso."
        "Responder de forma convicente":
            en "Espero ter realizado uma faculdade, ter minha vida financeira estável, e com uma carreia brilhant em formação"





     

            
            
        

            