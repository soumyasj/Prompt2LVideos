#Script to obtain ocr tokens of the frames of videos using easyocr and write in a json file
import os
import json
import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm 
from decord import VideoReader
from pytesseract import pytesseract
from matplotlib import pyplot as plt
import easyocr




#ocr based on frames of a video

folder_p = "/home/soumya/Desktop/Research-2023/MS-Thesis/IndependentProject/dataset_repo/video_wise_frames/climate_sky_news/"
output_p = "/home/soumya/Desktop/Research-2023/MS-Thesis/IndependentProject/dataset_repo/ocr/climate_sky_news/"
folder = os.listdir(folder_p)

already_done = os.listdir(output_p)

# print(folder[0])
# exit()
for fold in tqdm(range(len(folder))):
# fold = 0

    if str(fold)+".json" not in already_done:

        all_images = folder_p+folder[fold]
        output_p = output_p


        all_images_folder = os.listdir(all_images)
        reader = easyocr.Reader(['en'])
        # print("HI")
        # exit()
        all_ocrs = []

        for i in (range(len(all_images_folder))):
            each_dict = {}
            img_path = all_images + "/" +str(all_images_folder[i])
            # print(img_path)
            # exit()
            text = reader.readtext(img_path)
            # print(text)
            # exit()
            each_dict["image_path"] = str(all_images_folder[i])
            all_text = []
            for w in text:
                all_text.append(w[1])
            all_text_str = ' '.join(all_text)
            if all_text_str=="":
                each_dict["text"] = "--"
            else:
                each_dict["text"] = all_text_str    
            all_ocrs.append(each_dict)

        out_file = output_p + str(fold) + ".json"
            
        with open(out_file, "w") as f:
            json.dump(all_ocrs, f)

    else:
        print("already_done")


exit()

all_images = "/home/soumya/Desktop/Research-2023/MS-Thesis/IndependentProject/dataset_repo/frames/"
all_images_folder = os.listdir(all_images)
reader = easyocr.Reader(['en'], gpu=False)
# print("HI")
# exit()
all_ocrs = []

for i in tqdm(range(len(all_images_folder))):
    each_dict = {}
    img_path = "/home/soumya/Desktop/Research-2023/MS-Thesis/IndependentProject/dataset_repo/frames/" + str(all_images_folder[i])
    # print(img_path)
    # exit()
    text = reader.readtext(img_path)
    # print(text)
    # exit()
    each_dict["image_path"] = str(all_images_folder[i])
    all_text = []
    for w in text:
        all_text.append(w[1])
    all_text_str = ' '.join(all_text)
    if all_text_str=="":
        each_dict["text"] = "--"
    else:
        each_dict["text"] = all_text_str    
    all_ocrs.append(each_dict)
    
with open("breaking_news_and_health_sky_news.json", "w") as f:
    json.dump(all_ocrs, f)



