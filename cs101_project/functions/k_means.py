import argh
import cv2
from PIL import Image
import numpy as np


def reduce_colors(img_kmeans, number_of_colors):
    '''
    # see this https://muthu.co/reduce-the-number-of-colors-of-an-image-using-k-means-clustering/
    #https://programmerbackpack.com/k-means-clustering-for-image-segmentation/

    '''
    # Transform to 2d array
    # Our image has a width w and a height h, and we need to transform the shape of the 
    # image into a Nx3 shape, where N is the w*h product, and 3 is for the 3 colors. 
    # This is needed so that we can pass the image to the kmeans method of opencv.

    reshaped_image = np.float32(img_kmeans.reshape(-1, 3))

    k = number_of_colors

    stop_criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 5.0)
    #(cv2.TERM_CRITERIA_MAX_ITER, 300)


    ret, labels, clusters = cv2.kmeans(reshaped_image, number_clusters, None, stopCriteria, 10, cv2.KMEANS_RANDOM_CENTERS)


    clusters = np.uint8(clusters)
    intermediateImage = clusters[labels.flatten()]


    clusteredImage = intermediateImage.reshape((img_kmeans.shape))
    Image.fromarray(clusteredImage).show()


if __name__ == '__main__':
    argh.dispatch_command(reduce_colors)
    

# Test function -----------------------------------------------------------------

path_to_image = '/home/ecamo19/Documents/cursos_libros_tutoriales/cursos/codeacademy/codecademy_projects/cs101_project/test_images/bird.png'
img = cv2.imread(path_to_image, cv2.COLOR_BGR2RGB)
img_kmeans = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
Image.fromarray(img_kmeans).show()


