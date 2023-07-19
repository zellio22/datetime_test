from datetime import datetime

date_str = "2023-ju03-15 _bite_21:32:25"

# Convertir la chaîne de caractères en objet datetime en utilisant strptime
ma_date = datetime.strptime(date_str, "%Y-ju%m-%d _bite_%H:%M:%S") #tu parce ici 
print(type(ma_date))
# Afficher la date en tant qu'objet datetime
print(f"La date en tant qu'objet datetime est : {ma_date}")