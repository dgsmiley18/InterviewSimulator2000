init:
    $ pontos = 100

define entrevistadora = Character("Entrevistadora")
define entrevistado = Character('Entrevistado')

image entrevistadora = "images/en.png"
image fundao = "images/ci.png"


label start:
    
    play music "audio/audiofundo1.mp3"
    scene fundao:
        zoom 1.5

    show entrevistadora
    with fade

    entrevistadora "Olá, tudo bem? Eu represento a Flux Express, uma empresa estabelecida há 20 anos no mercado, dedicada a prestar serviços à comunidade, comercializar produtos e apoiar profissionais no campo de Tecnologia da Informação." 
    entrevistadora "Gostaríamos de informar que você está atualmente participando do nosso processo seletivo para a posição de Analista de Testes. Esta breve entrevista online tem como objetivo nos permitir conhecer melhor você e avaliar como sua experiência e habilidades podem contribuir para o nosso ambiente de trabalho."

    entrevistadora "Se estiver de acordo, poderíamos prosseguir com a entrevista?"

    menu:
        "Podemos sim":
            entrevistado 'Prossiga, por favor!'
            jump pergunta_inicial

        "Desisto":
            entrevistado "Não quero prosseguir"
            jump encerrar

label encerrar:
    entrevistado "Tudo bem então, tenha um bom dia"
    $ renpy.quit()

label pergunta_inicial:
    entrevistadora "Vamos começar! Para comerçarmos, precisamos inicialmente saber se essa é a sua primeira  experiência?"
    
    menu:
        "Sim, essa é minha primeira experiência.":
            entrevistado "Já tive experiência na área."
            $ pontos += 10
            jump segunda_pergunta

        "Rasoalvelmente, já ocupei cargo por pouco tempo.":
            $ pontos += 10
            entrevistado "Já trabalhei por curto périodo."
            jump segunda_pergunta

        "Não possuo experiência nessa área.":
            $ pontos += 0
            entrevistado "Essa é será minha primeira experiência."
            jump segunda_pergunta


label segunda_pergunta:
    if pontos == 6:
        jump start
    entrevistadora "Vamos para a segunda pergunta. Por que você quer este trabalho? " 

    menu: 
        "Responder com desdém":
            $ pontos -= 30
            entrevistado "Essa pergunta é realmente importante?"
            jump terceira_pergunta
        "Responder com  dúvida":
            $ pontos -= 10
            entrevistado "Ainda não sei dizer."
            jump terceira_pergunta
        "Responder com educação":
            $ pontos += 20
            entrevistado "Acredito que vou adquirir bastante conhecimento nesta empresa"
            jump terceira_pergunta

label terceira_pergunta:
    entrevistadora "Agora que sabemos o motivo de sua bsuca por esse emprego, vamos a próxima pergunta.  Onde você se vê daqui a 5 anos?"
    menu:
        "Responder com arrogância":
            $ pontos -= 30
            entrevistado "bem longe daqui"

        "Responder com dúvida":
            $ pontos -= 10
            entrevistado "Ainda não pensei sobre isso."

        "Responder de forma convicente":
            $ pontos += 20
            entrevistado "Espero ter realizado uma faculdade, ter minha vida financeira estável, e com uma carreia brilhant em formação"


label quarta_pergunta:
    if pontos < 60:
        jump fora
    entrevistadora "Vamos prosseguir para próxima pergunta, quais são seus pontos fortes?"
    menu:
        "Desviar da pergunta":
            entrevistado "Invés disso, posso contar uma piada?"
            entrevistadora "Hmmm... acho melhor não."
            entrevistado "Eita..."
            $ pontos -= 20
        "Responder a pergunta":
            entrevistado "Sou muito prestativo, consigo trabalhar sobre pressão, organizado, pro atividade e comunicativo"
            $ pontos += 20
label quinta_pergunta:
    entrevistadora "Você gosta de trabalhar em equipe?"
    menu:
        "Sim":
            entrevistado "Me dou muito bem com pessoas, acredito que se todos se ajudarem nas tarefas solicitadas, isso pode trazer resultados positivos para a empresa."
            entrevistadora "Isso é bom de saber, temos varios times em nossa equipe, e trabalho em equipe é sempre um ponto forte"
            $ pontos += 30
        "Não":
            entrevistado "Não me dou bem com pessoas, prefiro trabalhar individualmente"
            $ pontos -= 30
label sexta_pergunta:
    entrevistadora "Vamos dar prólogo a próxima pergunta. Você está se candidatando a vagas em outras empresas?"
    menu:
        "Não":
            entrevistado "Na verdade não, vi essa vaga na internet e me interessei pela empresa e com os comentários externos, achei interessante me candidatar."
            $ pontos += 20
        "Sim":
            entrevistado "Estou sim, caso eu consiga a vaga, vou descartar as outras opções."
            $ pontos -= 20


label resultados:
    if pontos >= 100:
        jump parabens
    elif pontos <= 60:
        jump fora
    
label fora:
    if pontos < 60:
        entrevistadora "Tudo bem, coletamos todas as informações que precisavamos, retornaremos assim que possivel analisarmos todos seus dados por completo"
        "No final eles não me chamaram..."
        $ renpy.quit()

label parabens:
    entrevistadora "Meus parabéns! Essa vaga é sua. Você começa segunda-feira 10 da manha."


     

            
            
        

            