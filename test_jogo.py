import unittest
from jogo import Jogo, JogoAdapter
from jogador import Jogador

class TestJogoAdapter(unittest.TestCase):
    def test_gerar_json_adaptado(self):
        jogo = Jogo()
        jogador1 = Jogador("Marcelo", "vermelho")
        jogador2 = Jogador("Pedro", "azul")
        jogador3 = Jogador("Edson", "verde")
        jogo.adicionar_jogador(jogador1)
        jogo.adicionar_jogador(jogador2)
        jogo.adicionar_jogador(jogador3)
        jogo.distribuir_territorios()
        jogo.distribuir_objetivos()
        
        adapter = JogoAdapter(jogo)
        json_adaptado = adapter.gerar_json_adaptado()
        
        self.assertIn("game_players", json_adaptado)
        self.assertIn("total_territories", json_adaptado)
        self.assertIn("objectives", json_adaptado)

if __name__ == '__main__':
    unittest.main()
