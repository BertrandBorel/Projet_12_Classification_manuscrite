# Projet_12_Classification_manuscrite
---

## Contexte du projet
Ce brief a pour objectif de manipuler les images et les premiers pas des techniques de Deep Learning et CNN avec Tensorflow.

​

Dans ce brief, nous appliquons un apprentissage supervisé pour reconnaitre les chiffres à partir d’une image.

​

## Challenges

Manipulation des images.
Analyse, prétraitement et visualisation des images.
Manipulation et l’exploitation de la Bibliothèque Tensorflow.
Préparation d’un modèle CNN.
​

## Phases de brief

​

### Partie 1 : Base de données, Analyse et Préparation

​

Pour aborder cette problématique de la reconnaissance des chiffres, il est primordial d’avoir une DataSet. Pour cela, vous devez télécharger la Dataset MNIST (https://github.com/teavanist/MNIST-JPG).

​

Par la suite, il faut développer une boucle for pour lire les images et les charger sous forme un tenseur.

​

**Outils :**

– Import os

– Import cv2

– from sklearn.model_selection import train_test_split

– os.listdir(chemin)

– cv2.cvtColor(img, cv2.COLOR_GRAY2BGR) si besoin

– cv2.resize(img,(width,height), interpolation = cv2.INTER_AREA) si besoin

– Data.append(image) – Label.append(classe)

​

### Partie 2 : Architecture CNN sur Tensorflow

​

Cette deuxième partie est réservée pour développer une architecture CNN sur tensorflow, et lancée par la suite l’apprentissage de CNN. Calculer l’accuracy et la matrice de confusion sur les données de test, commenter les performances obtenues. Outil : https://www.tensorflow.org/tutorials/images/cnn

​

### Partie 3 : Tester l’efficacité du modèle

​

Nous cherchons à tester le modèle développer sur des nouvelles données. Pour un début, utiliser l’application Paint pour simuler des chiffres, et tester les performances de votre modèle sur les chiffres simulés.

​

Il sera intéressant de développer une application python pour reconnaitre automatiquement les chiffres en intégrant votre modèle CNN.

## Modalités pédagogiques
Le deadline pour rendre ce travail est fixé pour le 28 mars.

Le projet est réalisé en groupe de 2-3 personnes.

## Critères de performance
Le bon choix du modèle CNN.
Le bon fonctionnement de l'Application demandée.

## Modalités d'évaluation
L’évaluation de ce projet sera partagée entre :

La réalisation des différentes étapes décrite dans le contexte.
Les Notebooks demandés.

## Livrables
Un dépôt GitHub avec :
-   Un Notebook bien structuré/organisé qui réalise les différentes étapes de ce projet.
-   Un Readme.md pour mettre en avant votre projet.
