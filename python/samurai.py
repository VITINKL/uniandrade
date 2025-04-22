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

    def atacar(self, outro):
        dano = random.randint(int(self.força * 0.8), self.força)
        print(f"{self.nome} da guilda {self.guilda} ataca {outro.nome} causando {dano} de dano!")
        outro.vida -= dano
        if outro.vida < 0:
            outro.vida = 0

    def status(self):
        print(f"\n👤 Personagem: {self.nome}")
        print(f"🏆 Ranking: {self.ranking}")
        print(f"🏰 Guilda: {self.guilda}")
        print(f"❤️ Vida: {self.vida}")
        print(f"💪 Força: {self.força}")
        print(f"🎒 Inventário: {self.inventario}")

def batalha(p1, p2):
    print("\n⚔️ BATALHA ENTRE GUILDAS ⚔️")
    rodada = 1
    while p1.vida > 0 and p2.vida > 0:
        print(f"\n--- Rodada {rodada} ---")
        if rodada % 2 == 1:
            p1.atacar(p2)
        else:
            p2.atacar(p1)
        time.sleep(1)  # Dá emoção à batalha
        p1.status()
        p2.status()
        rodada += 1

    print("\n🏁 Fim da batalha!")
    vencedor = p1 if p1.vida > 0 else p2
    print(f"🎉 {vencedor.nome} da guilda {vencedor.guilda} venceu a batalha!")

# Criando os personagens com guilda e ranking
samurai = PersonagemGame("Hiroshi", "Surreal", 110, 23, "Samurais Extintos")
spartano = PersonagemGame("Kratos", "Diamante", 120, 21, "Destruidores")

# Adicionando itens ao inventário
samurai.inventario.extend(["Katana Lendária", "Poção de Cura"])
spartano.inventario.extend(["Lança Dourada", "Escudo de Esparta"])

# Status inicial
print("🏁 Status Inicial dos Combatentes 🏁")
samurai.status()
spartano.status()

# Iniciar batalha
batalha(samurai, spartano)
