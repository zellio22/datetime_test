from datetime import datetime

# Supposons que vous avez deux objets datetime représentant les deux dates
date1 = datetime(2021, 10, 5, 15, 30)
date2 = datetime(2021, 10, 2, 15, 45)

# Calculer l'écart entre les deux dates en utilisant la soustraction
ecart = date2 - date1
print(type(ecart))
# Afficher l'écart sous forme de chaîne de caractères (str)
print(ecart)
#afficher l'ecart en STR formaté
