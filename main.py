import os 
import sys 
import time 

from ConfigParser import cwd, image_path, compressed_image_path
from app import get_image_compressed

start_time = time.time()

image_name = input("Enter the file path of the image to be compressed without <quotes> -> ")

(get_image_compressed(image_name, image_path, compressed_image_path))

end_time = time.time()
print("Total Time taken in seconds: ", round(end_time - start_time,2))