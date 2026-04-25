population_totale = 1000
S = 999  
I = 1    
R = 0    


taux_infection = 0.3  
taux_guerison = 0.1    
dt = 1                

print("Jour | Sains | Infectés | Guéris")
print("-" * 30)

for jour in range(50):
    
    nouveaux_malades = (taux_infection * S * I) / population_totale
    nouveaux_gueris = taux_guerison * I
    
  
    S = S - nouveaux_malades
    I = I + nouveaux_malades - nouveaux_gueris
    R = R + nouveaux_gueris
    
    if jour % 5 == 0:
        print(f"{jour:4} | {int(S):5} | {int(I):8} | {int(R):6}")
