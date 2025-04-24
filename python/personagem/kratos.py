import time
import random

class PersonagemGame:
    def __init__(self, nome, ranking, vida, força, guilda):
        self.nome = nome
        self.ranking = ranking
        self.vida = vida
        self.força = força
        self.guilda = guilda
        self.inventario = []
        self.defendendo = False

    def atacar(self, outro):
        dano_base = random.randint(int(self.força * 0.8), self.força)
        if outro.defendendo:
            dano = int(dano_base / 2)
            print(f"{outro.nome} defendeu! O dano foi reduzido para {dano}.")
        else:
            dano = dano_base
        print(f"{self.nome} ataca {outro.nome} causando {dano} de dano!")
        outro.vida -= dano
        if outro.vida < 0:
            outro.vida = 0

    def defender(self):
        self.defendendo = True
        print(f"{self.nome} está se defendendo neste turno!")

    def status(self):
        print(f"\n👤 Personagem: {self.nome}")
        print(f"🏆 Ranking: {self.ranking}")
        print(f"🏰 Guilda: {self.guilda}")
        print(f"❤️ Vida: {self.vida}")
        print(f"💪 Força: {self.força}")
        print(f"🎒 Inventário: {self.inventario}")

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

# Criando personagens
samurai = PersonagemGame("Hiroshi", "Surreal", 110, 23, "Samurais Extintos")
spartano = PersonagemGame("Kratos", "Diamante", 120, 21, "Destruidores")

# Adicionando itens
samurai.inventario.extend(["Katana Lendária", "Furos de estiragem"])
spartano.inventario.extend(["Lâminas do Caos", "Os Olhos da Verdade"])

# Status inicial
print("🏁 Status Inicial dos Combatentes 🏁")
samurai.status()
spartano.status()

# Iniciar batalha
batalha_interativa(samurai, spartano)
