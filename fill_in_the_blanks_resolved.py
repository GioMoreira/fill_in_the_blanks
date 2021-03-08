data = {
    'facil': {
        'frase': "Um __0__ passo para um __1__ , um __2__ salto para __3__",
        'chances': 3,
        'respostas': ['pequeno', 'homem', 'grande', 'humanidade']
    },
    'medio': {
        'frase': "Seja a __0__ que __1__ deseja __2__ no __3__",
        'chances': 3,
        'respostas': ['mudança', 'voce', 'ver', 'mundo']
    },
    'dificil': {
        'frase': "Talvez a maior __0__ da __1__ seja que __2__ aprendeu as __3__ da __4__",
        'chances': 3,
        'respostas': ['licao', 'historia', 'ninguem', 'licoes', 'historia']
    }
}


def selecionar_nivel():
    while True:
        nivel = input('Escolha o nível: ( fácil | médio | difícil) --> ').lower()
        if nivel in data:
            return nivel
        print("Nível não existente. Tente de novo!")


def jogo():
    nivel = selecionar_nivel()
    frase = data[nivel]['frase']
    respostas = data[nivel]['respostas']
    chances = data[nivel]['chances']
    lacuna_respondida = 0
    print(f'Você escolheu o nível {nivel} e sua frase é:\n{frase}')
    while chances > 0 and lacuna_respondida < len(respostas):
        resposta_user = str(input(f'Qual a resposta da lacuna {lacuna_respondida}: '))
        if resposta_user == respostas[lacuna_respondida]:
            print('Correto!!')
            if lacuna_respondida == len(respostas) - 1:
                print('VOCÊ GANHOU!!')
            lacuna_respondida += 1
        else:
            chances -= 1
            if chances == 0:
                print('Você perdeu! :( ')
            else:
                print(f'Errado! Agora você tem {chances} chance.')


jogo()
