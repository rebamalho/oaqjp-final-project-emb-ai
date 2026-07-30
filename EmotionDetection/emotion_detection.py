import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    texto = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=texto, headers = headers)
    var_txt = response.text
    var_dict = json.loads(var_txt)
    anger_score = var_dict['emotionPredictions'][0]['emotion']['anger']
    disgust_score = var_dict['emotionPredictions'][0]['emotion']['disgust']
    fear_score = var_dict['emotionPredictions'][0]['emotion']['fear']
    joy_score = var_dict['emotionPredictions'][0]['emotion']['joy']
    sadness_score = var_dict['emotionPredictions'][0]['emotion']['sadness']
    dominant_emotion = max(var_dict['emotionPredictions'][0]['emotion'], key = var_dict['emotionPredictions'][0]['emotion'].get)

    return {
    'anger': anger_score,
    'disgust': disgust_score,
    'fear': fear_score,
    'joy': joy_score,
    'sadness': sadness_score,
    'dominant_emotion': dominant_emotion
    }
