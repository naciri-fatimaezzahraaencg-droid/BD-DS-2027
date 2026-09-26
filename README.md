# Analyse : Facteurs freinant la croissance marocaine en 2027

Analyse basée sur le **Budget économique exploratoire 2027** du Haut-Commissariat au Plan (HCP), relayé par Medias24.

## Contexte

Selon le HCP, la croissance du PIB marocain devrait ralentir à **3,0%** en 2027, après **4,8%** en 2026, principalement en raison du retour à une campagne agricole moyenne après une année 2025-2026 exceptionnelle.

## Facteurs qui freinent la croissance en 2027

| Facteur | 2026 | 2027 | Pourquoi ça freine |
|---|---|---|---|
| Valeur ajoutée agricole | +19,1% | **-6,8%** | Chute nette, effet de base après récolte exceptionnelle |
| Investissement brut | +9,5% | +4,8% | Ralentissement net du rythme d'investissement |
| Déficit du compte courant | 3,9% du PIB | 3,6% du PIB | Reste élevé, pèse sur les réserves de change |
| Déficit budgétaire | 3,4% du PIB | 3,2% du PIB | Reste élevé, limite la marge budgétaire de l'État |
| Dette du Trésor | 65,8% du PIB | 65,2% du PIB | Niveau élevé, alourdit le service de la dette |
| **PIB réel (résultat global)** | +4,8% | +3,0% | Synthèse du ralentissement |

> **Note méthodologique** : les déficits et la dette affichent une légère amélioration en valeur, mais restent classés ici comme freins structurels car leurs niveaux demeurent élevés et continuent de contraindre les marges de manœuvre budgétaires et l'investissement.

## Facteurs qui soutiennent réellement la croissance en 2027

| Facteur | 2026 | 2027 |
|---|---|---|
| PIB non agricole | +3,3% | +4,2% |
| Taux d'investissement (% du PIB) | 35,2% | 35,3% |

## Contenu du dépôt

- `Facteurs_croissance_Maroc.xlsx` — tableaux Excel (2 feuilles : freins / soutiens) avec formules
- `graphique_croissance_maroc.py` — script Python (matplotlib) générant le graphique comparatif
- `croissance_maroc.png` — graphique généré

## Générer le graphique

```bash
pip install matplotlib numpy
python3 graphique_croissance_maroc.py
```

## Source

Haut-Commissariat au Plan (HCP), *Budget économique exploratoire 2027*, juillet 2026.
Relayé par [Medias24](https://medias24.com/2026/07/20/le-hcp-prevoit-une-croissance-de-3-en-2027-1725909/).
