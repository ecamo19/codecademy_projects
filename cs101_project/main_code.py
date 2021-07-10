# Packages ----------------------------------------------------------------------
import cv2
from PIL import Image
import numpy as np
from functions.count_colors import *

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
        path_to_image = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/codeacademy/projects/cs101_final_project/test_images/bird.png'
         
        # Read image PIL, here the image is not an array
        image = Image.open(path_to_image) 
        
        # -----------------------------------------------------------------------


