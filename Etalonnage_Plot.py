import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. DONNÉES EXPÉRIMENTALES BRUTES 
# =============================================================================
angles = np.linspace(0, 30, 26)  # Vecteur d'angle de 0° à 50° par pas de 2°

brut_C3C4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 17, 36, 53, 56, 62, 70, 79, 80, 79, 82, 103, 84]
brut_C5C6 = [0, 0, 0, 0, 0, 33, 98, 140, 232, 247, 297, 322, 330, 358, 393, 388, 430, 470, 485, 491, 512, 520, 533, 560, 539, 530]

# =============================================================================
# 2. LOI D'ÉTALONNAGE 
# =============================================================================
def loi_etalonnage(X):
    A = 0.000312
    B = 0.016021
    C = -0.053437
    
    # Le polynôme donne un résultat en grammes
    masse_grammes = A * (np.array(X) ** 2) + B * np.array(X) + C
    
    # On convertit en kilogrammes pour la formule P = F/S
    masse_kg = masse_grammes / 1000.0
    
    return np.clip(masse_kg, 0.0, None)
masse_C3C4 = loi_etalonnage(brut_C3C4)
masse_C5C6 = loi_etalonnage(brut_C5C6)

# =============================================================================
# 3. CONVERSION PHYSIQUE EN PRESSION (MPa)
# =============================================================================
rayon_mm = 2.0
rayon_m = rayon_mm / 1000.0  # Conversion en mètres
surface_m2 = np.pi * (rayon_m ** 2)  # S = pi * r^2
g = 9.81  # Accélération de la pesanteur (m/s^2)

# Calcul de la pression : P = (M * g) / S
# On divise par 1e6 à la fin pour passer de Pascals (Pa) à MegaPascals (MPa)
pression_C3C4_MPa = (masse_C3C4 * g) / surface_m2 / 1e6
pression_C5C6_MPa = (masse_C5C6 * g) / surface_m2 / 1e6

# =============================================================================
# 4. GÉNÉRATION DU GRAPHIQUE
# =============================================================================
plt.figure(figsize=(10, 6))

# Tracé pour le segment supérieur C3-C4
plt.plot(angles, pression_C3C4_MPa, color='blue', marker='o', linestyle='-', linewidth=2, label='Segment supérieur C3-C4')

# Tracé pour le segment inférieur C5-C6
plt.plot(angles, pression_C5C6_MPa, color='red', marker='s', linestyle='-', linewidth=2, label='Segment inférieur C5-C6')

# Configuration des axes et titres
plt.title("Évolution de la pression intradiscale locale en fonction de l'angle de flexion", fontsize=12, fontweight='bold')
plt.xlabel("Angle de flexion θ (degrés)", fontsize=10)
plt.ylabel("Pression mécanique (MPa)", fontsize=10)

# Mise en forme
plt.xlim(-2, 30)
plt.ylim(-0.005, max(max(pression_C3C4_MPa), max(pression_C5C6_MPa)) * 1.1)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', fontsize=10)

# Affichage du rendu final
plt.show()