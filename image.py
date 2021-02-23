import cv2 as cv
import sys
import time

def main():
	img = cv.imread(cv.samples.findFile("gattocovid.jpg"))
	if img is None:
		sys.exit("Non riesco a trovare l'immagine")
	cv.imshow("Finestra di prova", img)
	cv.waitKey(0)



if __name__=="__main__":
	main()