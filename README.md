# README - Projet de Datamining sur les Données de Photos Flickr

## Description
Ce projet de datamining vise à explorer et analyser les données issues de la plateforme Flickr. L'objectif est de segmenter les photos en clusters significatifs à l'aide de différentes méthodes de clustering, puis d'exploiter des techniques de text mining pour nommer ces clusters en fonction des tags associés aux images. Une analyse temporelle est également effectuée pour étudier l'évolution de l'utilisation des tags.

Une présentation détaillée du projet est disponible sur YouTube : [Lien vers la vidéo](https://www.youtube.com/watch?v=l4IeNgMNO3E)

## Objectifs
1. **Exploration des données** : Analyse initiale des données collectées
2. **Nettoyage des données** : Suppression des valeurs aberrantes, gestion des données manquantes, etc.
3. **Préparation des données pour le clustering** : Transformation des données pour une meilleure performance des algorithmes
4. **Clustering des données** :
   - K-Means
   - Clustering hiérarchique
   - DBSCAN
5. **Text Mining pour le nommage des clusters** :
   - TF-IDF
   - Algorithme Apriori
   - Règles d’association
6. **Analyse temporelle** :
   - Étude de la variation des tags par heure et par mois
   - Exclusion des tags temporels pour un nommage plus pertinent des clusters

## Technologies utilisées
- **Langages** : Python
- **Bibliothèques** : pandas, numpy, scikit-learn, nltk, mlxtend, matplotlib, seaborn

## Structure du projet
```
📂 LyonPhoto-DataMining
├── FD_project_2024_2025.pdf    # Consignes du projet
├── file.txt                    # Fichier contenant les tags (pour la visualisation)
├── flickr_data2.csv            # Données brutes de Flickr
├── project.ipynb               # Notebook Jupyter principal
├── map.html                    # Carte interactive
├── map1.html                   # Carte interactive
├── map2.html                   # Carte interactive
├── map3.html                   # Carte interactive
├── map4.html                   # Carte interactive
├── map5.html                   # Carte interactive
├── map6.html                   # Carte interactive
├── map7.html                   # Carte interactive
├── map8.html                   # Carte interactive
├── map9.html                   # Carte interactive
├── map10.html                  # Carte interactive
├── map11.html                  # Carte interactive
```

## Installation et exécution
1. **Cloner le dépôt**
```sh
git clone https://github.com/CLEMS3/LyonPhoto-DataMining.git
cd LyonPhoto-DataMining
```
2. **Lancer les notebooks Jupyter**

## Résultats et analyses
Les résultats finaux incluent :
- Une segmentation des photos en clusters pertinents
- Un nommage automatique des clusters basé sur l'analyse des tags
- Une étude des tendances temporelles dans l'utilisation des tags

## Auteurs
- **WILLEM Amaury** – https://github.com/memory5ty7
- **CHAPARD Clément** – https://github.com/CLEMS3

