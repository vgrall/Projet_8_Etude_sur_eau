import pandas as pd

# Importer le fichier de données
region = pd.read_csv('region.csv')

# Créer un fichier pour enregistrer les résultats
with open('resultats_analyse_region.txt', 'w') as f:
    # Vérifier les types de données dans chaque colonne
    f.write("Types de données dans 'region':\n")
    f.write(str(region.dtypes) + "\n\n")
    
    # Vérifier les valeurs manquantes
    f.write("Valeurs manquantes dans 'region':\n")
    f.write(str(region.isnull().sum()) + "\n\n")
    
    # Afficher les 10 premières lignes
    f.write("Les 10 premières lignes de 'region':\n")
    f.write(str(region.head(10)) + "\n\n")
    
    # Nombre de pays
    f.write("Nombre de pays:\n")
    f.write(str(region['Country'].nunique()) + "\n\n")
    
    # Nombre de valeurs différentes dans la colonne 'region'
    f.write("Nombre de valeurs différentes dans 'region':\n")
    f.write(str(region['region'].nunique()) + "\n\n")
    
    # Statistiques descriptives
    f.write("Statistiques descriptives:\n")
    f.write(str(region.describe()) + "\n\n")
    
    # Analyser les valeurs uniques et doublons
    f.write("Nombre de valeurs uniques dans 'Country':\n")
    f.write(str(region['Country'].nunique()) + "\n\n")
    f.write("Nombre de doublons:\n")
    f.write(str(region.duplicated().sum()) + "\n\n")
