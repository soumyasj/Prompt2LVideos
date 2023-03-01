# #Code to convert videos to frames based on fps (1 frame per second)

# import os
# import json
# import cv2
# import numpy as np
# from PIL import Image
# from tqdm import tqdm 
# from decord import VideoReader
# from pytesseract import pytesseract
# from matplotlib import pyplot as plt
# import easyocr

# folder_path = "/home/soumya/Desktop/Research-2023/MS-Thesis/IndependentProject/dataset_repo/health_sky_news_small/"
# output_folder = "/home/soumya/Desktop/Research-2023/MS-Thesis/IndependentProject/dataset_repo/frames/"
# folder = os.listdir(folder_path)

# for i in tqdm(range(len(folder))):
#     vid_path = folder_path + folder[i]
#     output_vid_path = output_folder + folder[i].split(".mp4")[0]
#     vidcap = cv2.VideoCapture(vid_path)
#     vr = VideoReader(vid_path)
#     fps = int(vr.get_avg_fps())
#     success,image = vidcap.read()
#     count = 0
#     nct = 0
#     # print(success)
#     # exit()
#     while (success):
#         success,image = vidcap.read()
#         if count % fps == 0:
#             written_path = output_vid_path + "_" +str(nct) + ".jpg"
#             nct+=1
#             cv2.imwrite(written_path, image) 
#         count += 1

#     print(count, fps, nct)




#Code to convert videos to frames based on fps (1 frame per second) video present in each folder

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

folder_path = "/home/soumya/Desktop/Research-2023/MS-Thesis/IndependentProject/dataset_repo/videos/sports_sky_news/"
output_folder = "/home/soumya/Desktop/Research-2023/MS-Thesis/IndependentProject/dataset_repo/video_wise_frames/sports_sky_news/"
folder_new = os.listdir(folder_path)

for i in tqdm(range(len(folder_new))):
    try:
        folder = [folder_new[i]]
        video_name = os.listdir(folder_path+folder[0])
        out_path = output_folder+ "/" + folder[0] + "/"  
        if not os.path.exists(out_path):
            os.makedirs(out_path)
            vid_path = folder_path + folder[0] + "/" + video_name[0]
            vidcap = cv2.VideoCapture(vid_path)
            vr = VideoReader(vid_path)
            fps = int(vr.get_avg_fps())
            success,image = vidcap.read()
            count = 0
            nct = 0
            while (success):
                success,image = vidcap.read()
                if count % fps == 0:
                    try:
                        written_path = out_path + folder[0] + "_" + str(nct) + ".jpg"
                        nct+=1
                        cv2.imwrite(written_path, image)
                    except:
                        pass
                count+=1
    except:
        print("video error")
