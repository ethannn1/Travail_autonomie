# Écrêtage des valeurs d'un tableau

def limite_amplitude(x, x_min, x_max):
   if x_min <= x <= x_max:
       return x
   elif x<x_min:
       return x_min
   return x_max
    

def ecrete(valeurs, x_min, x_max):
    valeurs_ecretees = []
    for v in valeurs:
        y = limite_amplitude(v, x_min, x_max)
        valeurs_ecretees.append(y)
    return valeurs_ecretees


# tests
valeurs = [34, 56, 89, 134, 152, 250, 87, -34, -187, -310]
attendu = [34, 56, 89, 134, 150, 150, 87, -34, -150, -150]
resultat = ecrete(valeurs, -150, 150)
assert attendu == resultat, f"Erreur avec ecrete({valeurs})"
