from jogo import Jogo
from jogador import Jogador
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def iniciar_jogo():
    jogo = Jogo()
    jogador1 = Jogador("Edson", "Vermelho")
    jogador2 = Jogador("Marcelo", "Azul")
    jogador3 = Jogador("Pedro", "Verde")

    jogo.adicionar_jogador(jogador1)
    jogo.adicionar_jogador(jogador2)
    jogo.adicionar_jogador(jogador3)

    jogo.definir_ordem_jogadores()
    jogo.distribuir_territorios()
    jogo.distribuir_objetivos()
    jogo.iniciar_rodada()


    jogo.distribuir_cartas()


    with open('dados.json', 'w') as f:
        f.write(jogo.gerar_json())

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)