# Packages ----------------------------------------------------------------------
#import cv2
#from PIL import Image
#import numpy as np
#import glob
#import os

# Load selfmade functions
#from functions.count_colors import *
#from functions.k_means import *

# -------------------------------------------------------------------------------
#print("\nPlease,enter the path where your images are stored")
#print("\tpath example: '/path/to/'")
#print("\tFor quitting the program enter quit.")

#flag = True

#while True:

# Get image path from user ------------------------------------------------------

#    path_to_image = input("\nPath where images are stored: ")
#    if path_to_image == "quit":
#        flag = False
#        print("\n\tBye!\n")
#        break   
    
#    else:
        #/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/codeacademy/codecademy_projects/cs101_project/test_images
#        print("\nImages available: ")
#        for each_image in os.listdir(path_to_image):
#            if ".jpg" in each_image or ".png" in each_image or ".jpeg" in each_image:        
#                print(f'\t> {os.path.basename(each_image)}')
                
#        image_name = input('\nWhich image do you want to analize?: ')
        
        # Read images using PIL -------------------------------------------------
        # Read image PIL, here the image is not an array
#        image = Image.open(f'{path_to_image}/{image_name}') 
        
        # Image for kmeans, convert image to array
#        img_kmeans = np.array(image)
        
# Count colors function ---------------------------------------------------------
        
 #       count_colors(image)
       
# Reduce colors -----------------------------------------------------------------
 #       print("\nDo you want to reduce the colors of your image:")
 #       quantization = input("yes or no: ")
        
#        if quantization != "yes":
#            flag = False
#            print("\n\tBye!\n")
#            break 
           
#        else:
            
#            number_of_colors = int(input("How many colors do you want to display: "))
#            clustered_image = reduce_colors(img_kmeans, number_of_colors = number_of_colors)
        
            # concatanate image Horizontally
#            horizontal_images = np.concatenate((image, clustered_image), axis=1)
            
#            cv2.imshow('comparition', cv2.cvtColor(horizontal_images, cv2.COLOR_RGB2BGR))
#            cv2.waitKey(0)
            
#            print("\nDo you want to save your new image:")
#            save_image = input("yes or no: ")
            
#            if save_image == "no":
#                continue

#            elif save_image == "yes":
#                print("\tPlease specify where the image should be saved")
#                print("\tPath example: '/path/to/save'")
#                path_to_save = input("\nPath: ")
#                image_name = input("\nImage name: ")
#                cv2.imwrite(f'{path_to_save}/{image_name}.jpg',cv2.cvtColor(clustered_image, cv2.COLOR_RGB2BGR))
#                cv2.waitKey(0)
#                print("\n> Image saved!")
#                flag = False
#                print("\n\tBye!\n")
 
 
 
#
#
#
#
#
#
#
#
#    



