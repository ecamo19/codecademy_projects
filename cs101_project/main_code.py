# Packages ----------------------------------------------------------------------
import cv2
from PIL import Image
import numpy as np
import argh

# Load selfmade functions
from functions.count_colors import *
from functions.k_means import *

# -------------------------------------------------------------------------------
print("\nPlease,enter the path where your image is stored")
print("\tpath example: '/path/to/image.jpg'")
print("\tFor quitting the program enter quit.")

flag = True
while True:

# Get image path from user ------------------------------------------------------
 
    path_to_image = input("\nPath to image:")
    
    if path_to_image == "quit":
        flag = False
        print("\n\tBye!\n")
        break   
    
    else:   
        print(f'\n Your image is located at {path_to_image}\n')
        # Read images using PIL -------------------------------------------------
        
        # TEST DELETE AT THE END
        path_to_image = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/codeacademy/codecademy_projects/cs101_project/test_images/bird.png'
         
        # Read image PIL, here the image is not an array
        image = Image.open(path_to_image) 
        
        #Probar se image sirve en el kmeans
        
        # images for kmeans
        img = cv2.imread(path_to_image, cv2.COLOR_BGR2RGB)
        img_kmeans = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        
# Count colors function ---------------------------------------------------------
        
        count_colors(image)

# Reduce colors -----------------------------------------------------------------
        print("\nDo you want to reduce the colors of your image:")
        reduce_colors = input("yes or no: ")
        
        if reduce_colors == "no":
            flag = False
            print("\n\tBye!\n")
            break 
            
        else:
            number_of_colors = int(input("How many colors do you want to display: "))
            reduce_colors(img_kmeans,number_of_colors)
           

