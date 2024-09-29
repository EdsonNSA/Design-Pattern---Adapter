import json
import random

class Jogo:
    def __init__(self):
        self.jogadores = []
        self.territorios = ["Território1", "Território2", "Território3", "Território4", "Território5", "Território6"]
        self.objetivos = [
            "Conquistar 3 territórios",
            "Eliminar um jogador",
            "Conquistar 2 continentes",
            "Conquistar 18 territórios",
            "Conquistar 24 territórios",
            "Conquistar a Ásia e a América do Sul",
            "Conquistar a Europa, América do Sul e um terceiro continente",
            "Conquistar a América do Norte e a África"
        ]
        self.cartas = ["Infantaria", "Cavalaria", "Artilharia"]
        self.ordem_jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

    def definir_ordem_jogadores(self):
        self.ordem_jogadores = random.sample(self.jogadores, len(self.jogadores))

    def distribuir_territorios(self):
        random.shuffle(self.territorios)
        for i, jogador in enumerate(self.jogadores):
            jogador.receber_territorios(self.territorios[i::len(self.jogadores)])

    def distribuir_objetivos(self):
        for jogador in self.jogadores:
            jogador.receber_objetivo(random.choice(self.objetivos))

    def iniciar_rodada(self):
        for jogador in self.jogadores:
            jogador.distribuir_exercitos(5)

    def distribuir_cartas(self):
        for jogador in self.jogadores:
            jogador.cartas = random.choices(self.cartas, k=3)

    def gerar_json(self):
        dados = {
            "jogadores": [
                {
                    "nome": jogador.nome,
                    "cor": jogador.cor,
                    "objetivo": jogador.objetivo,
                    "territorios": jogador.territorios,
                    "exercitos": jogador.exercitos,
                    "cartas": jogador.cartas
                } for jogador in self.jogadores
            ]
        }
        return json.dumps(dados, indent=4)

class JogoAdapter:
    def __init__(self, jogo):
        self.jogo = jogo

    def gerar_json_adaptado(self):
        dados = {
            "game_players": [
                {
                    "player_name": jogador.nome,
                    "player_color": jogador.cor,
                    "target": jogador.objetivo,
                    "territories": jogador.territorios,
                    "armies": jogador.exercitos,
                    "cards": jogador.cartas
                } for jogador in self.jogo.jogadores
            ],
            "total_territories": len(self.jogo.territorios),
            "objectives": self.jogo.objetivos
        }
        return json.dumps(dados, indent=4)
