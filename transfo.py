import pandas as pd



# Charger le fichier contenant les années en colonnes
df = pd.read_csv("donneeBanqueMondialeDensite.csv")  # Remplace par ton fichier

df_melted = df.melt(id_vars=["Country FR", "Country", "Indicator Name"], 
                     var_name="Year", 
                     value_name="Value")

# Convertir l'année en entier (optionnel)
df_melted["Year"] = df_melted["Year"].astype(int)

#df_melted.to_csv("densite.csv", index=False)  # Remplace par le nom de ton fichier
