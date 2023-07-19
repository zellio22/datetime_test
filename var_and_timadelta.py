from datetime import datetime, timedelta

# Supposons que vous avez les variables suivantes représentant la date
annee_str = "2021"
mois_str = "10"
jour_str = "1"
heure_str = "12"
minute_str = "30"

# Convertir les variables en objets de type int
annee = int(annee_str)
mois = int(mois_str)
jour = int(jour_str)
heure = int(heure_str)
minute = int(minute_str)

# Créer l'objet de type date en utilisant la méthode datetime
ma_date = datetime(annee, mois, jour, heure, minute)

# Ajouter 10 heures à la date en utilisant timedelta
nouvelle_date = ma_date + timedelta(hours=10)

# Afficher la nouvelle date
print(nouvelle_date)
