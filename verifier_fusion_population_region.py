import pandas as pd

# Charger les fichiers CSV
population = pd.read_csv('Population.csv')
region = pd.read_csv('region.csv')

# Normaliser les noms de pays (exemple simple)
population['Country'] = population['Country'].str.strip().str.lower()
region['Country'] = region['Country'].str.strip().str.lower()

# Fusionner les fichiers sur la colonne 'Country'
fusion_population_region = pd.merge(population, region, on='Country', how='inner')

# Trouver les pays dans 'population' qui n'ont pas été fusionnés
pays_non_fusionnes = population[~population['Country'].isin(fusion_population_region['Country'])]['Country'].unique()

# Vérifier si une partie du nom de 'Country' du fichier 'population' se retrouve dans les valeurs de 'Country' du fichier 'region'
correspondances_partielles = {}
for pays in pays_non_fusionnes:
    correspondances = region[region['Country'].str.contains(pays, na=False)]['Country'].unique()
    if correspondances.size > 0:
        correspondances_partielles[pays] = correspondances

# Enregistrer les correspondances partielles dans un fichier
with open('correspondances_partielles.txt', 'w') as f:
    for pays, correspondances in correspondances_partielles.items():
        f.write(f"{pays}: {', '.join(correspondances)}\n")
