from cgitb import small, text
import os
import json
from tqdm import tqdm
from random import sample
import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration

def abstractive_summarization(text):
    # Check if GPU is available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load pre-trained T5 model and tokenizer on the GPU
    model_name = "t5-small"  # You can also use "t5-base", "t5-large", or other variants for better performance.
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

    # Preprocess the text for summarization
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True).to(device)

    # Generate the summary
    summary_ids = model.generate(inputs, max_length=150, num_beams=4, early_stopping=True)

    # Decode the summary IDs into text
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

def main():
    data = json.load(open('../path_to_your_json_file.json')) #json file should contain name of the videos
    all_d = []
    for i in tqdm(data):
        each_d = {}
        each_d['clip_id'] = i['clip_id']
        text_to_summarize_l = []
        for j in i['transcript']:
            text_to_summarize_l.append(j['transcript'])
        
        text_to_summarize = ' '.join(text_to_summarize_l)
        summary = abstractive_summarization(text_to_summarize)
        each_d['summary'] = summary
        all_d.append(each_d)


    with open('../name_of_output_file.json', 'w') as f:
        json.dump(all_d, f)

if __name__=="__main__":
    main()