# Packages ----------------------------------------------------------------------
import cv2
from PIL import Image
import numpy as np
import argh
import webbrowser


# Load selfmade functions
from functions.count_colors import *
from functions.k_means import *



# -------------------------------------------------------------------------------
print("\nPlease,enter the path where your image is stored")
print("\tpath example: '/path/to/image.jpg'")
print("\tFor quitting the program enter quit.")

flag = True

d = 0
while True:

# Get image path from user ------------------------------------------------------
 
    path_to_image = input("\nPath to image:")
    if path_to_image == "quit":
        flag = False
        print("\n\tBye!\n")
        break   
    
    else:   
        print(f'\n\tYour image is located at {path_to_image}\n')
        # Read images using PIL -------------------------------------------------
        
        # TEST DELETE AT THE END
        path_to_image = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/codeacademy/codecademy_projects/cs101_project/test_images/bird.png'
        
        # Read image PIL, here the image is not an array
        image = Image.open(path_to_image) 
        
        # Image for kmeans
        img_kmeans = np.array(image)
        
        
# Count colors function ---------------------------------------------------------
        
        count_colors(image)

# Reduce colors -----------------------------------------------------------------
        print("\nDo you want to reduce the colors of your image:")
        quantization = input("yes or no: ")
        
        if quantization != "yes":
            flag = False
            print("\n\tBye!\n")
            break 
           
        else:
            number_of_colors = int(input("How many colors do you want to display: "))
            
            clustered_image = reduce_colors(img_kmeans, number_of_colors = number_of_colors)
            
            # concatanate image Horizontally
            horizontal_images = np.concatenate((image, clustered_image), axis=1)
              
            cv2.imshow('comparition', cv2.cvtColor(horizontal_images, cv2.COLOR_RGB2BGR))
         
            #cv2.waitKey(1000000)
            cv2.destroyAllWindows()
            
            
            print("\nDo you want to save your new image:")
            save_image = input("yes or no: ")
            
        
            if save_image == "no":
                continue

            elif save_image == "yes":
                print("\tPlease specify where the image should be saved")
                print("\tPath example: '/path/to/save'")
                path_to_save = input("\nPath: ")
                image_name = input("\nImage name: ")
                cv2.imwrite(f'{path_to_save}/{image_name}.jpg',cv2.cvtColor(clustered_image, cv2.COLOR_RGB2BGR))
                cv2.waitKey(0)
                print("\nImage saved!")
             



