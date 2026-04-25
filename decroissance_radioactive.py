import matplotlib.pyplot as plt
import math

N0 = 1000 
lambda_const = 0.693  
temps = range(0, 10)  

# equation : N(t) = N0 * exp(-lambda * t)
populations = [N0 * math.exp(-lambda_const * t) for t in temps]

plt.plot(temps, populations, 'ro-')
plt.title("Décroissance radioactive")
plt.xlabel("Temps (jours)")
plt.ylabel("Nombre de noyaux")
plt.grid()
plt.show()
