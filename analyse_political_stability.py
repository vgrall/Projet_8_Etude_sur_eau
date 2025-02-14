import pandas as pd

# Importer le fichier de données
political_stability = pd.read_csv('PoliticalStability.csv')

# Créer un fichier pour enregistrer les résultats
with open('resultats_analyse_political_stability.txt', 'w') as f:
    # Vérifier les types de données dans chaque colonne
    f.write("Types de données dans 'political_stability':\n")
    f.write(str(political_stability.dtypes) + "\n\n")
    
    # Vérifier les valeurs manquantes
    f.write("Valeurs manquantes dans 'political_stability':\n")
    f.write(str(political_stability.isnull().sum()) + "\n\n")
    
    # Afficher les 10 premières lignes
    f.write("Les 10 premières lignes de 'political_stability':\n")
    f.write(str(political_stability.head(10)) + "\n\n")
    
    # Nombre de pays
    f.write("Nombre de pays:\n")
    f.write(str(political_stability['Country'].nunique()) + "\n\n")
    
    # Nombre de valeurs différentes dans la colonne 'Granularity'
    f.write("Nombre de valeurs différentes dans 'Granularity':\n")
    f.write(str(political_stability['Granularity'].nunique()) + "\n\n")
    
    # Statistiques descriptives
    f.write("Statistiques descriptives:\n")
    f.write(str(political_stability.describe()) + "\n\n")
    
    # Analyser les valeurs uniques et doublons
    f.write("Nombre de valeurs uniques dans 'Country':\n")
    f.write(str(political_stability['Country'].nunique()) + "\n\n")
    f.write("Nombre de doublons:\n")
    f.write(str(political_stability.duplicated().sum()) + "\n\n")
