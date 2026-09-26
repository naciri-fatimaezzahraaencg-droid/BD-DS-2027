"""
Graphique : Facteurs freinant/soutenant la croissance marocaine 2026-2027
Source : HCP (Haut-Commissariat au Plan) - Budget économique exploratoire 2027, via Medias24

Reclassement (avis utilisateur) : les déficits (compte courant, budgétaire) et la dette du
Trésor restent des freins structurels malgré une légère amélioration, car leurs niveaux
demeurent élevés et continuent de peser sur les marges de manoeuvre de l'économie.
"""
import matplotlib.pyplot as plt
import numpy as np

# --- Facteurs qui FREINENT la croissance en 2027 ---
freins = [
    "VA agricole",
    "Investissement brut",
    "Déficit compte\ncourant (% PIB)",
    "Déficit budgétaire\n(% PIB)",
    "Dette du Trésor\n(% PIB)",
    "PIB réel (global)",
]
freins_2026 = [19.1, 9.5, 3.9, 3.4, 65.8, 4.8]
freins_2027 = [-6.8, 4.8, 3.6, 3.2, 65.2, 3.0]

# --- Facteurs qui SOUTIENNENT réellement la croissance ---
soutiens = [
    "PIB non agricole",
    "Taux d'investissement\n(% du PIB)",
]
soutiens_2026 = [3.3, 35.2]
soutiens_2027 = [4.2, 35.3]

fig, axes = plt.subplots(1, 2, figsize=(15, 6))
width = 0.35

# Graphique 1 : Freins
x1 = np.arange(len(freins))
axes[0].bar(x1 - width/2, freins_2026, width, label="2026", color="#2E86AB")
axes[0].bar(x1 + width/2, freins_2027, width, label="2027", color="#C0392B")
axes[0].axhline(0, color="black", linewidth=0.8)
axes[0].set_xticks(x1)
axes[0].set_xticklabels(freins, fontsize=9)
axes[0].set_ylabel("Valeur (%)")
axes[0].set_title("Facteurs qui FREINENT la croissance en 2027")
axes[0].legend()
for i, (a, b) in enumerate(zip(freins_2026, freins_2027)):
    axes[0].text(i - width/2, a + (1.5 if a >= 0 else -3), f"{a}%", ha="center", fontsize=8, fontweight="bold")
    axes[0].text(i + width/2, b + (1.5 if b >= 0 else -3), f"{b}%", ha="center", fontsize=8, fontweight="bold")

# Graphique 2 : Soutiens
x2 = np.arange(len(soutiens))
axes[1].bar(x2 - width/2, soutiens_2026, width, label="2026", color="#2E86AB")
axes[1].bar(x2 + width/2, soutiens_2027, width, label="2027", color="#27AE60")
axes[1].set_xticks(x2)
axes[1].set_xticklabels(soutiens, fontsize=9)
axes[1].set_ylabel("Valeur (%)")
axes[1].set_title("Facteurs qui SOUTIENNENT la croissance en 2027")
axes[1].legend()
axes[1].set_xlim(-0.6, len(soutiens) - 0.4)
for i, (a, b) in enumerate(zip(soutiens_2026, soutiens_2027)):
    axes[1].text(i - width/2, a + 0.8, f"{a}%", ha="center", fontsize=8, fontweight="bold")
    axes[1].text(i + width/2, b + 0.8, f"{b}%", ha="center", fontsize=8, fontweight="bold")

plt.suptitle("Croissance marocaine 2027 : freins vs soutiens (Source : HCP)", fontsize=13, fontweight="bold")
plt.tight_layout()
plt.savefig("/mnt/user-data/outputs/croissance_maroc.png", dpi=150)
print("Graphique enregistré avec succès.")
