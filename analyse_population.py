import pandas as pd

# Importer le fichier de données
population = pd.read_csv('Population.csv')

# Créer un fichier pour enregistrer les résultats
with open('resultats_analyse_population.txt', 'w') as f:
    # Vérifier les types de données dans chaque colonne
    f.write("Types de données dans 'population':\n")
    f.write(str(population.dtypes) + "\n\n")
    
    # Vérifier les valeurs manquantes
    f.write("Valeurs manquantes dans 'population':\n")
    f.write(str(population.isnull().sum()) + "\n\n")
    
    # Afficher les 10 premières lignes
    f.write("Les 10 premières lignes de 'population':\n")
    f.write(str(population.head(10)) + "\n\n")
    
    # Nombre de pays
    f.write("Nombre de pays:\n")
    f.write(str(population['Country'].nunique()) + "\n\n")
    
    # Nombre de valeurs différentes dans la colonne 'Granularity'
    f.write("Nombre de valeurs différentes dans 'Granularity':\n")
    f.write(str(population['Granularity'].nunique()) + "\n\n")
    
    # Statistiques descriptives
    f.write("Statistiques descriptives:\n")
    f.write(str(population.describe()) + "\n\n")
    
    # Analyser les valeurs uniques et doublons
    f.write("Nombre de valeurs uniques dans 'Country':\n")
    f.write(str(population['Country'].nunique()) + "\n\n")
    f.write("Nombre de doublons:\n")
    f.write(str(population.duplicated().sum()) + "\n\n")
