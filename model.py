class Habilidade:
    def __init__(self, nome):
        self._nome = nome
        self._xp = 0
        self._nivel = 0
        self._tarefas = None
    
    def alterar_nome(self, nome):
        self._nome = nome

    def iniciar_xp(self, xp_inicial):
        self._xp = xp_inicial

    def calcular_nivel(self, xp):
        nivel = 0
        for i in range(1, 11):
            if xp >= 10*2**i:
                nivel += 1
            else:
                break
        self._nivel = nivel
    
    def nova_tarefa(self, nome, data, tempo_hr):
        self._xp += tempo_hr

def niveis_em_pontos():
    niveis = list()
    for i in range(1, 11):
        niveis.append(10*2**i)