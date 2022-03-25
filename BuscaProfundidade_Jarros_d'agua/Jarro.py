class Jarros:
    def __init__(self, x, y):
        self.x = x  # Jarro 1
        self.y = y  # Jarro 2
        self.profundidade = 0
        self.caminho = []  # Armazena os caminhos percorridos
        self.pilha = []  # Armazena nós não percorridos temporariamente
        self.vertice = []  # Armazena temporariamente vértices que podem ser gerados em um nó

    '''Função responsável por executar a lógica de inserção de um caminho'''

    def register(self, x, y):
        if [x, y] not in self.caminho and [x, y] not in self.pilha:
            self.vertice.append([x, y])

            # O primeiro vertice de um nó será o próximo a ser analisado
            if len(self.vertice) == 1:
                self.x = x
                self.y = y

                self.caminho.append([x, y])

                return False  # Novo caminho

            # Outros vertices que surgirem no nó será armazenado para futuro caminho caso não exista mais caminhos (sem saída) a percorrer
            self.pilha.append([x, y])

            return False  # Novo caminho
        else:
            return True  # Um caminho de [x, y] já foi percorrido

    '''Função responsável por definir o objetivo'''

    def defineGoal(self, x, y):
        self.caminho.append([self.x, self.y])  # Caminho inicial [0, 0]

        while True:

            if x == self.x and y == self.y:
                print('')
                print("🚀 Finalizou 🚀")
                print('')
                print(f'Caminho: {self.caminho}')
                break
            else:
                self.defineRules(self.x, self.y)

    ''' Função responsável por aplicar as regras determinadas no exercício do Jarro d'água. '''

    def defineRules(self, x, y):
        include = []  # Armazena se o caminho é repetido ou não

        print('')
        print('------------------|')
        print(f'Aplicando: {x, y} |')
        print('------------------|')

        if x < 3:
            repeated = self.register(3, y)  # Regra R1
            include.append(repeated)
            if not repeated:
                print('## R1 ##')

        if y < 4:
            repeated = self.register(x, 4)  # Regra R2
            include.append(repeated)
            if not repeated:
                print('## R2 ##')

        if x > 0:
            repeated = self.register(0, y)  # Regra R3
            include.append(repeated)
            if not repeated:
                print('## R3 ##')

        if y > 0:
            repeated = self.register(x, 0)  # Regra R4
            include.append(repeated)
            if not repeated:
                print('## R4 ##')

        if y > 0 and (x + y) <= 3:
            repeated = self.register(x + y, 0)  # Regra R5
            include.append(repeated)
            if not repeated:
                print('## R5 ##')

        if y > 0 and (x + y) > 3:
            repeated = self.register(3, y - (3 - x))  # Regra R6
            include.append(repeated)
            if not repeated:
                print('## R6 ##')

        if x > 0 and (x + y) <= 4:
            repeated = self.register(0, x + y)  # Regra R7
            include.append(repeated)
            if not repeated:
                print('## R7 ##')

        if x > 0 and (x + y) > 4:
            repeated = self.register(x - (4 - y), 4)  # Regra R8
            include.append(repeated)
            if not repeated:
                print('## R8 ##')

        print('')
        print(f'Fim da profundidade {self.profundidade}')

        # Se todos os nós gerados forem iguais a pelo menos um nó que já foi feito caminho, não existirá uma nova ramificação
        noRemification = all(x == True for x in include)

        include = []

        # Zera os vértices analisados de um nó. Partindo para o próximo nó...
        self.vertice = []

        if noRemification:
            print('')
            print('Não há ramificações')
            # Pega o último vértice que não foi percorrido, caso não exista mais ramificações no nó.
            [self.x, self.y] = self.pilha.pop()
            # Adiciona no caminho já que estará sendo percorrido
            self.caminho.append([self.x, self.y])

            return

        self.profundidade += 1  # Aumenta o nível de profundidade da árvore
