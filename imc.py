poids = 55 
taille = 1.68

imc = poids / (taille ** 2)

print(f"Votre IMC est de : {imc:.2f}")

if imc < 18.5:
    print("Catégorie : Insuffisance pondérale")
elif 18.5 <= imc < 25:
    print("Catégorie : Corpulence normale")
else:
    print("Catégorie : Surpoids")
