import math

def calculer_tau(pKa, c):
    Ka = 10**(-pKa)
    a = 1
    b = Ka / c
    constante_c = -Ka / c

    delta = b**2 - 4 * a * constante_c
    
    tau = (-b + math.sqrt(delta)) / (2 * a)
    return tau

resultat = calculer_tau(pKa, c)
print(f"Le taux d'avancement est : {resultat:.4f}")
