import requests
import json

def emotion_detector(text_to_analyze):

     
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    input_json = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = input_json, headers=header)

    print("status_code from NLP:", response.status_code)
   
    if response.status_code == 200:
        formated_response = json.loads(response.text)
        emotion_dict = formated_response['emotionPredictions'][0]['emotion']
        anger_score = emotion_dict['anger']
        disgust_score = emotion_dict['disgust']
        fear_score = emotion_dict['fear']
        joy_score = emotion_dict['joy']
        sadness_score = emotion_dict['sadness']

        score_list =  [anger_score, disgust_score, fear_score, joy_score, sadness_score]

        for key, value in emotion_dict.items():
            if value == max(score_list):
                global dominant_emotion
                dominant_emotion = key
                break

        return {
            'anger' : anger_score,
            'disgust' : disgust_score,
            'fear' : fear_score,
            'joy' : joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
            }

    elif response.status_code == 400 or response.status_code == 500:
        return {
            'anger' : None,
            'disgust' : None,
            'fear' : None,
            'joy' : None,
            'sadness': None,
            'dominant_emotion': None
            }


