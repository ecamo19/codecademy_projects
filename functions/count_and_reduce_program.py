# Packages ----------------------------------------------------------------------
import cv2
from PIL import Image
import numpy as np
import glob
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import argh

# Load selfmade functions
from functions.count_colors import *
from functions.color_reduction_k_means import *


def count_and_reduce():
    
    """
    This function contains all for the color count and color reduction
    """

    print("\nPlease,enter the directory where your images are stored")
    print("...or enter the word test to analize test images included ")
    print("\npath example: '/path/to/'")
    print("\tFor quitting the program enter quit.")

    flag = True
    while True:

    # Get image path from user -------------------------------------------------
        path_to_image = input("\n Where are your images stored? or enter the word test: ")
        if path_to_image == "quit":
            flag = False
            print("\n\tBye!\n")
            break   

        elif path_to_image == "test":
            path_to_image = "test_images"

        # Read images available in the folder ----------------------------------
        print("\nImages available: ")

        for each_image in os.listdir(path_to_image):

            if each_image.endswith('png') or each_image.endswith('jpg'):        
                print(f'\t> {os.path.basename(each_image)}')

        # Choose image ---------------------------------------------------------
        image_name = input('\nWhich image do you want to analize?: ')
        if image_name == "quit":
            flag = False
            print("\n\tBye!\n")
            break  

        else:
            # Read images using PIL --------------------------------------------
            # image is not an array
            image = Image.open(f'{path_to_image}/{image_name}') 

            # Image for kmeans, convert image to array
            img_kmeans = np.array(image)

            # Count colors function --------------------------------------------

            count_colors(image)

            # Reduce colors ----------------------------------------------------
            print("\nDo you want to reduce the colors of your image:")
            quantization = input("yes or no: ")

            if quantization != "yes":
                    flag = False
                    print("\n\tBye!\n")
                    break 

            else:

                # Color reduction
                number_of_colors = int(input("How many colors do you want to display: "))
                clustered_image = reduce_colors(img_kmeans, number_of_colors = number_of_colors)

                # Concatanate images horizontally
                horizontal_images = np.concatenate((image, clustered_image), axis=1)
                figure(figsize=(20, 15), dpi = 300)

                fig = plt.imshow(horizontal_images)

                fig.axes.get_xaxis().set_visible(False)
                fig.axes.get_yaxis().set_visible(False)

                plt.show()

                print("\nDo you want to save your new image:")
                save_image = input("yes or no: ")

                if save_image == "no":
                    continue

                elif save_image == "yes":
                    print("\tPlease specify where the image should be saved")
                    print("\tPath example: '/path/to/save'")
                    path_to_save = input("\nPath: ")
                    image_name = input("\nImage name: ")
                    cv2.imwrite(f'{path_to_save}/{image_name}.jpg',cv2.cvtColor(clustered_image,                               cv2.COLOR_RGB2BGR))
                    cv2.waitKey(0)
                    print("\n> Image saved!")
                    flag = False
                    print("\n\tBye!\n")
                    break 

if __name__ == '__main__':
    argh.dispatch_command(count_and_reduce)