import argh
import cv2
from PIL import Image
import numpy as np


def reduce_colors(img_kmeans, number_of_colors):
    '''
    This function was develop following:
    https://docs.opencv.org/4.5.2/d1/d5c/tutorial_py_kmeans_opencv.html
    '''
    # Transform to 2d array
    # Our image has a width w and a height h, and we need to transform the shape of the 
    # image into a Nx3 shape, where N is the w*h product, and 3 is for the 3 colors. 
    # This is needed so that we can pass the image to the kmeans method of opencv.
    
    global clustered_image
    reshaped_image = np.float32(img_kmeans.reshape(-1, 3))

    k = number_of_colors

    stop_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 5.0)
    #(cv2.TERM_CRITERIA_MAX_ITER, 300)


    ret, labels, clusters = cv2.kmeans(reshaped_image,k, None, stop_criteria, 10, cv2.KMEANS_RANDOM_CENTERS)


    clusters = np.uint8(clusters)
    intermediate_image = clusters[labels.flatten()]

    
    clustered_image = intermediate_image.reshape((img_kmeans.shape))
    
    return clustered_image
    

if __name__ == '__main__':
    argh.dispatch_command(reduce_colors)
    

# Test function -----------------------------------------------------------------

#Image.fromarray(img_kmeans).show()
# image = Image.open(path_to_image)
# image_array = np.array(image)
# reduce_colors(image_array, number_of_colors = 5)
