


## FICHIER mortalite
# Charger les fichiers CSV
mortalite = pd.read_csv('MortalityRateAttributedToWater.csv')

# Uniformiser les noms de colonnes
mortalite.rename(columns={'Country': 'Country', 'Year': 'Year'}, inplace=True)

# Gérer les valeurs manquantes
mortalite.fillna(0, inplace=True)

# Supprimer les doublons
mortalite.drop_duplicates(inplace=True)

# Convertir les types de données
mortalite['Year'] = mortalite['Year'].astype(int)

# Normaliser les noms de pays (exemple simple)
mortalite['Country'] = mortalite['Country'].str.strip().str.lower()

#jointure des deux fichiers sur la colonne Country, year et Granularity
df_final = df_final.merge(mortalite, on=['Country', 'Year', 'Granularity'], how='left')
#Dans le fichier mortalité je n'ai qu'une seule année de répertoriée et seulement 3 niveaux de granularité
#Je fais un left join pour ne pas perdre les informations de population des pays qui n'ont pas de données de mortalité

## FICHIER acces_potable
# Charger les fichiers CSV

acces_potable = pd.read_csv('BasicAndSafelyManagedDrinkingWaterServices.csv')

# Uniformiser les noms de colonnes
acces_potable.rename(columns={'Country': 'Country', 'Year': 'Year'}, inplace=True)

# Gérer les valeurs manquantes
acces_potable.fillna(0, inplace=True)

# Supprimer les doublons
acces_potable.drop_duplicates(inplace=True)

# Convertir les types de données
acces_potable['Year'] = acces_potable['Year'].astype(int)

# Normaliser les noms de pays (exemple simple)
acces_potable['Country'] = acces_potable['Country'].str.strip().str.lower()

#jointure des deux fichiers sur la colonne Country, year et Granularity
df_final = df_final.merge(acces_potable, on=['Country', 'Year', 'Granularity'], how='left')
#Dans le fichier acces_potable il manque une année par rapport au fichier joint précédemment
#Je fais un left join pour ne pas perdre les informations des pays qui n'ont pas de données d'accès à l'eau potable

## FICHIER political_stability
# Charger les fichiers CSV
political_stability = pd.read_csv('PoliticalStability.csv')

# Uniformiser les noms de colonnes
political_stability.rename(columns={'Country': 'Country', 'Year': 'Year'}, inplace=True)

# Gérer les valeurs manquantes
political_stability.fillna(0, inplace=True)

# Supprimer les doublons
political_stability.drop_duplicates(inplace=True)

# Convertir les types de données
political_stability['Year'] = political_stability['Year'].astype(int)

# Normaliser les noms de pays (exemple simple)
political_stability['Country'] = political_stability['Country'].str.strip().str.lower()

#jointure des deux fichiers sur la colonne Country, year et Granularity
df_final = df_final.merge(political_stability, on=['Country', 'Year', 'Granularity'], how='left')
#Dans le fichier political_stability il manque 2 valeurs de granularity par rapport au fichier joint précédemment
#Je fais un left join pour ne pas perdre les informations des pays qui n'ont pas de données de stabilité politique

#convertir le fichier final en csv
# df_final.to_csv('df_finalbis.csv', index=False)
# print('Fusion terminée')




