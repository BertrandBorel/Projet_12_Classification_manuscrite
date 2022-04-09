import os
import cv2
import random
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# Chemin des images
chemin = "./test_pictures/"
liste_test = os.listdir(chemin) 


# on choisi une image aléatoire à chaque fois
rand = random.choice(liste_test)

# on décide du nouveau chemin de l'élément aléatoire
route = "./test_pictures/" + rand

# on affiche l'élément aléatoire avec la variable route
image = cv2.imread(route)

plt.figure(figsize=(2,2))
plt.subplot()
plt.xticks([])
plt.yticks([])
plt.imshow(image)
plt.show()

## Formatage des images 
img_array = np.array(image)/255.0
img = np.expand_dims(img_array, axis=0)

# Prédiction 
filepath = './modelCNN'
liste_label = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
loaded_model = tf.keras.models.load_model(filepath)
prediction = loaded_model.predict(img)

resultat = liste_label[np.argmax(prediction)]
print('Prédiction :',resultat)