import pandas as pd

# Importer le fichier de données
acces_potable = pd.read_csv('accesPotable.csv')

# Créer un fichier pour enregistrer les résultats
with open('resultats_analyse_acces_potable.txt', 'w') as f:
    # Vérifier les types de données dans chaque colonne
    f.write("Types de données dans 'acces_potable':\n")
    f.write(str(acces_potable.dtypes) + "\n\n")
    
    # Vérifier les valeurs manquantes
    f.write("Valeurs manquantes dans 'acces_potable':\n")
    f.write(str(acces_potable.isnull().sum()) + "\n\n")
    
    # Afficher les 10 premières lignes
    f.write("Les 10 premières lignes de 'acces_potable':\n")
    f.write(str(acces_potable.head(10)) + "\n\n")
    
    # Nombre de pays
    f.write("Nombre de pays:\n")
    f.write(str(acces_potable['Country'].nunique()) + "\n\n")
    
    # Nombre de valeurs différentes dans la colonne 'Granularity'
    f.write("Nombre de valeurs différentes dans 'Granularity':\n")
    f.write(str(acces_potable['Granularity'].nunique()) + "\n\n")
    
    # Statistiques descriptives
    f.write("Statistiques descriptives:\n")
    f.write(str(acces_potable.describe()) + "\n\n")
    
    # Analyser les valeurs uniques et doublons
    f.write("Nombre de valeurs uniques dans 'Country':\n")
    f.write(str(acces_potable['Country'].nunique()) + "\n\n")
    f.write("Nombre de doublons:\n")
    f.write(str(acces_potable.duplicated().sum()) + "\n\n")
