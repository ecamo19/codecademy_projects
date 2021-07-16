import argh

# Count number of colors in image -----------------------------------------------

def count_colors(image):
    """
    This function was developed using this repository:
    https://github.com/townsean/pixel-color-count/blob/master/pixel-color-count.py
    by Ashley Grenon https://github.com/townsean
    
    The function register the RGB values (eg: 0,0,4) of each single pixel.
    A color is define here a combination of the three posible combinations of
    RGB values.
    
    For example if one pixel has a value of [0,0,0] this is register as a color 
    while a pixel with a value of  [0,0,1] is register as a new color
    
    """
    
    # Get dimmension of the image 
    width, height = image.size
    
    # Covert image to RGB
    rgb_image = image.convert('RGB')
    
    # Create empty dictinary to store the RGB
    color_count = {}
    
    # Iterate through each single pixel in the image and keep a count of the 
    # RGB values of each single pixel
    
    for each_column in range(width):
        for each_row in range(height):
            
            # Get RGB value
            rgb = rgb_image.getpixel((each_column, each_row))
            
            # Add it to the dictionary
            if rgb in color_count:
                color_count[rgb] += 1
            else:
                color_count[rgb] = 1
    
    # Print the total number of colours.
    print(f'\n> Your image has {len(color_count.keys())} different colors\n')


if __name__ == '__main__':
    argh.dispatch_command(count_colors)
    

# Test function -----------------------------------------------------------------
# Load packages
# import cv2
# from PIL import Image
# import numpy as np
# import argh

# path_to_image = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/codeacademy/projects/cs101_final_project/test_images/bird.png'
#          
# # Read image PIL, here the image is not an array
# image = Image.open(path_to_image)
# 
# count_colors(image)





