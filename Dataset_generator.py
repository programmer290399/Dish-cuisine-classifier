import requests
import cv2
import os
from google_images_download import google_images_download 

response = google_images_download.googleimagesdownload()   
item = input("enter the keywords :")
num = input("Enter number of images to scrape :")
arguments = {"keywords": item ,"limit": int(num) ,"print_urls":True , 'chromedriver': 'H:\\rps\\python\\Food_Image_Classifier\\chromedriver.exe'}  
paths = response.download(arguments)   

path_list = paths[item]




print(path_list)

for imagePath in path_list:
	print('checking:' , imagePath)
	delete = False

	try:
		image = cv2.imread(imagePath)

		if image is None:
			print("None")
			delete = True

	except:
		print("Except")
		delete = True

	if delete:
		print("[INFO] deleting {}".format(imagePath))
		os.remove(imagePath)