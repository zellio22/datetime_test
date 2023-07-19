from datetime import datetime

# Supposons que vous avez un timestamp représentant une date
timestamp = 1678912345  # Remplacez ceci par votre timestamp réel

# Convertir le timestamp en objet datetime
ma_date = datetime.fromtimestamp(timestamp)
print(type(ma_date))
print(ma_date)

# Afficher la date sous forme de chaîne de caractères (str)
format_date = ma_date.strftime("%Y-%m-%d %H:%M:%S")#concatenation on peux ajouter dutexte ici
print(type(format_date))
print(format_date)#2023-03-15 21:32:25

# Convertir de datetime a str
ma_date = datetime.strptime(format_date, "%Y-%m-%d %H:%M:%S") #tu parce ici 
print(type(ma_date))
print(ma_date)
