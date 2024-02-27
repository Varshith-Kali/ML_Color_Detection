# Color Detection using Pandas & OpenCV...
import cv2
import argparse
import pandas as pd



ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help='Image Path')
args = vars(ap.parse_args())

img_path = args['image']
img = cv2.imread(img_path)

index = ["color_name", "color", "hex", "R", "G", "B"]
csv = pd.read_csv