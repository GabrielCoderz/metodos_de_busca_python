class Jarros:
    def __init__(self, x, y):
        self.x = x  # Jarro 1
        self.y = y  # Jarro 2
        self.caminho = []  # Armazena os caminhos percorridos

    '''Função responsável por executar a lógica de inserção de um caminho'''

    def register(self, x, y):
        if [x, y] not in self.caminho:

            self.x = x
            self.y = y

            self.caminho.append([x, y])

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
                return

        if y < 4:
            repeated = self.register(x, 4)  # Regra R2
            include.append(repeated)
            if not repeated:
                print('## R2 ##')
                return

        if x > 0:
            repeated = self.register(0, y)  # Regra R3
            include.append(repeated)
            if not repeated:
                print('## R3 ##')
                return

        if y > 0:
            repeated = self.register(x, 0)  # Regra R4
            include.append(repeated)
            if not repeated:
                print('## R4 ##')
                return

        if y > 0 and (x + y) <= 3:
            repeated = self.register(x + y, 0)  # Regra R5
            include.append(repeated)
            if not repeated:
                print('## R5 ##')
                return

        if y > 0 and (x + y) > 3:
            repeated = self.register(3, y - (3 - x))  # Regra R6
            include.append(repeated)
            if not repeated:
                print('## R6 ##')
                return

        if x > 0 and (x + y) <= 4:
            repeated = self.register(0, x + y)  # Regra R7
            include.append(repeated)
            if not repeated:
                print('## R7 ##')
                return

        if x > 0 and (x + y) > 4:
            repeated = self.register(x - (4 - y), 4)  # Regra R8
            include.append(repeated)
            if not repeated:
                print('## R8 ##')
                return
