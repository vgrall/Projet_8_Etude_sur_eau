import pandas as pd


# Charger les fichiers CSV
mortalite = pd.read_csv('mortalite.csv')
region = pd.read_csv('regionweb.csv') #issue du site https://www.geograf.in/fr/table.php et https://www.business-plan-excel.fr/liste-pays-du-monde-excel-capitale-continent/
population = pd.read_csv('Population.csv')
acces_potable = pd.read_csv('accesPotable.csv')
political_stability = pd.read_csv('PoliticalStability.csv')

# Uniformiser les noms de colonnes
mortalite.rename(columns={'Country': 'Country', 'Year': 'Year'}, inplace=True)
region.rename(columns={'Country': 'Country'}, inplace=True)  # Garder la colonne 'region' en minuscule
population.rename(columns={'Country': 'Country', 'Year': 'Year'}, inplace=True)
acces_potable.rename(columns={'Country': 'Country', 'Year': 'Year'}, inplace=True)
political_stability.rename(columns={'Country': 'Country', 'Year': 'Year'}, inplace=True)


# Gérer les valeurs manquantes
mortalite.fillna(0, inplace=True)
region.fillna(0, inplace=True)
population.fillna(0, inplace=True)
acces_potable.fillna(0, inplace=True)
political_stability.fillna(0, inplace=True)

# Supprimer les doublons
mortalite.drop_duplicates(inplace=True)
region.drop_duplicates(inplace=True)
population.drop_duplicates(inplace=True)
acces_potable.drop_duplicates(inplace=True)
political_stability.drop_duplicates(inplace=True)

# Convertir les types de données
mortalite['Year'] = mortalite['Year'].astype(int)
population['Year'] = population['Year'].astype(int)
acces_potable['Year'] = acces_potable['Year'].astype(int)
political_stability['Year'] = political_stability['Year'].astype(int)

# Normaliser les noms de pays (exemple simple)
mortalite['Country'] = mortalite['Country'].str.strip().str.lower()
region['Country'] = region['Country'].str.strip().str.lower()
population['Country'] = population['Country'].str.strip().str.lower()
acces_potable['Country'] = acces_potable['Country'].str.strip().str.lower()
political_stability['Country'] = political_stability['Country'].str.strip().str.lower()

# Vérifier que la colonne 'region' existe dans le DataFrame 'region'
if 'region' not in region.columns:
    raise KeyError("La colonne 'region' n'existe pas dans le DataFrame 'region'")

# Fusionner les fichiers sur les colonnes communes 'Country' et 'Year'
df_final = population.merge(region, on='Country', how='outer')
#Resultat, un fichier qui répertorie les continents par pays avec leur population
#il y a des lignes sans population ni granularité car n'existaient pas dans le fichier region initial
#Compter le nombre de ligne sans population ni granularité
df_final['Population'].isnull().sum()
#afficher le nombre de ligne sans population ni granularité
#print(df_final['Population'].isnull().sum())
#supprimer les lignes sans population ni granularité
df_final = df_final.dropna(subset=['Population'])





# df_final = df_final.merge(population, on=['Country', 'Year', 'Granularity'], how='outer')
# df_final.to_excel('donnees_fusionnees.xlsx', index=False)
# df_final = df_final.merge(acces_potable, on=['Country', 'Year'], how='outer')
# df_final = df_final.merge(political_stability, on=['Country', 'Year'], how='outer')

# # Enregistrer le fichier fusionné
# df_final.to_csv('donnees_fusionnees.csv', index=False)
