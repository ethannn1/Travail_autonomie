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

def inverse_chaine(chaine):
    resultat = ""
    for caractere in chaine:
        resultat = caractere + resultat
    return resultat

def est_palindrome(chaine):
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_palindromique(nombre):
    chaine = str(nombre)
    return est_palindrome(chaine)


# tests

assert inverse_chaine('bac') == 'cab'

assert not est_palindrome('NSI')

assert est_palindrome('ISN-NSI')

assert not est_palindromique(214312)

assert est_palindromique(213312)
