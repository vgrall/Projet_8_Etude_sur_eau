import pandas as pd

# Importer le fichier de données
mortalite = pd.read_csv('mortalite.csv')

# Créer un fichier pour enregistrer les résultats
with open('resultats_analyse_mortalite.txt', 'w') as f:
    # Vérifier les types de données dans chaque colonne
    f.write("Types de données dans 'mortalite':\n")
    f.write(str(mortalite.dtypes) + "\n\n")
    
    # Vérifier les valeurs manquantes
    f.write("Valeurs manquantes dans 'mortalite':\n")
    f.write(str(mortalite.isnull().sum()) + "\n\n")
    
    # Afficher les 10 premières lignes
    f.write("Les 10 premières lignes de 'mortalite':\n")
    f.write(str(mortalite.head(10)) + "\n\n")
    
    # Nombre de pays
    f.write("Nombre de pays:\n")
    f.write(str(mortalite['Country'].nunique()) + "\n\n")
    
    # Nombre de valeurs différentes dans la colonne 'Granularity'
    f.write("Nombre de valeurs différentes dans 'Granularity':\n")
    f.write(str(mortalite['Granularity'].nunique()) + "\n\n")
    
    # Statistiques descriptives
    f.write("Statistiques descriptives:\n")
    f.write(str(mortalite.describe()) + "\n\n")
    
    # Analyser les valeurs uniques et doublons
    f.write("Nombre de valeurs uniques dans 'Country':\n")
    f.write(str(mortalite['Country'].nunique()) + "\n\n")
    f.write("Nombre de doublons:\n")
    f.write(str(mortalite.duplicated().sum()) + "\n\n")
