#Code used to do random testing. It can be modified based on the predictions of the model

import random
import os
import json
from tqdm import tqdm
import numpy as np
import random


#function to obtain scores; returns a dict containing R@1, R@5, R@10
def evaluate(matrix):

    txt2img = {}
    for i in range(60):
        txt2img[i] = i


    pred = np.asarray(matrix)
    ranks = np.zeros(pred.shape[0])

    for index, score in enumerate(pred):
        inds = np.argsort(score)[::-1]
        gt_img_ids = txt2img[index]
        if isinstance(gt_img_ids, int):
            ranks[index] = np.where(inds == gt_img_ids)[0][0]

    ir1 = 100.0 * len(np.where(ranks < 1)[0]) / len(ranks)
    ir5 = 100.0 * len(np.where(ranks < 5)[0]) / len(ranks)
    ir10 = 100.0 * len(np.where(ranks < 10)[0]) / len(ranks)

    ir_mean = (ir1 + ir5 + ir10) / 3

    eval_result = {
                    "img_r1": ir1,
                    "img_r5": ir5,
                    "img_r10": ir10,
                    "img_r_mean": ir_mean,
                    }
    eval_result = {k: round(v, 2) for k, v in eval_result.items()}

    return eval_result


def main():
    # Create a 2D list with dimensions [60, 60] filled with numbers from 0 to 59 as the test set has 60 video-caption pairs and shuffle them to make random predictions
    matrix = [[j for j in range(60)] for _ in range(60)]
    for row in matrix:
        random.shuffle(row)
    
    eval_result = evaluate(matrix)

    with open('../test_res.json', 'w') as f:
        json.dump(eval_result, f)