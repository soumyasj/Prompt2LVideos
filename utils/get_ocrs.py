#Script to obtain ocr tokens of the frames of videos using easyocr and write in a json file
import os
import json
import cv2
from tqdm import tqdm 
import easyocr


#function to obtain OCR tokens given frames
def get_ocr_info(input_video_wise_frame_path, output_video_wise_ocr_path, folder, already_done):

    for fold in tqdm(range(len(folder))):
        if str(fold)+".json" not in already_done:

            all_images = input_video_wise_frame_path+folder[fold]
            output_p = output_video_wise_ocr_path
            all_images_folder = os.listdir(all_images)
            reader = easyocr.Reader(['en'])
            all_ocrs = []

            for i in (range(len(all_images_folder))):
                each_dict = {}
                img_path = all_images + "/" +str(all_images_folder[i])
                text = reader.readtext(img_path)
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



if __name__=="__main__":

    #define paths
    input_video_wise_frame_path = "../frames/"
    output_video_wise_ocr_path = "../ocrs/"
    folder = os.listdir(input_video_wise_frame_path)
    already_done = os.listdir(output_video_wise_ocr_path)

    get_ocr_info(input_video_wise_frame_path, output_video_wise_ocr_path, folder, already_done)