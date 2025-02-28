import pandas as pd

# Charger les fichiers CSV UNSD
region = pd.read_csv('UNSD.csv')
# Supprimer la colonne 'Sub-region Name'
region.drop('Sub-region Name', axis=1, inplace=True)
# Supprimer les doublons
region.drop_duplicates(inplace=True)
# Normaliser les noms de pays
region['Country'] = region['Country'].str.strip().str.lower()

# Lire le fichier RegionCountry.csv 
regionOC = pd.read_csv('RegionCountry.csv')
# Renommer et normaliser les colonnes
regionOC.rename(columns={'REGION (DISPLAY)': 'region'}, inplace=True)
regionOC['Country'] = regionOC['Country'].str.strip().str.lower()
# Effectuer une jointure (merge) sur 'Country' en mode OUTER pour récupérer toutes les données
merged_df = pd.merge(region, regionOC, on='Country', how='outer', suffixes=('_region', '_oc'))
# Prioriser la région de regionOC si elle existe
merged_df['region'] = merged_df['region_oc'].combine_first(merged_df['region_region'])
# Supprimer les colonnes temporaires
merged_df = merged_df[['Country', 'region']]

# Charger le fichier densite
densite = pd.read_csv('densite.csv')
# Uniformiser les noms de colonnes
densite.rename(columns={'Country': 'Country', 'Year': 'Year', 'Value': 'Densite'}, inplace=True)
# Gérer les valeurs manquantes
densite.fillna(0, inplace=True)
# Supprimer les doublons inutiles
densite.drop_duplicates(inplace=True)
# Convertir les types de données
densite['Year'] = densite['Year'].astype(int)
# Normaliser les noms de pays
densite['Country'] = densite['Country'].str.strip().str.lower()
# Garder uniquement la valeur maximale pour chaque combinaison (Country, Year)
densite = densite.groupby(['Country', 'Year'], as_index=False).agg({'Densite': 'max'})
# Jointure des deux fichiers sur la colonne Country
merged_df = pd.merge(merged_df, densite, on='Country', how='left')


## FICHIER Population
# Charger les fichiers CSV
population = pd.read_csv('Population.csv')
# Uniformiser les noms de colonnes
population.rename(columns={'Country': 'Country', 'Year': 'Year'}, inplace=True)
# Gérer les valeurs manquantes
population.fillna(0, inplace=True)
# Supprimer les doublons
population.drop_duplicates(inplace=True)
# Convertir les types de données
population['Year'] = population['Year'].astype(int)
# Normaliser les noms de pays (exemple simple)
population['Country'] = population['Country'].str.strip().str.lower()
#jointure des deux fichiers sur la colonne Country
df_final = population.merge(merged_df, on=['Country', 'Year'], how='left')
#Etant donné que j'ai plus de pays dans le fichier region qui provient d'une source externe, je fais un left join 
# pour ne garder que les pays qui existent dans le fichier population


# Dictionnaire des régions à attribuer pour chaque pays selon la classification M49 des Nations Unies
region_dict = {
    "sudan (former)": "Northern Africa",
    "channel islands": "Northern Europe",
    "china, hong kong sar": "Eastern Asia",
    "china, macao sar": "Eastern Asia",
    "china, mainland": "Eastern Asia",
    "china, taiwan province of": "Eastern Asia",
    "french guyana": "South America",
    "netherlands antilles (former)": "Caribbean",
    "palestine": "Western Asia",
    "saint helena, ascension and tristan da cunha": "Sub-Saharan Africa",
    "saint-martin (french part)": "Caribbean",
    "serbia and montenegro": "Southern Europe",
    "sint maarten (dutch part)": "Caribbean"
}

# Normalisation des noms de pays dans df_final
df_final['Country'] = df_final['Country'].str.strip().str.lower()
# Remplir les valeurs manquantes dans la colonne 'region' en utilisant le dictionnaire
df_final['region'] = df_final.apply(
    lambda row: region_dict.get(row['Country'], row['region']), axis=1)
# Assurez-vous qu'il n'y a pas de valeurs manquantes restantes
# Si une valeur dans 'region' est toujours manquante, on peut lui attribuer une valeur par défaut, par exemple 'Unknown'
df_final['region'].fillna('Unknown', inplace=True)
# Renommer la colonne region en continent
df_final.rename(columns={'region': 'Region_Continent'}, inplace=True)

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

print(df_final.columns)

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
df_final.to_csv('PIVOT.csv', index=False)
print('Fusion terminée')