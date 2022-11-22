import easyocr
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
import cv2
import os
import time
from os import listdir

 # Création fichier texte pour résultats
file_objects = open('gros_resultat','w')
dir_path = ('F:/Projets Pilgrim Technology/Airport 2020/images/OCR/OCR1/NikonD3200-24Mpx-photos-refrigerants/')

 # Chemin répertoire pour sauvegarde
script_dir = os.path.dirname(__file__)
results_dir = os.path.join(script_dir, 'Output/')

reader = easyocr.Reader(['en'],True)  # Chargement model
font = cv2.FONT_HERSHEY_SIMPLEX  # Font

for file in os.listdir(dir_path): 
     # Image à tester
    img_name = os.path.join(dir_path, file)
     # image_path = "images/" + img_name
     # On enregistre l'heure de début
    start = time.time()
    result = reader.readtext(img_name)
     # On enregistre l'heure de fin 
    end = time.time()
    process_time = (end - start) * 10**3
    img = cv2.imread(img_name)

    # Détection multi caractères
    for i in result:
        top_left = tuple([int(val) for val in i[0][0]])
        bottom_right = tuple([int(val) for val in i[0][2]])
        text = i[1]
        img = cv2.rectangle(img , top_left, bottom_right ,(255,255,0),5)  #cadre
        img = cv2.putText(img , text , top_left , font , 10 , (255,0,0),15)
       # raw_data = {'Date': [time.asctime( time.localtime(time.time()) )],'Nom du fichier':[img_name],'Numéro container': [text], "Temps d'execution": [process_time]}
        data = img_name +";"+ str(process_time) +";"+ text + "\n"
        file_objects.write(data)
      
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.savefig("output/"+ file) # Sauvegarde

file_objects.close()

print("That's all folks")  