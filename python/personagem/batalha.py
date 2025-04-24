import time
from personagem import PersonagemGame

def turno_jogador(jogador, oponente):
    print(f"\n🔁 Turno de {jogador.nome} ({jogador.guilda})")
    print("Escolha sua ação:")
    print("1 - Atacar")
    print("2 - Defender")
    escolha = input("Digite o número da ação: ")

    jogador.defendendo = False  # resetar defesa a cada turno

    if escolha == "1":
        jogador.atacar(oponente)
    elif escolha == "2":
        jogador.defender()
    else:
        print("Ação inválida! Você perdeu o turno.")

def batalha_interativa(p1, p2):
    print("\n⚔️ BATALHA INTERATIVA ENTRE GUILDAS ⚔️")
    input("Pressione ENTER para começar a batalha...")

    rodada = 1
    while p1.vida > 0 and p2.vida > 0:
        print(f"\n--- Rodada {rodada} ---")
        if rodada % 2 == 1:
            turno_jogador(p1, p2)
        else:
            turno_jogador(p2, p1)
        time.sleep(1)
        p1.status()
        p2.status()
        rodada += 1

    print("\n🏁 Fim da batalha!")
    vencedor = p1 if p1.vida > 0 else p2
    print(f"🎉 {vencedor.nome} da guilda {vencedor.guilda} venceu a batalha!")
