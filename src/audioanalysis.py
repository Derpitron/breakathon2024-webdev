
import requests

API_URL = "https://api-inference.huggingface.co/models/ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition"
headers = {"Authorization": "Bearer hf_***"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = query("tmp/flac_output.flac")

import json

def get_highest_score_label(json_data):
    try:
        if isinstance(json_data, str):
            data = json.loads(json_data)
        elif isinstance(json_data, list):
            data = json_data
        else:
            return None
            
        if not data:
            return None

        highest_score = -1
        highest_score_label = None

        for item in data:
            if isinstance(item, dict) and "score" in item and "label" in item:
                score = item["score"]
                if isinstance(score,(int,float)) and score > highest_score:
                    highest_score = score
                    highest_score_label = item["label"]
            else:
                print("Warning: Invalid item in JSON data:", item)
                
        return highest_score_label

    except json.JSONDecodeError:
        print("Invalid JSON string provided.")
        return None
    
get_highest_score_label(output) #returns the highest value of the score and the corresponding emotion 